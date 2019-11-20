import pandas as pd
###This file was used to copy the data from "amazon.csv" to a table in a local database

data = pd.read_csv('/home/gian/PycharmProjects/forest_fires/amazon.csv')
data.columns = [c.lower() for c in data.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://gian:teste@localhost:5432/gian')

data.to_sql('amazon', con=engine)