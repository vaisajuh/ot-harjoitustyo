from tkinter import ttk
from tkinter.messagebox import showwarning


class Login:
    def __init__(self, root, functionality, db, session):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self._login = None
        self._username_entry = None
        self._password_entry = None

    def destroy(self):
        self._login.destroy()

    def _validate_login(self):
        if len(self._username_entry.get()) in range(4, 20) and\
                len(self._password_entry.get()) in range(4, 20):
            self._validate_password()

        else:
            showwarning(
                title="Tiedoksi",
                message="Käyttäjänimen ja salasanan tulee olla neljän ja "
                "kahdenkymmenen merkin väliltä"
            )

    def _validate_password(self):
        validate = self.db.users.validate_password(
            self._username_entry.get(), self._password_entry.get())
        if validate == False:
            showwarning(
                title="Tiedoksi",
                message="Väärä salasana!"
            )
        else:
            self.session.add_session(validate)
            self.functionality()

    def start_login(self):

        self._login = ttk.Frame(master=self.root)
        self._login.pack(padx=10, pady=10, fill='x', expand=True)

        self._username_label = ttk.Label(master=self._login, text="Käyttäjänimi")
        self._username_label.pack(fill='x', expand=True)

        self._username_entry = ttk.Entry(master=self._login)
        self._username_entry.pack(fill='x', expand=True)

        self._password_label = ttk.Label(master=self._login, text="Salasana")
        self._password_label.pack(fill='x', expand=True)

        self._password_entry = ttk.Entry(master=self._login, show="*")
        self._password_entry.pack(fill='x', expand=True)

        login_button = ttk.Button(
            master=self._login, text="Kirjaudu", command=self._validate_login)
        login_button.pack(fill='x', expand=True, pady=10)
