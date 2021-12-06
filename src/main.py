from tkinter import Tk
from ui.ui import UI
from database.handle_database import HandleDatabase
from session.handle_session import HandleSession


def main():
    database = HandleDatabase()
    session = HandleSession()
    root = Tk()
    root.title("Yhteystiedot")
    root.resizable(False, False)
    root.geometry('300x300')
    user_interface = UI(root, database, session)
    user_interface.start_login()
    root.mainloop()


if __name__ == '__main__':
    main()
