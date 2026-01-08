import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_delete_product(client):
    response = client.post('/api/products', json={
        'name': 'Product 1',
        'description': 'A great product',
        'price': 19.99
    })
    assert response.status_code == 201

    product_id = response.get_json()['id']

    client.set_cookie('localhost', 'session', 'admin-session-id')  # Mock admin login session
    
    delete_response = client.delete(f'/api/products/{product_id}', follow_redirects=True)
    assert delete_response.status_code == 200
    assert delete_response.get_json()['message'] == 'Product deleted successfully'

    get_response = client.get(f'/api/products/{product_id}')
    assert get_response.status_code == 404