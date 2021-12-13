import sqlite3
from config import CONTACTS_DATABASE_PATH
from reader import csv_reader
from storage.handle_contacts import HandleContacts
from storage.handle_users import HandleUsers


class HandleDatabase:
    """Luokka, joka vastaa tietokantayhteydestä, sen alustamisesta ja
    tarvittaessa kaikkien tietojen poistamisesta

    Attributes:
    database: Yhteys tietokantaan
    tables: Tietokantaan lisättävät taulut
    users: Luokan users logiikka, joka saa parametrina tietokantayhteyden
    contacts: Luokan contacts logiikka, joka saa parametrina tietokantayhteyden
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa muuttujat"""

        self.database = sqlite3.connect(CONTACTS_DATABASE_PATH)
        self.tables = csv_reader.get_database_tables()
        self.users = HandleUsers(self.database)
        self.contacts = HandleContacts(self.database)
        self._initialize_database()

    def _initialize_database(self):
        """Lisää tietokantaan atribuutissa table olevat
        tietokantataulut"""

        for i in self.tables:
            self.database.execute(i[0])
        
        for i in self.tables:
            print(i[0])

    def _clear_database(self):
        """Poistaa kaiken tiedon tietokannan tauluista"""

        self.database.execute('DELETE FROM Users')
        self.database.execute('DELETE FROM Contacts')
        self.database.commit()
