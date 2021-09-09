from tkinter import *
import tkinter

class AppGui(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.title("DARK SOULS™ III SaveAutomation")
        self.geometry("600x300")
        self.minsize(600,300)
        self.maxsize(900,600)
        self.call('wm', 'iconphoto', self._w,PhotoImage(file='image.ico'))
        self.iconphoto(True, PhotoImage(file='image.ico'))

root = AppGui(NONE)
root.mainloop()