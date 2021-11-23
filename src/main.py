from tkinter import Tk
from ui.ui import UI
from handle_database import HandleDatabase

def main():
   db = HandleDatabase()
   root = Tk()
   root.title("Yhteystiedot")
   root.resizable(False, False)
   root.geometry('300x300')
   ui = UI(root, db)
   ui.start_login()
   root.mainloop()


if __name__ == '__main__':
    main()