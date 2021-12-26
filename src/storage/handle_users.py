import hashlib

class HandleUsers:
    """Luokka hallinnoi tietokantaan kirjautuneita käyttäjiä
    Attributes:
    database: Tietokantayhteys
    """

    def __init__(self, database):
        """Luokan konstruktori"""

        self.database = database

    def _get_user(self, name: str):
        """Palauttaa parametrina annetun käyttäjän tiedot """

        get_user = self.database.execute(
            'SELECT id, name, password FROM Users WHERE name like ?', [name]).fetchall()
        return list(get_user[0])

    def insert_user(self, name: str, password: str):
        """Luo uuden käyttäjän tietokantaan"""

        name = name.lower()
        password = password.lower()
        password = self._create_hash(password)
        count = self.database.execute(
            'SELECT COUNT(*) FROM Users WHERE name LIKE ?', [name]).fetchone()[0]
        if count == 0:
            self.database.execute(
                'INSERT INTO Users (name, password) VALUES (?,?)', [name, password])
            self.database.commit()
            return True
        return False

    def validate_password(self, name: str, password: str):
        """Hakee käyttäjää tietokannasta ja jos löytyy, niin palauttaa käyttäjän id-numeron."""

        count = self.database.execute(
            'SELECT COUNT(*) FROM Users WHERE name LIKE ?', [name]).fetchone()[0]
        if count == 1:
            get_id = self._get_user(name)[0]
            get_password = self._get_user(name)[2]
            password = self._create_hash(password)
            if get_password == password:
                return int(get_id)
        return False

    def validate_length(self, name: str, password: str):
        """Tarkastaa käyttäjän syötteen pituuden oikeellisuuden"""

        if len(name) in range(3, 20) and len(password) in range(5, 20):
            return True
        return False

    def _create_hash(self, password: str):
        """Luo hajautusarvon salanan suojaamiseksi"""

        password = hashlib.sha3_512(password.encode())
        password = password.hexdigest()
        return password
