from flask import Blueprint, request, jsonify
from backend.models.user_model import User, db
from backend.models.password_reset_model import PasswordReset
from flask_mail import Mail, Message
import os
from datetime import datetime

mail = Mail()

bp = Blueprint('password_reset', __name__, url_prefix='/password_reset')

def send_reset_email(user_email, token):
    msg = Message('Password Reset Request',
                  sender=os.environ.get('MAIL_DEFAULT_SENDER'),
                  recipients=[user_email])
    msg.body = f"To reset your password, visit the following link: {request.url_root}reset/{token}\n\nIf you did not make this request, please ignore this email."
    mail.send(msg)

@bp.route('/request', methods=['POST'])
def request_reset():
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'No user with this email found'}), 404

    reset_token = str(uuid.uuid4())
    password_reset = PasswordReset(user_id=user.id, token=reset_token)
    db.session.add(password_reset)
    db.session.commit()

    send_reset_email(user.email, reset_token)

    return jsonify({'message': 'Password reset email sent'}), 200

@bp.route('/reset/<token>', methods=['POST'])
def reset_password(token):
    password_reset = PasswordReset.query.filter_by(token=token).first()

    if not password_reset or password_reset.expires_at < datetime.utcnow():
        return jsonify({'error': 'Invalid or expired token'}), 400

    password = request.json.get('password')
    if not password:
        return jsonify({'error': 'Password is required'}), 400

    user = User.query.get(password_reset.user_id)
    user.set_password(password)
    db.session.commit()

    db.session.delete(password_reset)
    db.session.commit()

    return jsonify({'message': 'Password reset successful'}), 200