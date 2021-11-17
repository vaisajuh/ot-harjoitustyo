from ui.login import Login
from ui.functionality import Functionality

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def destroy_current_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None
    

    def start_login(self):
        self.destroy_current_view()
        self.current_view = Login(self.root, self.start_functionality)
        self.current_view.start_login()
    
    
    def start_functionality(self):
        self.destroy_current_view()
        self.current_view = Functionality(self.root, self.start_login)
        self.current_view.start_functionality()
