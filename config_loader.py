import yaml
import jsonschema
import os

INSTRUMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "instruments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "symbol": {"type": "string"},
                    "display_name": {"type": "string"},
                    "lot_size": {"type": "integer", "minimum": 1},
                    "instrument_token": {"type": ["string", "integer"]},
                    "enabled": {"type": "boolean"}
                },
                "required": ["symbol", "lot_size"]
            }
        }
    },
    "required": ["instruments"]
}

def load_instruments_config(config_path='config/instruments.yaml'):
    """
    Loads and validates the instruments configuration from a YAML file.

    Args:
        config_path (str): The path to the instruments YAML file.

    Returns:
        list: A list of instrument configurations if the file is valid.
        Returns None if the file is not found or invalid.
    """
    if not os.path.exists(config_path):
        return None

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

    try:
        jsonschema.validate(instance=config, schema=INSTRUMENT_SCHEMA)
        # Set default value for 'enabled' if not present
        for instrument in config.get('instruments', []):
            instrument.setdefault('enabled', True)
        return config['instruments']
    except jsonschema.exceptions.ValidationError as e:
        print(f"Invalid instruments configuration: {e.message}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during validation: {e}")
        return None