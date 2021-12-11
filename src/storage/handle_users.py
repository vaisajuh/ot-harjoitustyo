
class HandleUsers:
    """Luokka hallinnoi tietokantaan kirjautuneita käyttäjiä 
    Attributes:
    database: Tietokantayhteys
    """

    def __init__(self, database):
        """Luokan konstruktori"""

        self.database = database

    def get_user(self, name: str):
        """Palauttaa parametrina annetun käyttäjän id-numeron """
        get_user = self.database.execute(
            'SELECT id, name, password FROM Users WHERE name like ?', [name]).fetchall()
        return list(get_user[0])

    def insert_user(self, name: str, password: str):
        """Luo uuden käyttäjän tietokantaan"""

        name = name.lower()
        password = password.lower()
        self.database.execute(
            'INSERT INTO Users (name, password) VALUES (?,?)', [name, password])
        self.database.commit()

    def validate_password(self, name: str, password: str):
        """Hakee käyttäjää tietokannasta ja jos löytyy, niin tarkastaa 
        salasanan oikeellisuuden. Jos käyttäjää ei löydy tietokannasta, niin 
        se lisätään sinne"""

        count = self.database.execute(
            'SELECT COUNT(*) FROM Users WHERE name LIKE ?', [name]).fetchone()[0]
        get_id = ""
        if int(count) == 1:
            get_id = self.get_user(name)[0]
            get_password = self.get_user(name)[2]
            if str(get_password) == password:
                return int(get_id)
            return False
        self.insert_user(name, password)
        get_id = self.get_user(name)[0]
        return int(get_id)
