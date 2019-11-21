import psycopg2
from psycopg2 import sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Connects to the database and creates a cursor to execute SQL queries
conn = psycopg2.connect(dbname='gian', user='gian', password='teste', host='localhost', port='5432')
cur = conn.cursor()

# Obtain a list of the states contained in the table
cur.execute(sql.SQL("select state from public.amazon"))
states = pd.DataFrame(cur.fetchall()).drop_duplicates().iloc[:, 0]

# Obtain a list of the years contained in the table
cur.execute(sql.SQL("select year from public.amazon"))
years = pd.DataFrame(cur.fetchall()).drop_duplicates().iloc[:, 0]

# Creates a query based on state selected by user
query = "SELECT {} FROM public.amazon WHERE state = %s;"
columns = ("year", "number")
state = ['Acre']  # this will be through user input
cur.execute(sql.SQL(query).format(sql.SQL(', ').join(map(sql.Identifier, columns))), state)
data_aqcuired = pd.DataFrame(data=cur.fetchall(), columns=columns)

# Calculates the number of forest fires by year
forest_fires_by_year = []
for i in years:
    forest_fires_by_year.append(data_aqcuired['number'][data_aqcuired['year'] == i].sum())


def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(forest_fires_by_year))
    plt.bar(index, forest_fires_by_year)
    plt.xlabel('Year')
    plt.ylabel('Fires')
    plt.xticks(index, years, fontsize=5, rotation=30)
    plt.title('Forest fires in state')
    plt.show()


plot_bar_x()
