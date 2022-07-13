import logging.config
import os

import yaml

import definitions


def create_tmp_dir() -> None:
    tmp_dir_path = f'{definitions.ROOT_DIR}/tmp'
    os.makedirs(tmp_dir_path, exist_ok=True)


def setup_config(config_path: str = 'configs/config.yaml') -> dict:
    config = None
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            try:
                config = yaml.safe_load(f)
                logging_section = config['logging']
                log_name = f"{definitions.ROOT_DIR}/{logging_section['handlers']['file_handler']['filename']}"
                logging_section['handlers']['file_handler']['filename'] = log_name
                create_tmp_dir()
                logging.config.dictConfig(logging_section)
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=logging.INFO)
    else:
        print(f'Could not find config by specified path - {config_path}')

    return config
