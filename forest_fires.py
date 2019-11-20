import pandas

forest_fire_data = pandas.read_csv('amazon.csv', encoding='latin_1')


# The following functions were implemented to improve code readability

def year(year):
    return forest_fire_data['year'] == year


def month(month):
    return forest_fire_data['month'] == month


def state(state):
    return forest_fire_data['state'] == state

