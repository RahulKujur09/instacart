import os, sys
from src.exception import CustomException
from src.logger import logging

def validate_columns(df, expected_columns):
    try:
        actual_column = set(df.columns)
        expected_column = set(expected_columns)

        missing_columns = expected_column - actual_column
        extra_columns = actual_column - expected_column

        if missing_columns:
            raise ValueError(
                f"Missing columns: {missing_columns}"
            )
        
        if extra_columns:
            raise ValueError(
                f"Extra columns found: {extra_columns}"
            )
        
        logging.info(f"Schema Validation passed")
        
        return True
    except Exception as e:
        raise CustomException(e, sys)