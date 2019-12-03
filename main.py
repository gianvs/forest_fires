import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlalchemy
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import sessionmaker

# defining functions used to acquire data from the SQL table (previously contained in 'amazon_table.py' file and implemented with psycopg2), and to plot graph.

def get_states(table,engine):
    return pd.read_sql(sqlalchemy.select([table.columns.state]),engine).drop_duplicates().iloc[:,0]

def get_years(table,engine):
    return pd.read_sql(sqlalchemy.select([table.columns.year]),engine).drop_duplicates().iloc[:,0]

def get_plot_data(table,engine,state):
    return pd.read_sql(sqlalchemy.select([table.columns.year,table.columns.number]).where(table.columns.state == state),engine)

def plot_bar_graph(x_data, y_data, x_label, y_label, title):
    # this is for plotting purpose
    index = np.arange(len(x_data))
    plt.bar(index, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(index, x_data, rotation=30)
    plt.title(title)
    plt.show()


engine = sqlalchemy.create_engine('mysql+pymysql://WxVyhiGBXQ:RKAsHKo3zg@remotemysql.com:3306/WxVyhiGBXQ')
Session = sessionmaker(bind = engine)
session = Session()
meta = MetaData()
amazon = Table('amazon', meta, autoload=True, autoload_with=engine)

states = get_states(amazon,engine).tolist()
years = get_years(amazon,engine).tolist()


while True:
    for i in range(len(states)):
        print(str(i + 1) + ' ' + states[i] + '\t\t', end=" ")
        if (i + 1) % 4 == 0:
            print('')

    try:
        user_input = int(input('\nType the number of the desired state or type 0 to quit: '))
    except ValueError:
        print("This is not a whole number.")
        break;

    if (user_input >= 1) and (user_input <= len(states)):
        data_acquired = data = get_plot_data(amazon,engine,states[user_input])

        # Calculates the number of forest fires by year
        forest_fires_by_year = []
        for i in data_acquired['year'].drop_duplicates():
            forest_fires_by_year.append(data_acquired['number'][data_acquired['year'] == i].sum())
        plot_bar_graph(data_acquired['year'].drop_duplicates(), forest_fires_by_year, 'Year', 'Number of Fires', 'Amazon Fires in '+ states[user_input - 1])
    elif user_input == 0:
        break
    else:
        print('Invalid entry!')
