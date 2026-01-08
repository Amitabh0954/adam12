import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_login_success(client):
    response = client.post('/api/auth/register', json={
        'email': 'test@example.com',
        'password': 'securepassword'
    })
    assert response.status_code == 201

    response = client.post('/api/auth/login', json={
        'email': 'test@example.com',
        'password': 'securepassword'
    })
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Login successful'

def test_login_failure(client):
    response = client.post('/api/auth/login', json={
        'email': 'fake@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert response.get_json()['message'] == 'Invalid email or password'