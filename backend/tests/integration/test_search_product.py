import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_search_product(client):
    response = client.post('/api/products', json={
        'name': 'Test Product',
        'description': 'A product used for testing',
        'price': 9.99
    })
    assert response.status_code == 201

    search_response = client.get('/api/search?query=test')
    assert search_response.status_code == 200
    assert len(search_response.get_json()['products']) > 0

def test_search_product_pagination(client):
    for i in range(15):
        client.post('/api/products', json={
            'name': f'Product {i}',
            'description': 'Just another product',
            'price': 19.99
        })

    search_response = client.get('/api/search?query=product&page=2&page_size=5')
    assert search_response.status_code == 200
    assert len(search_response.get_json()['products']) == 5