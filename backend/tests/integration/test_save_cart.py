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

def test_save_and_load_cart(client):
    client.set_cookie('localhost', 'session', 'user-session-id')  # Mock user login session

    product = Product(name='Test Product', description='A product used for testing', price=10.99)
    response = client.post('/api/products', json=product.dict())
    assert response.status_code == 201

    product_id = response.get_json()['id']

    cart_item = {'product': {'id': product_id}, 'quantity': 2}
    client.post('/api/cart', json=cart_item)

    save_response = client.post('/api/cart/save')
    assert save_response.status_code == 200
    assert save_response.get_json()['message'] == 'Cart saved successfully'

    load_response = client.get('/api/cart/load')
    assert load_response.status_code == 200
    assert len(load_response.get_json()['items']) == 1
    assert load_response.get_json()['items'][0]['quantity'] == 2

def test_save_cart_without_login(client):
    save_response = client.post('/api/cart/save')
    assert save_response.status_code == 401
    assert save_response.get_json()['message'] == 'User must be logged in'

def test_load_cart_without_login(client):
    load_response = client.get('/api/cart/load')
    assert load_response.status_code == 401
    assert load_response.get_json()['message'] == 'User must be logged in'