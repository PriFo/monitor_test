from tkinter import messagebox as mb
from window import MainWindow


class App:

    def __init__(self):
        self.__window = MainWindow()

    def exec(self):
        try:
            self.__window.start()
        except Exception as e:
            mb.showerror(str(e.args[0]), str(e))
