import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

import pandas as pd
import pymysql








from dotenv import load_dotenv

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')





def read_sql_data():

    logging.info("reading MYSQL DB")

    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        #logging.info("connection established",mydb)
        logging.info("connection established %s", mydb)


        df=pd.read_sql_query('select * from students',mydb)

        print(df.head())

        return df
        #pass
    except Exception as ex:
        raise CustomException(ex)
