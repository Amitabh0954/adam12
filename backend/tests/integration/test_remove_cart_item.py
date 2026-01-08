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

def test_remove_from_cart(client):
    client.set_cookie('localhost', 'session', 'user-session-id')  # Mock user login session

    product = Product(name='Test Product', description='A product used for testing', price=10.99)
    response = client.post('/api/products', json=product.dict())
    assert response.status_code == 201

    product_id = response.get_json()['id']

    cart_item = {'product': {'id': product_id}, 'quantity': 2}
    client.post('/api/cart', json=cart_item)

    remove_response = client.delete(f'/api/cart/{product_id}')
    assert remove_response.status_code == 200
    assert remove_response.get_json()['message'] == 'Item removed successfully'
    assert len(remove_response.get_json()['cart']['items']) == 0

def test_remove_non_existent_item(client):
    client.set_cookie('localhost', 'session', 'user-session-id')  # Mock user login session

    response = client.delete('/api/cart/999')
    assert response.status_code == 404
    assert response.get_json()['message'] == 'Item not found in cart'