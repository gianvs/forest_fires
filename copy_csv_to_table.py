""" This file is used to copy the data from "amazon.csv" to a table in an online database. """

import pandas as pd
from sqlalchemy import create_engine


data = pd.read_csv('amazon.csv')
data.columns = [c.lower() for c in data.columns]
engine = create_engine('mysql+pymysql://WxVyhiGBXQ:RKAsHKo3zg@remotemysql.com:3306/WxVyhiGBXQ')
data.to_sql('amazon', con=engine)