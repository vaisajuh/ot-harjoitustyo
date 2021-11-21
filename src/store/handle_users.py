
class HandleUsers:

    def __init__(self, db):
        self.database = db
    

    def get_users(self):
        get_users = self.database.execute('SELECT name, password FROM Users').fetchall()

        return get_users

    def insert_user(self, name: str, password: str):
        self.database.execute('INSERT INTO Users (name, password) VALUES (?,?)', [name, password])
        self.database.commit()
    

  