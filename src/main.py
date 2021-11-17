from tkinter import Tk
from ui.ui import UI

def main():
   root = Tk()
   root.title("Yhteystiedot")
   root.resizable(False, False)
   ui = UI(root)
   ui.start_login()
   root.mainloop()


if __name__ == '__main__':
    main()