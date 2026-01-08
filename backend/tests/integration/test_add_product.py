import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_add_product_success(client):
    response = client.post('/api/products', json={
        'name': 'Product 1',
        'description': 'A great product',
        'price': 19.99
    })
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Product added successfully'

def test_add_product_unique_name(client):
    response = client.post('/api/products', json={
        'name': 'Product 1',
        'description': 'Another great product',
        'price': 29.99
    })
    assert response.status_code == 400
    assert response.get_json()['message'] == 'Product name must be unique'