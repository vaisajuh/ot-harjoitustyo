import csv
from config import DATABASE_TABLES_PATH

"""Moduuli, jonka tehtävänä lukea tietokantaulut csv-tiedosta ja luoda niistä
palautettava lista"""

database_file = []

def init_file():
    with open(DATABASE_TABLES_PATH, encoding='utf-8') as tables:
        for row in csv.reader(tables, delimiter=";"):
            database_file.append(row)


def get_database_tables():
    init_file()
    return database_file
