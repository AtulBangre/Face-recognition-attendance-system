from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()