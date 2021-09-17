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
            
            #엔트리값 가져오는 함수 
            def UserName():
                name = self.e.get()
                f = open("path.txt","a")
                f.write(name+"\n")
                f.close()
                

            self.UsernameButton = Button(text="저장", command= UserName)#유저이름 저장 버튼
            self.UsernameButton.pack()

            self.root.mainloop()

if __name__ == '__main__':
    root = AppGui()
