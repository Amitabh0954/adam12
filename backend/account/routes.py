from flask import Blueprint, request, jsonify, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_mail import Mail, Message
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from .models import db, User, LoginAttempt, PasswordResetToken
from .schemas import UserSchema, LoginAttemptSchema, PasswordResetTokenSchema
from datetime import timedelta, datetime
import secrets

account_bp = Blueprint('account', __name__)
user_schema = UserSchema()
login_attempt_schema = LoginAttemptSchema()
password_reset_token_schema = PasswordResetTokenSchema()

@account_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    email = data['email']
    password = generate_password_hash(data['password'])
    
    new_user = User(email=email, password_hash=password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return user_schema.jsonify(new_user), 201

@account_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        attempt = LoginAttempt(user_id=user.id if user else None, success=False)
        db.session.add(attempt)
        db.session.commit()
        return jsonify({'message': 'Invalid credentials'}), 401

    attempt = LoginAttempt(user_id=user.id, success=True)
    db.session.add(attempt)
    db.session.commit()
    
    access_token = create_access_token(identity=user.id)
    session['user_id'] = user.id
    session.permanent = True
    session.modified = True

    return jsonify({'message': 'Login successful', 'user_id': user.id, 'access_token': access_token}), 200

@account_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@account_bp.before_request
def session_timeout():
    session.permanent = True
    account_bp.permanent_session_lifetime = timedelta(minutes=30)
    session.modified = True

@account_bp.route('/password-reset-request', methods=['POST'])
def password_reset_request():
    data = request.get_json()
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    token = secrets.token_hex(50)
    expiry_date = datetime.utcnow() + timedelta(hours=24)
    password_reset_token = PasswordResetToken(token=token, user_id=user.id, expiry_date=expiry_date)
    
    db.session.add(password_reset_token)
    db.session.commit()
    
    reset_link = url_for('account.reset_password', token=token, _external=True)
    send_password_reset_email(user.email, reset_link)
    
    return jsonify({'message': 'Password reset email sent'}), 200

@account_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    password_reset_token = PasswordResetToken.query.filter_by(token=token).first()

    if not password_reset_token or not password_reset_token.is_valid():
        return jsonify({'message': 'Invalid or expired token'}), 400

    data = request.get_json()
    new_password = data.get('password')
    password_reset_token.user.password_hash = generate_password_hash(new_password)
    password_reset_token.is_used = True
    
    db.session.commit()

    return jsonify({'message': 'Password has been reset successfully'}), 200

def send_password_reset_email(to_email: str, reset_link: str) -> None:
    msg = Message(subject="Password Reset Request",
                  sender="noreply@ecommerce.com",
                  recipients=[to_email],
                  body=f"Please use the following link to reset your password: {reset_link}")
    mail.send(msg)
