class HandleContacts:
    """Luokan tehtävänä hoitaa yhteystietojen hallinnointi

   Attributes:
   database: Yhteys tietokantaan

    """
    def __init__(self, database):
        """Luokan konstruktori"""

        self.database = database

    def get_contacts(self, user_id):
        """Palauttaa kirjautuneena olevan käyttäjän kontaktit"""

        get_contacts = self.database.execute('SELECT c.name, c.address, c.email, c.phonenumber,'
        ' c.id FROM Users u JOIN Contacts c on u.id = c.user_id WHERE u.id = ?',
        [user_id]).fetchall()
        return get_contacts

    def insert_contact(self,  user_id: int, name: str, address: str, email: str, phonenumber: str):
        """Kirjautunut käyttäjä voi lisätä tällä yhteystietoja tietokantaan"""

        name = name.lower()
        address = address.lower()
        email = email.lower()
        self.database.execute('INSERT INTO Contacts (user_id, name, address, email, phonenumber)'
                              ' VALUES (?,?,?,?,?)', [user_id, name, address, email, phonenumber])
        self.database.commit()

    def delete_contact(self, row_id: int):
        """Toiminto yhteystiedon poistamiseen"""

        self.database.execute('DELETE FROM Contacts WHERE id = ?', [row_id])
        self.database.commit()
