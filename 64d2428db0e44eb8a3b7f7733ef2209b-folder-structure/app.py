# Epic Title: User Account Management

from flask import Flask, request, jsonify
from backend.repositories.user.user_repository import UserRepository
from backend.services.user.user_service import UserService

app = Flask(__name__)

user_repository = UserRepository()
user_service = UserService(user_repository)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = user_service.register_user(email, password)
    return jsonify(user_id=user.user_id, email=user.email), 201

if __name__ == '__main__':
    app.run(debug=True)