from tkinter import ttk

class Functionality:
    def __init__(self, root, login):
        self.root = root
        self.login = login
        self.functionality = None

    
    def destroy(self):
        self.login.destroy()
        

    def start_functionality(self):

        self.functionality = ttk.Frame(master=self.root)
        self.functionality.pack(padx=10, pady=10, fill='x', expand=True)

        get_button = ttk.Button(master=self.functionality, text="Hae yhteystiedot", command="")
        get_button.pack(fill='x', expand=True, pady=10)

        add_button = ttk.Button(master=self.functionality, text="Lisää yhteystieto", command="")
        add_button.pack(fill='x', expand=True, pady=10)

        logout_button = ttk.Button(master=self.functionality, text="Kirjaudu ulos", command=self.login)
        logout_button.pack(fill='x', expand=True, pady=10)