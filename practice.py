import builtins
from tkinter import *
from tkinter import filedialog
import tkinter
import os
import shutil

"""
path.txt 내용

총 4줄

1. 그래픽 파일 이름(원본)
2. 세이브 폴더 경로 (원본)
3. 다크소울 세이브 폴더위치 
4. 세이브 파일 벡업할 폴더 위치
"""



class AppGui(tkinter.Tk):

    #입력값 텍스트 파일에 저장
    def UserName(name):
        path_list = ["C:\\Users\\",name,"\\AppData\\Roaming\\Dark Souls III"]
        f = open("path.txt","a")
        f.write(name+"\n")
        f.write(''.join(path_list)) #C:\Users\name\AppData\Roaming\Dark Souls III
        f.close()


    def __init__(self):
            self.root = Tk()
            self.root.title("DARK SOULS™ III SaveAutomation")#타이틀 변경
            self.root.geometry("600x300")#기본 사이즈
            self.root.minsize(600,300)#최소사이즈 설정
            self.root.maxsize(900,600)#최대사이즈 설정
            self.root.call('wm', 'iconphoto', self._w,PhotoImage(file='image.ico'))#윈도우 이미지 변경
            self.root.iconphoto(True, PhotoImage(file='image.ico'))#타이틀 이미지 변경
            
            #윈도우 사용자 이름 입력 엔트리
            self.e = Entry(self.root, width= 30)
            self.e.insert(0,"윈도우 사용자 이름 입력")
            self.e.pack()
   
            #유저이름 저장 버튼
            self.UsernameButton = Button(text="저장", command=lambda: AppGui.UserName(self.e.get()))
            self.UsernameButton.pack()

            self.root.mainloop()

if __name__ == '__main__':
    root = AppGui()
