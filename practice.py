import builtins
from tkinter import *
from tkinter import filedialog
import tkinter
import os
import shutil

"""
아무말
"""


class AppGui(tkinter.Tk):

    def FileName():
        #그래픽파일 경로(원본)
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("xml files", "*.xml"),("all files", "*.*")))
        f = open("path.txt","a")
        f.write(os.path.basename(filename)+"\n")
        f.close()

    def FolderName():
        #세이브폴더 경로(원본)
        foldername = filedialog.askdirectory()
        f = open("path.txt", "a")
        f.write(foldername+"\n")
        f.close()
    
    def Copy():
        f = open("path.txt","r")
        filename = f.readline()
        filename = filename.strip()

        folderpath = f.readline()
        filename = filename.strip()
        print(filename)
        print(folderpath)
        f.close()


    def __init__(self):
            self.root = Tk()
            self.root.title("DARK SOULS™ III SaveAutomation")#타이틀 변경
            self.root.geometry("600x300")#기본 사이즈
            self.root.minsize(600,300)#최소사이즈 설정
            self.root.maxsize(900,600)#최대사이즈 설정
            self.root.call('wm', 'iconphoto', self._w,PhotoImage(file='image.ico'))#윈도우 이미지 변경
            self.root.iconphoto(True, PhotoImage(file='image.ico'))#타이틀 이미지 변경
            
            self.filenameButton = Button(text="file", command= AppGui.FileName)#파일이름 저장 버튼
            self.filenameButton.pack()

            self.folderpathButton = Button(text="folder",command=AppGui.FolderName)#세이브 파일 경로 저장 버튼
            self.folderpathButton.pack()

            self.SavefolderButton = Button(text="saveFolder", command=AppGui.FolderName)
            self.SavefolderButton.pack()

            self.copyButton = Button(text="copy", command=AppGui.Copy)
            self.copyButton.pack()

            self.root.mainloop()

if __name__ == '__main__':
    root = AppGui()
