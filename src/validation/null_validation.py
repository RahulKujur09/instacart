import sys
from pyspark.sql.functions import count, col, when
from src.exception import CustomException
from src.logger import logging

def get_null_counts(df):
    try:
        result = df.select([
            count(when(col(c).isNull(), c)).alias(c)
            for c in df.columns
        ])

        return result
    except Exception as e:
        raise CustomException(e, sys)
    
def get_duplicate_count(df):
    try:
        duplicate_count = (
            df.count() - df.dropDuplicates().count()
        )

        logging.info(f"Duplicate count: {duplicate_count}")

        return duplicate_count
    except Exception as e:
        raise CustomException(e, sys)