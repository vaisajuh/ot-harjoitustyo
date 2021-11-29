from tkinter import ttk
from tkinter.messagebox import showwarning


class Login:
    def __init__(self, root, functionality, db, session):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self.login = None
        self.username_entry = None
        self.password_entry = None

    def destroy(self):
        self.login.destroy()

    def validate_login(self):
        if len(self.username_entry.get()) >= 4 and len(self.username_entry.get()) <= 20 and \
                len(self.password_entry.get()) >= 4 and len(self.password_entry.get()) <= 20:
            self.validate_password()

        else:
            showwarning(
                title="Tiedoksi",
                message="Käyttäjänimen ja salasanan tulee olla neljän ja "
                "kahdenkymmenen merkin väliltä"
            )

    def validate_password(self):
        validate = self.db.users.validate_password(
            self.username_entry.get(), self.password_entry.get())
        if validate == False:
            showwarning(
                title="Tiedoksi",
                message="Väärä salasana!"
            )
        else:
            self.session.add_session(validate)
            self.functionality()

    def start_login(self):

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

        login_button = ttk.Button(
            master=self.login, text="Kirjaudu", command=self.validate_login)
        login_button.pack(fill='x', expand=True, pady=10)
