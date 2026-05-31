import os, sys
import yaml

from constants.constant import CURRENT_ENV
from constants.path import CONFIG_DIR

from src.exception import CustomException
from src.logger import logging

def load_config():
    try:
        config_file = os.path.join(CONFIG_DIR, f"{CURRENT_ENV}.yaml")

        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        raise CustomException(e, sys)