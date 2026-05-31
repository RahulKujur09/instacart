import os, sys
from src.logger import logging
from src.exception import CustomException


if __name__ == "__main__":
    try:
        a = 1/0
        logging.info("operation completed")
    except Exception as e:
        error = CustomException(e, sys)
        logging.error(error)
        raise CustomException(e, sys)