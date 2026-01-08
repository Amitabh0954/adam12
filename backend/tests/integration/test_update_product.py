import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_update_product(client):
    response = client.post('/api/products', json={
        'name': 'Product 1',
        'description': 'A great product',
        'price': 19.99
    })
    assert response.status_code == 201

    product_id = response.get_json()['id']

    update_response = client.put(f'/api/products/{product_id}', json={
        'description': 'An updated product description'
    })
    assert update_response.status_code == 200
    assert update_response.get_json()['description'] == 'An updated product description'

def test_update_product_name_conflict(client):
    response = client.post('/api/products', json={
        'name': 'Product 1',
        'description': 'A great product',
        'price': 19.99
    })
    assert response.status_code == 201

    client.post('/api/products', json={
        'name': 'Product 2',
        'description': 'Another great product',
        'price': 29.99
    })
    
    product_id = response.get_json()['id']

    update_response = client.put(f'/api/products/{product_id}', json={
        'name': 'Product 2'
    })
    assert update_response.status_code == 400
    assert 'Product name must be unique' in update_response.get_json()['message']