from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="#023ebf",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        bgimg=Image.open(r"images\recognizBG.jpg")
        bgimg=bgimg.resize((1530,800))
        self.photoimgbg=ImageTk.PhotoImage(bgimg)
        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=45,width=1530,height=800)

      
        b3_1=Button(bg_img,command=self.face_reco,text="Start", cursor="hand2",font=("times new roman",30,"bold"),bg="#023ebf",fg="white")
        b3_1.place(x=165,y=430,width=400,height=60) 



    # ==========attendance==============
    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            my_dataList=f.readlines()
       
            name_list=[]
            for line in my_dataList:     
                entry=line.split((","))         
                name_list.append(entry[0])
           
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):        
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
               
            
                

    def face_reco(self):
        def Draw_Boandry(img,classifier,scaleFector,minNeighbor,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFector,minNeighbor)
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username='root',password='07632',database='face_recognition')
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Department from student where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select id from student where id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>65:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Name:{n}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    self.mark_attendence(i,r,n,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord=Draw_Boandry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognizer",img)


            if cv2.waitKey(1)==13:
                
                video_cap.release()
                cv2.destroyAllWindows()
                break


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()