from ui.login import Login

class UI:
    def __init__(self, root):
        self.root = root


    def start(self):
        login = Login(self.root)
        login.login_start()
