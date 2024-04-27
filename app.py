from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_transformation import DataTransformationConfig




if __name__=="__main__":
    logging.info("the exce started")


    try:
        #data_ingestion_config=DataingestionConfig
        data_ingestion=DataIngestion()
        train_path_data,test_path_data=data_ingestion.initiate_data_ingestion()
        #        data_ingestion.initiate_data_ingestion()
       # data_ingestion=DataIngestion() 
        #train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_path_data,test_path_data)


        
    except Exception as e:
        logging.info('custom excpetion')
        raise CustomException(e,sys)
