import pytest
from backend.app import create_app
from backend.models.products.product import Product

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_add_to_cart(client):
    client.set_cookie('localhost', 'session', 'user-session-id')  # Mock user login session

    product = Product(name='Test Product', description='A product used for testing', price=10.99)
    response = client.post('/api/products', json=product.dict())
    assert response.status_code == 201

    product_id = response.get_json()['id']

    cart_item = {'product': {'id': product_id}, 'quantity': 2}
    add_response = client.post('/api/cart', json=cart_item)
    assert add_response.status_code == 200
    assert len(add_response.get_json()['items']) == 1
    assert add_response.get_json()['items'][0]['quantity'] == 2

def test_fetch_cart(client):
    client.set_cookie('localhost', 'session', 'user-session-id')  # Mock user login session

    response = client.get('/api/cart')
    assert response.status_code == 200
    assert response.get_json() is not None