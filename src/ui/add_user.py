from tkinter import ttk
from tkinter.constants import S
from tkinter.messagebox import showwarning, showinfo


class AddUser:
    def __init__(self, root, login, db):
        self.root = root
        self.db = db
        self.login = login
        self._insert_user = None
        self._username_entry = None
        self._password_entry = None

    def destroy(self):
        self._insert_user.destroy()

    def _add_user(self):
        if len(self._username_entry.get()) in range(3, 20) and\
                len(self._password_entry.get()) in range(3, 20):
            exists = self.db.users.insert_user(self._username_entry.get(), self._password_entry.get())
            if exists is True:
                showinfo(
                title="Tiedoksi",
                message="Käyttäjä lisätty tietokantaan!"
                )
            else:
                showwarning(
                title="Tiedoksi",
                message="Käyttäjä on jo ennestään tietokannassa"
                ) 
        else:
            showwarning(
                title="Tiedoksi",
                message="Käyttäjänimen ja salasanan tulee olla neljän ja "
                "kahdenkymmenen merkin väliltä"
            )

    def start_add_user(self):
        self.root.title("Lisää käyttäjä")

        self._insert_user = ttk.Frame(master=self.root)
        self._insert_user.pack(padx=10, pady=10, fill='x', expand=True)

        username_label = ttk.Label(master=self._insert_user, text="Käyttäjänimi")
        username_label.pack(fill='x', expand=True)

        self._username_entry = ttk.Entry(master=self._insert_user)
        self._username_entry.pack(fill='x', expand=True)

        password_label = ttk.Label(master=self._insert_user, text="Salasana")
        password_label.pack(fill='x', expand=True)

        self._password_entry = ttk.Entry(master=self._insert_user)
        self._password_entry.pack(fill='x', expand=True)

        add_button = ttk.Button(
            master=self._insert_user, text="Lisää käyttäjä", command=self._add_user)
        add_button.pack(fill='x', expand=True, pady=10)

        reverse_button = ttk.Button(
            master=self._insert_user, text="Palaa edelliseen näkymään", command=self.login)
        reverse_button.pack(fill='x', expand=True, pady=10)