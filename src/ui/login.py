from tkinter import ttk
from tkinter.messagebox import showwarning


class Login:
    def __init__(self, root, functionality, db, session, user):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self.user = user
        self._login = None
        self._username_entry = None
        self._password_entry = None

    def destroy(self):
        self._login.destroy()

    def _validate_login(self):
        if len(self._username_entry.get()) in range(3, 20) and\
                len(self._password_entry.get()) in range(3, 20):
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
                message="Salasana on väärä tai käyttäjää ei ole tietokannassa!"
            )
        else:
            self.session.add_session(validate)
            self.functionality()

    def start_login(self):
        self.root.title("Kirjaudu")

        self._login = ttk.Frame(master=self.root)
        self._login.pack(padx=10, pady=10, fill='x', expand=True)

        username_label = ttk.Label(master=self._login, text="Käyttäjänimi")
        username_label.pack(fill='x', expand=True)

        self._username_entry = ttk.Entry(master=self._login)
        self._username_entry.pack(fill='x', expand=True)

        password_label = ttk.Label(master=self._login, text="Salasana")
        password_label.pack(fill='x', expand=True)

        self._password_entry = ttk.Entry(master=self._login, show="*")
        self._password_entry.pack(fill='x', expand=True)

        login_button = ttk.Button(
            master=self._login, text="Kirjaudu", command=self._validate_login)
        login_button.pack(fill='x', expand=True, pady=10)

        add_user_button = ttk.Button(
            master=self._login, text="Lisää käyttäjä", command=self.user)
        add_user_button.pack(fill='x', expand=True, pady=10)
