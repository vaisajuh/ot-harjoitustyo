
class HandleUsers:

    def __init__(self, database):
        self.database = database

    def get_user(self, name: str):
        get_user = self.database.execute(
            'SELECT id, name, password FROM Users WHERE name like ?', [name]).fetchall()
        return list(get_user[0])

    def insert_user(self, name: str, password: str):
        name = name.lower()
        password = password.lower()
        self.database.execute(
            'INSERT INTO Users (name, password) VALUES (?,?)', [name, password])
        self.database.commit()

    def validate_password(self, name: str, password: str):
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
