#import module from tkinter for UI
from tkinter import *
from playsound import playsound
import os
from datetime import datetime;
import xlrd
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("py tester.py")
    
def function2():
    
    os.system("py resizeImages.py")

def function3():

    os.system("py recognise.py")
    

def function5():    
   os.system("py showreport")
   
def function6():

    root.destroy()


def attend():
    os.startfile(os.getcwd()+"Attendance_Sheets/attendance"+str(datetime.now().date())+'.xls')
    os.startfile(os.getcwd()+"Attendance_Sheets/attendance"+str(datetime.now().date())+'.xls')
    
#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Test Images",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
#Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
