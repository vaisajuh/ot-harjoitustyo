class HandleSession:

    def __init__(self):
        self.session = []
    

    def add_session(self, username):
        self.session.append(username)
    

    def get_session(self):
        id = len(self.session) - 1
        return id