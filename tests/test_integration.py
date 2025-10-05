import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_get_instruments_api(client, mocker):
    """Test the /api/instruments endpoint."""
    mock_instruments = [
        {
            'symbol': 'NSE:NIFTY25OCTFUT',
            'display_name': 'NIFTY OCT FUT',
            'lot_size': 75,
            'enabled': True
        }
    ]
    mocker.patch('app.ENABLED_INSTRUMENTS', mock_instruments)

    response = client.get('/api/instruments')
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, list)
    assert len(json_data) == 1
    assert json_data[0]['symbol'] == 'NSE:NIFTY25OCTFUT'
    assert json_data[0]['lot_size'] == 75

def test_dashboard_redirect(client):
    """Test that the dashboard redirects to login if not authenticated."""
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'Connect to Fyers' in response.data