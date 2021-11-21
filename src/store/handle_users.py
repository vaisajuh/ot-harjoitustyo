
class HandleUsers:

    def __init__(self, db):
        self.database = db
    

    def get_users(self):
        get_users = self.database.execute('SELECT name, password FROM Users').fetchall()
        for i in get_users:
            print(', '.join(i))
    

    def insert_user(self, name: str, password: str):
        self.database.execute('INSERT INTO Users (name, password) VALUES (?,?)', [name, password])
        self.database.commit()
  