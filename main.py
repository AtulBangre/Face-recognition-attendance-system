from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # 1st Image
        img=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        img=img.resize((510,130))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

        # 2nd Image
        img2=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        img2=img.resize((510,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=510,height=130)

        # 3rd Image
        img3=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        img3=img3.resize((510,130))
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=0,width=510,height=130)

        # bg Image
        bgimg=Image.open(r"G:\face recognition attendance system\images\bg.jpg")
        bgimg=bgimg.resize((1530,710))
        self.photoimgbg=ImageTk.PhotoImage(bgimg)
        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # Main label
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student Button
        img4=Image.open(r"G:\face recognition attendance system\images\bt1.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Student Details", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Detect Face Button
        img5=Image.open(r"G:\face recognition attendance system\images\bt1.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,image=self.photoimg4, cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)
        b2_1=Button(bg_img,text="Face Detector", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)

        # Attendance Button
        img6=Image.open(r"G:\face recognition attendance system\images\bt1.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,image=self.photoimg4, cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)
        b3_1=Button(bg_img,text="Face Detector", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)

        # AHelp Desk Button
        img7=Image.open(r"G:\face recognition attendance system\images\bt1.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg4, cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)
        b4_1=Button(bg_img,text="Face Detector", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)
        



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()