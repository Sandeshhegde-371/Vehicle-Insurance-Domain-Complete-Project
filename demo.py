'''#Below code is to check logging coniguration
from src.logger import logging

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")'''


'''#Below code is to check the exception configuration
from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e  # Raising custom exception with detailed error information
'''

from src.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()