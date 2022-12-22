from tkinter import messagebox as mb
from window import MainWindow


class App:

    def __init__(self) -> None:
        try:
            self.__window: MainWindow = MainWindow()
        except Exception as e:
            mb.showerror(str(e.args[0]), str(e))
            self.__window = None

    def exec(self) -> None:
        if self.__window:
            self.__window.start()
