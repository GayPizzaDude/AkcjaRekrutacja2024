from db import DataBase
import os

if not os.path.exists('./InputFiles'):
    os.mkdir('./InputFiles')


db = DataBase()

db.initiate_data_base()
db.populate_meetings()
db.populate_candidates()
db.populate_recruiters()



## TO DO
## ZMIENIC DATAFRAME NA JSON - DONE
## ZEMINIC FORME ZAPISU - DONE
## PODMIENIC BAZE DANYCH NA JSON