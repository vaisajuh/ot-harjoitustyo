import sqlite3
from config import CONTACTS_DATABASE_PATH
import csv_reader
from store.handle_contacts import HandleContacts
from store.handle_users import HandleUsers


class HandleDatabase:

    def __init__(self):
        self.database = sqlite3.connect(CONTACTS_DATABASE_PATH)
        self.tables = csv_reader.get_database_tables()
        self.users = HandleUsers(self.database)
        self.contacts = HandleContacts(self.database)

        self.initialize_database()

    def initialize_database(self):
        try:
            for i in self.tables:
                self.database.execute(''.join(i))
        except:
            ""

    def clear_database(self):
        self.database.execute('DELETE FROM Users')
        self.database.execute('DELETE FROM Contacts')
        self.database.commit()
        print('-------')
