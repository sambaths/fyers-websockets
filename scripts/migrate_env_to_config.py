import os
import yaml
from dotenv import load_dotenv

def migrate_env_to_config():
    """
    Migrates the instrument configuration from .env to config/instruments.yaml.
    """
    load_dotenv()

    symbol = os.getenv('SYMBOL')
    lot_size_str = os.getenv('LOT_SIZE')

    if not symbol or not lot_size_str:
        print("Error: SYMBOL or LOT_SIZE not found in .env file.")
        return

    try:
        lot_size = int(lot_size_str)
    except ValueError:
        print(f"Error: Invalid LOT_SIZE '{lot_size_str}' in .env file. Must be an integer.")
        return

    config_dir = 'config'
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    config_data = {
        'instruments': [
            {
                'symbol': symbol,
                'display_name': symbol,
                'lot_size': lot_size,
                'enabled': True
            }
        ]
    }

    config_path = os.path.join(config_dir, 'instruments.yaml')
    with open(config_path, 'w') as f:
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)

    print(f"Successfully migrated .env configuration to {config_path}")

if __name__ == "__main__":
    migrate_env_to_config()