import amazon_table
import psycopg2
from psycopg2 import sql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_bar_graph(x_data, y_data, x_label, y_label, title):
    # this is for plotting purpose
    index = np.arange(len(x_data))
    plt.bar(index, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(index, x_data, rotation=30)
    plt.title(title)
    plt.show()


connection = psycopg2.connect(dbname='gian', user='gian', password='teste', host='localhost', port='5432')
cursor = connection.cursor()

states = amazon_table.get_states(cursor).tolist()
while (True):
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
        cursor.execute(sql.SQL("select year from public.amazon"))
        years = pd.DataFrame(cursor.fetchall()).drop_duplicates().iloc[:, 0]
        query = "SELECT {} FROM public.amazon WHERE state = %s;"
        columns = ("year", "number")
        state = [states[user_input - 1]]
        cursor.execute(sql.SQL(query).format(sql.SQL(', ').join(map(sql.Identifier, columns))), state)
        data_acquired = pd.DataFrame(data=cursor.fetchall(), columns=columns)
        print(type(years))
        print(type(data_acquired['year']))
        # Calculates the number of forest fires by year
        forest_fires_by_year = []
        for i in data_acquired['year'].drop_duplicates():
            forest_fires_by_year.append(data_acquired['number'][data_acquired['year'] == i].sum())
        plot_bar_graph(data_acquired['year'].drop_duplicates(), forest_fires_by_year, 'Year', 'Number of Fires', 'Amazon Fires in '+ states[user_input - 1])
    elif user_input == 0:
        break
    else:
        print('Invalid entry!')
