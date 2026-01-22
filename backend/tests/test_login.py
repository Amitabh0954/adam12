import unittest
from backend.app import app

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_success(self):
        response = self.app.post('/login', data=dict(username='correct_user', password='correct_pass'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Successfully logged in', response.data)

    def test_login_failure(self):
        response = self.app.post('/login', data=dict(username='wrong_user', password='wrong_pass'))
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid credentials', response.data)

if __name__ == '__main__':
    unittest.main()
