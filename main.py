from db import DataBase
import os

if not os.path.exists('./InputFiles'):
    os.mkdir('./InputFiles')


db = DataBase()

db.initiate_data_base()
