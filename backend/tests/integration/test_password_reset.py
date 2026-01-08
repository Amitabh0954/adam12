import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_password_reset_request(client):
    response = client.post('/api/auth/register', json={
        'email': 'test@example.com',
        'password': 'securepassword'
    })
    assert response.status_code == 201

    response = client.post('/api/auth/password-reset', json={
        'email': 'test@example.com'
    })
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Password reset link sent'

def test_password_reset_confirm(client):
    response = client.post('/api/auth/password-reset', json={
        'email': 'test@example.com'
    })
    assert response.status_code == 200

    reset_token = ''  # Replace with the actual token printed in request_password_reset
    response = client.post('/api/auth/password-reset/confirm', json={
        'email': 'test@example.com',
        'token': reset_token,
        'new_password': 'newsecurepassword'
    })
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Password has been reset'