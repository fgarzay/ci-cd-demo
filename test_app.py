import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test home page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'CI/CD' in response.data

def test_health(client):
    """Test health endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'

def test_test_endpoint(client):
    """Test test endpoint"""
    response = client.get('/api/test')
    assert response.status_code == 200
    data = response.get_json()
    assert data['test'] == 'passed'
