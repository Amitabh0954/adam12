import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_add_category(client):
    response = client.post('/api/categories', json={
        'name': 'Electronics'
    })
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Category added successfully'

def test_add_duplicate_category(client):
    client.post('/api/categories', json={
        'name': 'Electronics'
    })

    response = client.post('/api/categories', json={
        'name': 'Electronics'
    })
    assert response.status_code == 400

def test_get_all_categories(client):
    client.post('/api/categories', json={'name': 'Electronics'})
    client.post('/api/categories', json={'name': 'Home Appliances'})

    response = client.get('/api/categories')
    assert response.status_code == 200
    categories = response.get_json()
    assert len(categories) >= 2