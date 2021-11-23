
class HandleUsers:

    def __init__(self, db):
        self.database = db
    

    def get_users(self):
        list = []
        get_users = self.database.execute('SELECT name, password FROM Users').fetchall()
        for i in get_users:
            list.append(i[0] + ", " + i[1])
        return list

    def insert_user(self, name: str, password: str):
        try:
            self.database.execute('INSERT INTO Users (name, password) VALUES (?,?)', [name, password])
            self.database.commit()
        except:
            ""

  