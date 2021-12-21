class HandleContacts:
    """Luokan tehtävänä hoitaa yhteystietojen hallinnointi

   Attributes:
   database: Yhteys tietokantaan

    """
    def __init__(self, database):
        """Luokan konstruktori"""

        self.database = database

    def get_contacts(self, user_id: int, name:str, address: str, email: str, phone_number: str):
        """Palauttaa kirjautuneena olevan käyttäjän kontaktit"""

        name = "%" + name + "%"
        address = "%" + address + "%"
        email = "%" + email + "%"
        phone_number = "%" + phone_number + "%"
        get_contacts = self.database.execute('SELECT c.name, c.address, c.email, c.phonenumber,'
        ' c.id FROM Users u JOIN Contacts c on u.id = c.user_id WHERE u.id = ? AND (c.name LIKE'
        ' ? OR c.address LIKE ? OR c.email LIKE ? OR c.phonenumber LIKE ?) GROUP BY c.name',
        [user_id, name, address, email, phone_number]).fetchall()
        return get_contacts

    def insert_contact(self,  user_id: int, name: str, address: str, email: str, phone_number: str):
        """Kirjautunut käyttäjä voi lisätä tällä yhteystietoja tietokantaan"""

        name = name.lower()
        address = address.lower()
        email = email.lower()
        self.database.execute('INSERT INTO Contacts (user_id, name, address, email, phonenumber)'
                              ' VALUES (?,?,?,?,?)', [user_id, name, address, email, phone_number])
        self.database.commit()

    def delete_contact(self, row_id: int):
        """Toiminto yhteystiedon poistamiseen"""

        self.database.execute('DELETE FROM Contacts WHERE id = ?', [row_id])
        self.database.commit()

    def get_row(self, row_id: int):
        """Toiminto palauttaa yhteystiedon käyttöliittymään käyttäjän muokattavaksi"""

        get_row = self.database.execute('SELECT c.name, c.address, c.email, c.phonenumber,'
        ' c.id FROM Users u JOIN Contacts c on u.id = c.user_id WHERE c.id = ?',
        [row_id]).fetchone()
        return get_row

    def update_row(self, row_id: int, name: str, address: str, email: str, phone_number: str):
        """Toiminto yhteystiedon päivittämiseen"""

        self.database.execute('UPDATE Contacts SET name = ?, address = ?, email = ?,'
        ' phonenumber = ? WHERE id = ?',[name, address, email, phone_number, row_id])
        self.database.commit()
    
    def validate_name(self, name: str):
        """Tarkastaa käyttäjän syöttämän nimen pituuden oikeellisuuden"""
        if len(name) in range(3,20):
            return True
    
    def validate_address(self, address: str):
        """Tarkastaa käyttäjän syöttämän osoitteen pituuden oikeellisuuden"""
        if len(address) in range(10, 40):
            return True
    
    def validate_email(self, email: str):
        """Tarkastaa käyttäjän syöttämän sähköpostiosoitteen pituuden oikeellisuuden"""
        if len(email) in range(10,40):
            first_letter = email[0]
            last_letter = email[-1]
            if '@' and "." in email\
                and first_letter != "@" and last_letter != ".":
                return True
    
    def validate_phone_number(self, phone_number: str):
        """Tarkastaa käyttäjän syöttämän puhelinnumeron pituuden oikeellisuuden"""
        if len(phone_number) in range(10,40) and\
             phone_number.isdecimal():
             return True
    