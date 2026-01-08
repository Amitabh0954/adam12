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

def test_modify_cart_item(client):
    client.set_cookie('localhost', 'session', 'user-session-id')  # Mock user login session

    product = Product(name='Test Product', description='A product used for testing', price=10.99)
    response = client.post('/api/products', json=product.dict())
    assert response.status_code == 201

    product_id = response.get_json()['id']

    cart_item = {'product': {'id': product_id}, 'quantity': 2}
    client.post('/api/cart', json=cart_item)

    modify_response = client.put(f'/api/cart/{product_id}', json={'quantity': 5})
    assert modify_response.status_code == 200
    assert modify_response.get_json()['message'] == 'Cart updated successfully'
    assert modify_response.get_json()['cart']['items'][0]['quantity'] == 5

def test_modify_cart_item_invalid_quantity(client):
    client.set_cookie('localhost', 'session', 'user-session-id')

    product = Product(name='Test Product', description='A product used for testing', price=10.99)
    response = client.post('/api/products', json=product.dict())
    assert response.status_code == 201

    product_id = response.get_json()['id']

    cart_item = {'product': {'id': product_id}, 'quantity': 2}
    client.post('/api/cart', json=cart_item)

    modify_response = client.put(f'/api/cart/{product_id}', json={'quantity': -3})
    assert modify_response.status_code == 400
    assert modify_response.get_json()['message'] == 'Quantity must be a positive integer'