import unittest
from flask import Flask
from controllers.auth.login_controller import login_controller
from services.auth.login_service import LoginService

class LoginControllerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.register_blueprint(login_controller)
        cls.client = cls.app.test_client()
        cls.login_service = LoginService()

    def test_login_success(self):
        with self.app.app_context():
            self.login_service.login = lambda email, password: {'status': 200, 'message': 'Login successful'}
            response = self.client.post('/login', json={
                'email': 'testuser@example.com',
                'password': 'password123'
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'status': 200, 'message': 'Login successful'})

    def test_login_failure(self):
        with self.app.app_context():
            self.login_service.login = lambda email, password: {'status': 401, 'message': 'Invalid credentials'}
            response = self.client.post('/login', json={
                'email': 'testuser@example.com',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.get_json(), {'status': 401, 'message': 'Invalid credentials'})

    def test_logout_success(self):
        with self.app.app_context():
            self.login_service.logout = lambda user_id: {'status': 200, 'message': 'Logout successful'}
            response = self.client.post('/logout', json={
                'user_id': 1
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'status': 200, 'message': 'Logout successful'})

    def test_logout_failure(self):
        with self.app.app_context():
            self.login_service.logout = lambda user_id: {'status': 400, 'message': 'Logout failed'}
            response = self.client.post('/logout', json={
                'user_id': 1
            })
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_json(), {'status': 400, 'message': 'Logout failed'})

if __name__ == '__main__':
    unittest.main()