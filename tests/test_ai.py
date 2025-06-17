import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_huggingface_integration(client):
    response = client.get('/api/ai/huggingface')  # Change this to your actual API route
    assert response.status_code == 200
    assert b"Success" in response.data  # Modify this according to your actual response

# Add more tests for AI-related endpoints (OpenAI, etc.)
