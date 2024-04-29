from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.mlproject.components.model_train import ModelTrainerConfig,ModelTrainer

import sys

if __name__=="__main__":
    logging.info("the exce started")


    try:
        #data_ingestion_config=DataingestionConfig
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        #        data_ingestion.initiate_data_ingestion()
       # data_ingestion=DataIngestion() 
        #train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)


        # model training
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        #model_trainer.initiate_model_trainer(train_arr,test_arr)


        
    except Exception as e:
        logging.info('custom excpetion')
        raise CustomException(e,sys)
