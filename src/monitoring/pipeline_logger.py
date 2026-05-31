import os,sys
from datetime import datetime

from src.logger import logging
from src.exception import CustomException

class PipelineLogger:
    @staticmethod
    def log_start(job_name):
        try:
            logging.info(f"PIPELINE STARTED | {job_name} | {datetime.now().strftime('%Y-%m-%d %H-%M-%S')}")
        except Exception as e:
            raise CustomException(e, sys)
        
    @staticmethod
    def log_end(job_name):
        try:
            logging.info(
                f"PIPELINE COMPLETED | {job_name} | {datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"
            )
        except Exception as e:
            raise CustomException(e, sys)
        
    @staticmethod
    def log_failure(job_name, error):
        try:
            logging.error(
                f"PIPELINE FAILED | {job_name} | ERROR: {error} | "
                f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"
            )
        except Exception as e:
            raise CustomException(e, sys)