from tkinter import Tk
from ui.ui import UI
from handle_database import HandleDatabase
from session.handle_session import HandleSession

def main():
   db = HandleDatabase()
   session = HandleSession()
   root = Tk()
   root.title("Yhteystiedot")
   root.resizable(False, False)
   root.geometry('300x300')
   ui = UI(root, db, session)
   ui.start_login()
   root.mainloop()


if __name__ == '__main__':
    main()