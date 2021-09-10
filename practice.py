from os import name
from tkinter import *
import tkinter

class AppGui(tkinter.Tk):

    def __init__(self):
            self.root = Tk()
            self.root.title("DARK SOULS™ III SaveAutomation")
            self.root.geometry("600x300")
            self.root.minsize(600,300)
            self.root.maxsize(900,600)
            self.root.call('wm', 'iconphoto', self._w,PhotoImage(file='image.ico'))
            self.root.iconphoto(True, PhotoImage(file='image.ico'))
            self.root.mainloop()

if __name__ == '__main__':
    root = AppGui()