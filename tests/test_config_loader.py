import os
import yaml
import pytest
from config_loader import load_instruments_config

@pytest.fixture
def valid_config_file(tmp_path):
    config_data = {
        'instruments': [
            {
                'symbol': 'NSE:NIFTY25OCTFUT',
                'display_name': 'NIFTY OCT FUT',
                'lot_size': 75,
                'enabled': True
            },
            {
                'symbol': 'NSE:BANKNIFTY25OCTFUT',
                'display_name': 'BANKNIFTY OCT FUT',
                'lot_size': 35,
                'enabled': False
            }
        ]
    }
    config_path = tmp_path / "instruments.yaml"
    with open(config_path, 'w') as f:
        yaml.dump(config_data, f)
    return str(config_path)

@pytest.fixture
def invalid_config_file(tmp_path):
    config_data = {
        'instruments': [
            {
                'symbol': 'NSE:NIFTY25OCTFUT',
                'display_name': 'NIFTY OCT FUT'
                # Missing lot_size
            }
        ]
    }
    config_path = tmp_path / "invalid_instruments.yaml"
    with open(config_path, 'w') as f:
        yaml.dump(config_data, f)
    return str(config_path)

def test_load_valid_config(valid_config_file):
    """Test loading a valid configuration file."""
    config = load_instruments_config(valid_config_file)
    assert config is not None
    assert len(config) == 2
    assert config[0]['symbol'] == 'NSE:NIFTY25OCTFUT'
    assert config[1]['enabled'] is False

def test_load_invalid_config(invalid_config_file):
    """Test loading an invalid configuration file."""
    config = load_instruments_config(invalid_config_file)
    assert config is None

def test_load_nonexistent_config():
    """Test loading a nonexistent configuration file."""
    config = load_instruments_config("nonexistent.yaml")
    assert config is None

def test_default_enabled_value(tmp_path):
    """Test that the 'enabled' field defaults to True if not provided."""
    config_data = {
        'instruments': [
            {
                'symbol': 'NSE:NIFTY25OCTFUT',
                'lot_size': 50
            }
        ]
    }
    config_path = tmp_path / "default_enabled.yaml"
    with open(config_path, 'w') as f:
        yaml.dump(config_data, f)

    config = load_instruments_config(str(config_path))
    assert config is not None
    assert len(config) == 1
    assert config[0]['enabled'] is True