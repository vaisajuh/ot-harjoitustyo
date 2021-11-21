from ui.login import Login
from ui.functionality import Functionality
from ui.add_contact import AddContact

class UI:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.current_view = None

    def destroy_current_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None
    

    def start_login(self):
        self.destroy_current_view()
        self.current_view = Login(self.root, self.start_functionality, self.db)
        self.current_view.start_login()
    
    
    def start_functionality(self):
        self.destroy_current_view()
        self.current_view = Functionality(self.root, self.start_login, self.start_add_contact)
        self.current_view.start_functionality()
    

    def start_add_contact(self):
        self.destroy_current_view()
        self.current_view = AddContact(self.root, self.start_functionality)
        self.current_view.start_add_contact()
