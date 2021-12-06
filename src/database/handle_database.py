import sqlite3
from config import CONTACTS_DATABASE_PATH
from reader import csv_reader
from storage.handle_contacts import HandleContacts
from storage.handle_users import HandleUsers


class HandleDatabase:

    def __init__(self):
        self.database = sqlite3.connect(CONTACTS_DATABASE_PATH)
        self.tables = csv_reader.get_database_tables()
        self.users = HandleUsers(self.database)
        self.contacts = HandleContacts(self.database)
        self.initialize_database()

    def initialize_database(self):
        for i in self.tables:
            self.database.execute(''.join(i))

    def clear_database(self):
        self.database.execute('DELETE FROM Users')
        self.database.execute('DELETE FROM Contacts')
        self.database.commit()
