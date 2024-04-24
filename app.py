from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException



if __name__=="__main__":
    logging.info("the exce started")


    try:
        a=1/0
    except Exception as e:
        logging.info('custom excpetion ')
        raise CustomException(e,sys)
