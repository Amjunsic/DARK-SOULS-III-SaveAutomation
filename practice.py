from genericpath import isfile
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter
import os
import shutil
import sys

class AppGui(tkinter.Tk):

    #입력값 텍스트 파일 저장, 경로 저장 유무 확인
    def UserName(name):
        path_list = ["C:/Users/",name,"/AppData/Roaming"]
        f = open("path.txt","a+")
        
        labe = Label(text="현재 경로:"+f.readline())

        #파일에 내용이 입력되어있는지 확인
        if os.stat("path.txt").st_size != 0:
            messagebox.showwarning("경고","경로가 이미 설정되어있습니다.\n" + "현재경로:"+open("path.txt","r").readline())#경로가 설정되어있다고 알림,현재 경로보여주기
            ChangPath = messagebox.askyesno("확인/취소", "현재 경로로 재설정하시겠습니까?\n"+''.join(path_list)) #경로 재설정 질문
            if ChangPath:
                f = open("path.txt", "w")#경로 재설정
                f.write(''.join(path_list))
        else:
            f.write(''.join(path_list)) #C:\Users\name\AppData\Roaming\Dark Souls III
            f.close()
            
    
    #세이브 파일 폴더 벡업폴더로 이동
    def saveMove():
        try:
            filename = filedialog.askdirectory()
            f = open("path.txt","r")
            path = f.readline()
            shutil.move(path,filename)     
        except FileNotFoundError:
            messagebox.showwarning("경로를 찾지못함","경로가 올바르게 설정되어 있는지 확인해 주세요")

    #백업폴더 세이브 파일 폴더로 이동 버튼
    def backupMove():
        try:
            filename = filedialog.askdirectory()
            f = open("path.txt","r")
            path = f.readline()
            shutil.move(filename,path)
        except FileNotFoundError:
             messagebox.showwarning("경로를 찾지못함","경로가 올바르게 설정되어 있는지 확인해 주세요")

    def __init__(self):
            self.root = Tk()
            self.root.title("DARK SOULS™ III SaveAutomation")#타이틀 변경
            self.root.geometry("600x300")#기본 사이즈
            self.root.minsize(410,500)#최소사이즈 설정
            self.root.maxsize(400,700)#최대사이즈 설정
            self.root.call('wm', 'iconphoto', self._w,PhotoImage(file='image.ico'))#윈도우 이미지 변경
            self.root.iconphoto(True, PhotoImage(file='image.ico'))#타이틀 이미지 변경
            
            #라벨
            Label(self.root,text="윈도우 유저 이름 입력").grid(row=0,column=0)#유저이름 라벨
            Label(self.root,text="세이브 폴더->벡업폴더 ").grid(row=2,column=0)#copy버튼 라벨
            Label(self.root,text="백업폴더->세이브 폴더").grid(row=3,column=0)

            
             #윈도우 사용자 이름 입력 엔트리
            self.e = Entry(self.root, width= 30)
            self.e.insert(0,"윈도우 사용자 이름 입력")
            self.e.grid(row=0,column=1)
   
            #유저이름 저장 버튼
            self.UsernameButton = Button(text="저장", width= 5 ,command=lambda: AppGui.UserName(self.e.get()))
            self.UsernameButton.grid(row=0,column=2,padx=2)

            #세이브 파일 폴더 벡업폴더로 이동 버튼
            self.saveMoveButton = Button(text="copy",width=30,command=AppGui.saveMove)
            self.saveMoveButton.grid(row=2,column=1,padx=2)

            #백업폴더 세이브 파일 폴더로 이동 버튼
            self.backupButton = Button(text="backup",width=30,command=AppGui.backupMove)
            self.backupButton.grid(row=3,column=1,padx=2)

            self.root.mainloop()

if __name__ == '__main__':
    root = AppGui()
