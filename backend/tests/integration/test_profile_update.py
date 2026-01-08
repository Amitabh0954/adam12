import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_profile_update(client):
    response = client.post('/api/auth/register', json={
        'email': 'test@example.com',
        'password': 'securepassword'
    })
    assert response.status_code == 201

    login_response = client.post('/api/auth/login', json={
        'email': 'test@example.com',
        'password': 'securepassword'
    })
    assert login_response.status_code == 200

    client.set_cookie('localhost', 'session', login_response.headers['Set-Cookie'])
    
    profile_response = client.put('/api/auth/profile', json={
        'email': 'newtest@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    })
    assert profile_response.status_code == 200
    assert profile_response.get_json()['email'] == 'newtest@example.com'