from tkinter import ttk

class Login:
    def __init__(self, root):
        self.root = root
        self.login = None
        self.username_entry = None
        self.password_entry = None

    
    def login_start(self):

        self.login = ttk.Frame(master=self.root)
        self.login.pack(padx=10, pady=10, fill='x', expand=True)


        self.username_label = ttk.Label(master=self.login, text="Käyttäjänimi")
        self.username_label.pack(fill='x', expand=True)

        self.username_entry = ttk.Entry(master=self.login)
        self.username_entry.pack(fill='x', expand=True)

        password_label = ttk.Label(master=self.login, text="Salasana")
        password_label.pack(fill='x', expand=True)

        self.password_entry = ttk.Entry(master=self.login, show="*")
        self.password_entry.pack(fill='x', expand=True)

        signin_button = ttk.Button(master=self.login, text="Kirjaudu", command="")
        signin_button.pack(fill='x', expand=True, pady=10)
    