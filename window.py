from tkinter import Tk, Button
from tkinter.ttk import Frame


WHITE = '#FFFFFF'
YELLOW = '#FFFF00'
CYAN = '#00FFFF'
LIGHT_GREEN = '#7CFC00'
GREEN = '#008000'
RED = '#FF0000'
BLACK = '#000000'
BLUE = '#0000FF'
MAGENTA = '#FF00FF'

COLORS: list[str] = [
    WHITE,
    YELLOW,
    CYAN,
    LIGHT_GREEN,
    GREEN,
    MAGENTA,
    RED,
    BLUE,
    BLACK
]

INDEX: int = 0


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.attributes(
            '-fullscreen',
            True
        )
        self.__color_frame: Frame = Frame(self)
        self.__color_btn: Button = Button(self.__color_frame, command=self.__on_color_btn_click,
                                          text='Click in center to start\n'
                                               'In the end app will destroy')
        self.__text_exist: bool = True
        self.__grid()

    def __grid(self):
        self.__color_frame.pack(fill='both')
        self.update()
        self.__color_btn.configure(height=self.winfo_height(), width=self.winfo_width())
        self.__color_btn.pack(fill='both')

    def __on_color_btn_click(self):
        if self.__text_exist:
            self.__forget_text()
        try:
            global INDEX
            self.__color_btn.configure(background=COLORS[INDEX])
            INDEX += 1
        except IndexError:
            self.destroy()

    def __forget_text(self):
        self.__color_btn.configure(text='')

    def start(self):
        self.mainloop()
