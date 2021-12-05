
class HandleUsers:

    def __init__(self, database):
        self.database = database

    def get_users(self):
        users = []
        get_users = self.database.execute(
            'SELECT name, password FROM Users').fetchall()
        for i in get_users:
            users.append(i[0] + ", " + i[1])
        return users

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
            get_id = self.database.execute(
                'SELECT Users.id FROM Users WHERE name LIKE ?', [name]).fetchone()[0]
            get_pass = self.database.execute(
                'SELECT password FROM Users WHERE name LIKE ?', [name]).fetchone()[0]
            if str(get_pass) == password:
                return int(get_id)
            return False
        self.insert_user(name, password)
        get_id = self.database.execute(
            'SELECT Users.id FROM Users WHERE name LIKE ?', [name]).fetchone()[0]
        return int(get_id)
