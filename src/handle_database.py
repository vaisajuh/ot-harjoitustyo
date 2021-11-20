import sqlite3
from config import CONTACTS_DATABASE
import csv_reader


class Handle_database:

    def __init__(self):
        self.database = sqlite3.connect(CONTACTS_DATABASE)
        self.tables = csv_reader.get_database_tables()
        

    def initialize_database(self):
        try:
            for i in self.tables:
                self.database.execute(','.join(i))
        except:
            ""  

if __name__ == "__main__":
    jees = Handle_database()
    jees.initialize_database()