import csv
from config import DATABASE_TABLES_PATH

database_file = []
def init_file():
    with open(DATABASE_TABLES_PATH) as tables:
        for row in csv.reader(tables, delimiter=";"):
            database_file.append(row)


def get_database_tables():
    init_file()
    return database_file