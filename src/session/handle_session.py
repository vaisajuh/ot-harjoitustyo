class HandleSession:

    def __init__(self):
        self.session = []


    def add_session(self, user_id):
        self.session.append(user_id)


    def get_session(self):
        user_id = self.session[-1]
        return user_id
