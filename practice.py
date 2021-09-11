from os import name
from tkinter import *
from tkinter import filedialog
import tkinter

class AppGui(tkinter.Tk):

    def FileName(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("xml files", "*.xml"),("all files", "*.*")))
        print(filename)

    def FolderName(slef):
        foldername = filedialog.askdirectory()
        print(foldername)

    def __init__(self):
            self.root = Tk()
            self.root.title("DARK SOULS™ III SaveAutomation")#타이틀 변경
            self.root.geometry("600x300")#기본 사이즈
            self.root.minsize(600,300)#최소사이즈 설정
            self.root.maxsize(900,600)#최대사이즈 설정
            self.root.call('wm', 'iconphoto', self._w,PhotoImage(file='image.ico'))#윈도우 이미지 변경
            self.root.iconphoto(True, PhotoImage(file='image.ico'))#타이틀 이미지 변경
            
            self.filenameButton = Button(text="file", command=self.FileName)#파일 경로버튼 생성
            self.filenameButton.pack()

            self.foldernameButton = Button(text="folder", command=self.FolderName)#폴더 경로버튼 생성
            self.foldernameButton.pack()
             
            self.root.mainloop()

if __name__ == '__main__':
    root = AppGui()