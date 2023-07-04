import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from dataclasses import dataclass#it si used to create class variables

@dataclass# it is a decorator which help us to define the class variable in this class without using __init__ function
class DataIngestionConfig:#in my data ingestion component any input that is required will be given to this DataIngestionCongig(inputs like where we are going to save Training data or where I have to save raw data or test data)
    train_data_path: str = os.path.join('artifacts','train.csv')#it will save the training data in this particular path
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):#here we will read our data
        logging.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)
            
            logging.info('train test split initiated')
            
            train_set,test_set = train_test_split(df,test_size = 0.2,random_state = 42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            logging.info('ingestion of the data is compeleted')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=='__main__':
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
        





