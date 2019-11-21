import psycopg2
from psycopg2 import sql
import pandas as pd

#This file is used to intervface with the public.amazon table

#Obtain a list of the states contained in the table
def get_states(cursor):
    cursor.execute(sql.SQL("select state from public.amazon"))
    states = pd.DataFrame(cursor.fetchall()).drop_duplicates().iloc[:,0]
    return states


def get_years(cursor):
    cursor.execute(sql.SQL("select years from public.amazon"))
    years = pd.DataFrame(cursor.fetchall()).drop_duplicates().iloc[:,0]
    return years

def get_plot_data(cursor,state):

# Creates a query based on state selected by user
    query = "SELECT {} FROM public.amazon WHERE state = %s;"
    columns = ("year", "number")
    state = [state] #this will be through user input
    cursor.execute(sql.SQL(query).format(sql.SQL(', ').join(map(sql.Identifier, columns))),state)
    data_aqcuired = pd.DataFrame(data = cursor.fetchall(),columns=columns)


# #Obtain a list of the years contained in the table
# cur.execute(sql.SQL("select year from public.amazon"))
# years = pd.DataFrame(self.cur.fetchall()).drop_duplicates().iloc[:,0]
#
#
# #Creates a query based on state selected by user
# query = "SELECT {} FROM public.amazon WHERE state = %s;"
# columns = ("year", "number")
# state = ['Acre'] #this will be through user input
# self.cur.execute(sql.SQL(query).format(sql.SQL(', ').join(map(sql.Identifier, columns))),state)
# data_aqcuired = pd.DataFrame(data = self.cur.fetchall(),columns=columns)
#
# #Calculates the number of forest fires by year
# forest_fires_by_year = []
# for i in years:
#     forest_fires_by_year.append(data_aqcuired['number'][data_aqcuired['year'] == i].sum())
#
# print(forest_fires_by_year)
#
#
#
