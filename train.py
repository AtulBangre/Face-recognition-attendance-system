from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.root.title("Face Recognition System")
        

        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="#023ebf",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        bgimg=Image.open(r"images\training.jpg")
        bgimg=bgimg.resize((1530,800))
        self.photoimgbg=ImageTk.PhotoImage(bgimg)
        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=45,width=1530,height=800)

      
        b3_1=Button(bg_img,command=self.train_classifier,text="Start", cursor="hand2",font=("times new roman",30,"bold"),bg="#023ebf",fg="white")
        b3_1.place(x=215,y=430,width=300,height=60) 

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        id=[]
        for image in path:
            img=Image.open(image).convert('L')  #Gray scale image
            imageNP=np.array(img,'uint8')
            ids=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNP)
            id.append(ids)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        
        id=np.array(id)

        # ======= Train the classifier=============
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,id)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data completed")



if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()