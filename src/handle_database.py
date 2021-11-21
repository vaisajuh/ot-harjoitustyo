import sqlite3
from config import CONTACTS_DATABASE_PATH
import csv_reader


class Handle_database:

    def __init__(self):
        self.database = sqlite3.connect(CONTACTS_DATABASE_PATH)
        self.tables = csv_reader.get_database_tables()
        

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
    

    def get_users(self):
        get_users = self.database.execute('SELECT name, password FROM Users').fetchall()
        for i in get_users:
            print(', '.join(i))
    

    def get_contacts(self):
        get_contacts = self.database.execute('SELECT name, address, email, phonenumber FROM Contacts').fetchall()
        for i in get_contacts:
            print(', '.join(i))
    

    def insert_user(self, name: str, password: str):
        self.database.execute('INSERT INTO Users (name, password) VALUES (?,?)', [name, password])


    def insert_contact(self, name: str, address: str, email: str, phonenumber: str):
        self.database.execute('INSERT INTO Contacts (name, address, email, phonenumber)'\
            'VALUES (?,?,?,?)', [name, address, email, phonenumber])

if __name__ == "__main__":
    test = Handle_database()
    test.initialize_database()
    test.insert_user("user", "1234")
    test.insert_contact("name", "street", "x@x.com", "0123456789")
    test.get_contacts()
    test.get_users()
    test.clear_database()
    test.insert_user("user", "1234")
    test.insert_contact("name", "street", "x@x.com", "0123456789")
    test.get_contacts()
    test.get_users()

