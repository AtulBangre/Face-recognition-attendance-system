from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class tain:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Train Data Set", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images\tit1.jpg")
        img_top=img_top.resize((1530,325))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        b3_1=Button(self.root,text="Start Train", cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"images\tit1.jpg")
        img_bottom=img_bottom.resize((1530,325))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)



if __name__=="__main__":
    root=Tk()
    obj=tain(root)
    root.mainloop()