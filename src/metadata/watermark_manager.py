import json
import os, sys
from datetime import datetime

from constants.path import WATERMARK_FILE
from src.exception import CustomException
from src.logger import logging

def get_watermark():
    try:
        try:
            with open(WATERMARK_FILE, "a") as f:
                return json.load(f)
        except FileNotFoundError:
            return None
    except Exception as e:
        raise CustomException(e, sys)
    
def update_watermark(file_name):
    try:
        watermark = {
            "last_processed_file" : file_name,
            "processed_time": datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        }

        with open(WATERMARK_FILE, "w") as f:
            json.dump(watermark, f, indent=4)

        logging.info(f"Watermark updated: {file_name}")
    except Exception as e:
        raise CustomException(e, sys)