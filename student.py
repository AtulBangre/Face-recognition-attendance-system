from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Student_Details:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
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
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=15,y=55,width=1500,height=600)

        # left Frame
        left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font=('times new roman',12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        # left Image
        img_left=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        img_left=img.resize((721,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=721,height=130)

        # current cource Frame
        current_cource_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text="Corrent cource information",font=('times new roman',12,"bold"))
        current_cource_frame.place(x=3,y=135,width=721,height=120)

        # Department
        dep_lebel=Label(current_cource_frame,text="Department",font=('times new roman',12,"bold"),bg="white")
        dep_lebel.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_cource_frame,font=('times new roman',12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","AIML","IT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Cource
        cource_lebel=Label(current_cource_frame,text="Cource",font=('times new roman',12,"bold"),bg="white")
        cource_lebel.grid(row=0,column=2,padx=10,sticky=W)

        cource_combo=ttk.Combobox(current_cource_frame,font=('times new roman',12,"bold"),state="readonly")
        cource_combo["values"]=("Select Cource","FE","SE","TE","BE")
        cource_combo.current(0)
        cource_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Cource
        year_lebel=Label(current_cource_frame,text="Year",font=('times new roman',12,"bold"),bg="white")
        year_lebel.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_cource_frame,font=('times new roman',12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_lebel=Label(current_cource_frame,text="Semester",font=('times new roman',12,"bold"),bg="white")
        semester_lebel.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_cource_frame,font=('times new roman',12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class student Frame
        class_student_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text="Class student information",font=('times new roman',12,"bold"))
        class_student_frame.place(x=3,y=255,width=721,height=300)
        
        #StudentID
        studentID_lebel=Label(class_student_frame,text="StudentID:",font=('times new roman',12,"bold"),bg="white")
        studentID_lebel.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Student Name
        student_name_lebel=Label(class_student_frame,text="Student Name:",font=('times new roman',12,"bold"),bg="white")
        student_name_lebel.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #Class Division  
        Class_Division_lebel=Label(class_student_frame,text="Class Division:",font=('times new roman',12,"bold"),bg="white")
        Class_Division_lebel.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        Class_Division_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        Class_Division_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #Roll No  
        Roll_No_lebel=Label(class_student_frame,text="Roll No:",font=('times new roman',12,"bold"),bg="white")
        Roll_No_lebel.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        Roll_No_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        Roll_No_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #Gender  
        Gender_lebel=Label(class_student_frame,text="Gender:",font=('times new roman',12,"bold"),bg="white")
        Gender_lebel.grid(row=2,column=0,padx=2,pady=5,sticky=W)

        Gender_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        Gender_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        #DOB  
        DOB_lebel=Label(class_student_frame,text="DOB:",font=('times new roman',12,"bold"),bg="white")
        DOB_lebel.grid(row=2,column=2,padx=2,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #Email  
        Email_lebel=Label(class_student_frame,text="Email:",font=('times new roman',12,"bold"),bg="white")
        Email_lebel.grid(row=3,column=0,padx=2,pady=5,sticky=W)

        Email_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        Email_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        #Phone No  
        Phone_No_lebel=Label(class_student_frame,text="Phone No:",font=('times new roman',12,"bold"),bg="white")
        Phone_No_lebel.grid(row=3,column=2,padx=2,pady=5,sticky=W)

        Phone_No_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        Phone_No_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)

        #Address  
        Address_lebel=Label(class_student_frame,text="Address:",font=('times new roman',12,"bold"),bg="white")
        Address_lebel.grid(row=4,column=0,padx=2,pady=5,sticky=W)

        Address_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        Address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        #Teacher_Name  
        Teacher_Name_lebel=Label(class_student_frame,text="Teacher Name:",font=('times new roman',12,"bold"),bg="white")
        Teacher_Name_lebel.grid(row=4,column=2,padx=2,pady=5,sticky=W)

        Teacher_Name_entry=ttk.Entry(class_student_frame,width=20,font=('times new roman',12,"bold"))
        Teacher_Name_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

        #readio Buttons
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value='Yes')
        radiobtn1.grid(row=6,column=0,padx=5)

        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value='Yes')
        radiobtn2.grid(row=6,column=1,padx=2)

        #buttons Frame
        btn_frame=Frame(class_student_frame,relief=RIDGE,bg='white')
        btn_frame.place(x=12,y=200,width=700,height=37)

        save_btn=Button(btn_frame,width=18,text="Save",font=('times new roman',12,"bold"),bg="green",fg='white')
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=18,text="Update",font=('times new roman',12,"bold"),bg="green",fg='white')
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=18,text="Delete",font=('times new roman',12,"bold"),bg="green",fg='white')
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=18,text="Reset",font=('times new roman',12,"bold"),bg="green",fg='white')
        reset_btn.grid(row=0,column=3)

        #buttons Frame
        btn_frame1=Frame(class_student_frame,relief=RIDGE,bg='white')
        btn_frame1.place(x=3,y=235,width=708,height=37)

        take_photo_btn=Button(btn_frame1,width=38,text="Take Photo",font=('times new roman',12,"bold"),bg="green",fg='white')
        take_photo_btn.grid(row=0,column=0)

        reset_btn=Button(btn_frame1,width=38,text="Reset",font=('times new roman',12,"bold"),bg="green",fg='white')
        reset_btn.grid(row=0,column=1)
     
        


        # right Frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font=('times new roman',12,"bold"))
        right_frame.place(x=755,y=10,width=730,height=580)

if __name__ == "__main__":
    root=Tk()
    obj=Student_Details(root)
    root.mainloop()