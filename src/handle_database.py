import sqlite3
from config import CONTACTS_DATABASE_PATH
import csv_reader
from store.handle_contacts import HandleContacts
from store.handle_users import HandleUsers


class Handle_database:

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
        print('-------')
    

if __name__ == "__main__":
    test = Handle_database()
    test.users.insert_user("udsaadsser", "1234")
    test.contacts.insert_contact("namedsa", "street", "x@x.com", "0123456789")
    test.contacts.get_contacts()
    test.users.get_users()
    test.clear_database()

