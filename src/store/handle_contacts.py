
class HandleContacts:

    def __init__(self, db):
        self.database = db
    

    def get_contacts(self):
        get_contacts = self.database.execute('SELECT name, address, email, phonenumber FROM Contacts').fetchall()
        for i in get_contacts:
            print(', '.join(i))
    

    def insert_contact(self, name: str, address: str, email: str, phonenumber: str):
        self.database.execute('INSERT INTO Contacts (name, address, email, phonenumber)'\
            'VALUES (?,?,?,?)', [name, address, email, phonenumber])
        self.database.commit()
