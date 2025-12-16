import pytest
from app import app  # Imports your Flask app

# 1. Create a "Test Client"
# This acts like a web browser but for code
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 2. Test the Home Page
def test_home_endpoint(client):
    """Test if the home page works and returns 200 OK"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Dairy Inventory System" in response.data or b"success" in response.data

# 3. Test the Inventory Page
def test_inventory_endpoint(client):
    """Test if the inventory list returns data"""
    response = client.get('/inventory')
    assert response.status_code == 200
    # Check if we get a list back
    assert isinstance(response.json, list)
