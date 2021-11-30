class HandleContacts:

    def __init__(self, database):
        self.database = database

    def get_contacts(self, user_id):
        get_contacts = self.database.execute('SELECT c.name, c.address, c.email, c.phonenumber '
        ' FROM Users u JOIN Contacts c on u.id = c.user_id WHERE u.id = ?', [user_id]).fetchall()
        return get_contacts

    def insert_contact(self,  user_id: int, name: str, address: str, email: str, phonenumber: str):
        name = name.lower()
        address = address.lower()
        email = email.lower()
        self.database.execute('INSERT INTO Contacts (user_id, name, address, email, phonenumber)'
        ' VALUES (?,?,?,?,?)', [user_id, name, address, email, phonenumber])
        self.database.commit()
