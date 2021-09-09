from tkinter import *
import tkinter

class AppGui(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        pass

root = AppGui(NONE)
root.title("DARK SOULS™ III SaveAutomation")
root.geometry("600x300")
root.minsize(600,300)
root.maxsize(900,600)
root.call('wm', 'iconphoto', root._w,PhotoImage(file='image.ico'))
root.iconphoto(True, PhotoImage(file='image.ico'))
root.mainloop()