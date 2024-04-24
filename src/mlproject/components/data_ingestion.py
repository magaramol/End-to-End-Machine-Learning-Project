import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

import pandas as pd
#import

from dataclasses import dataclass

@dataclass

class DataingestionConfig:
    train_data_path:str=os.path.joins('artifacts','train.csv')
    test_data_path:str=os.path.joins('artifacts','test.csv')
    raw_data_path:str=os.path.joins('artifacts','raw.csv')    