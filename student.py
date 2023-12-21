from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student_Details:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.root.title("Face Recognition System")

        #=================variables=======================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar() 
    

         # 1st Image
        img=Image.open(r"G:\face recognition attendance system\images\tit.jpg")
        img=img.resize((1530,130))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)

        # # 2nd Image
        # img2=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        # img2=img.resize((510,130))
        # self.photoimg2=ImageTk.PhotoImage(img2)
        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=510,y=0,width=510,height=130)

        # # 3rd Image
        # img3=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        # img3=img3.resize((510,130))
        # self.photoimg3=ImageTk.PhotoImage(img3)
        # f_lbl=Label(self.root,image=self.photoimg3)
        # f_lbl.place(x=1020,y=0,width=510,height=130)

        # bg Image
        bgimg=Image.open(r"G:\face recognition attendance system\images\bg.jpg")
        bgimg=bgimg.resize((1530,710))
        self.photoimgbg=ImageTk.PhotoImage(bgimg)
        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=113,width=1530,height=710)

        # Main label
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=3,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=15,y=55,width=1500,height=600)

        # left Frame
        left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font=('times new roman',12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        # left Image
        img_left=Image.open(r"G:\face recognition attendance system\images\student.jpg")
        img_left=img_left.resize((721,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=721,height=130)

        # current cource Frame
        current_cource_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text="Corrent cource information",font=('times new roman',12,"bold"))
        current_cource_frame.place(x=3,y=135,width=721,height=120)

        # Department
        dep_lebel=Label(current_cource_frame,text="Department",font=('times new roman',12,"bold"),bg="white")
        dep_lebel.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_cource_frame,textvariable=self.var_dep,font=('times new roman',12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","AIML","IT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Cource
        cource_lebel=Label(current_cource_frame,text="Cource",font=('times new roman',12,"bold"),bg="white")
        cource_lebel.grid(row=0,column=2,padx=10,sticky=W)

        cource_combo=ttk.Combobox(current_cource_frame,textvariable=self.var_course,font=('times new roman',12,"bold"),state="readonly")
        cource_combo["values"]=("Select Cource","FE","SE","TE","BE")
        cource_combo.current(0)
        cource_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_lebel=Label(current_cource_frame,text="Year",font=('times new roman',12,"bold"),bg="white")
        year_lebel.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_cource_frame,textvariable=self.var_year,font=('times new roman',12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_lebel=Label(current_cource_frame,text="Semester",font=('times new roman',12,"bold"),bg="white")
        semester_lebel.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_cource_frame,textvariable=self.var_sem,font=('times new roman',12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class student Frame
        class_student_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text="Class student information",font=('times new roman',12,"bold"))
        class_student_frame.place(x=3,y=255,width=721,height=300)
        
        #StudentID
        studentID_lebel=Label(class_student_frame,text="StudentID:",font=('times new roman',12,"bold"),bg="white")
        studentID_lebel.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=('times new roman',12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Student Name
        student_name_lebel=Label(class_student_frame,text="Student Name:",font=('times new roman',12,"bold"),bg="white")
        student_name_lebel.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=('times new roman',12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #Class Division  
        Class_Division_lebel=Label(class_student_frame,text="Class Division:",font=('times new roman',12,"bold"),bg="white")
        Class_Division_lebel.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=('times new roman',12,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #Roll No  
        Roll_No_lebel=Label(class_student_frame,text="Roll No:",font=('times new roman',12,"bold"),bg="white")
        Roll_No_lebel.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        Roll_No_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=('times new roman',12,"bold"))
        Roll_No_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #Gender  
        Gender_lebel=Label(class_student_frame,text="Gender:",font=('times new roman',12,"bold"),bg="white")
        Gender_lebel.grid(row=2,column=0,padx=2,pady=5,sticky=W)

        Gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=('times new roman',12,"bold"),state="readonly",width=18)
        Gender_combo["values"]=("Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        #DOB  
        DOB_lebel=Label(class_student_frame,text="DOB:",font=('times new roman',12,"bold"),bg="white")
        DOB_lebel.grid(row=2,column=2,padx=2,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=('times new roman',12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #Email  
        Email_lebel=Label(class_student_frame,text="Email:",font=('times new roman',12,"bold"),bg="white")
        Email_lebel.grid(row=3,column=0,padx=2,pady=5,sticky=W)

        Email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=('times new roman',12,"bold"))
        Email_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        #Phone No  
        Phone_No_lebel=Label(class_student_frame,text="Phone No:",font=('times new roman',12,"bold"),bg="white")
        Phone_No_lebel.grid(row=3,column=2,padx=2,pady=5,sticky=W)

        Phone_No_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=('times new roman',12,"bold"))
        Phone_No_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)

        #Address  
        Address_lebel=Label(class_student_frame,text="Address:",font=('times new roman',12,"bold"),bg="white")
        Address_lebel.grid(row=4,column=0,padx=2,pady=5,sticky=W)

        Address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=('times new roman',12,"bold"))
        Address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        #Teacher_Name  
        Teacher_Name_lebel=Label(class_student_frame,text="Teacher Name:",font=('times new roman',12,"bold"),bg="white")
        Teacher_Name_lebel.grid(row=4,column=2,padx=2,pady=5,sticky=W)

        Teacher_Name_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=('times new roman',12,"bold"))
        Teacher_Name_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

        #readio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value='Yes')
        radiobtn1.grid(row=6,column=0,padx=5)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value='No')
        radiobtn2.grid(row=6,column=2,padx=2)

        #buttons Frame
        btn_frame=Frame(class_student_frame,relief=RIDGE,bg='white')
        btn_frame.place(x=12,y=200,width=700,height=37)

        save_btn=Button(btn_frame,command=self.add_data,width=18,text="Save",font=('times new roman',12,"bold"),bg="green",fg='white')
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,command=self.update_data,width=18,text="Update",font=('times new roman',12,"bold"),bg="green",fg='white')
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,command=self.delete_data,width=18,text="Delete",font=('times new roman',12,"bold"),bg="green",fg='white')
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset_data,width=18,text="Reset",font=('times new roman',12,"bold"),bg="green",fg='white')
        reset_btn.grid(row=0,column=3)

        #buttons Frame
        btn_frame1=Frame(class_student_frame,relief=RIDGE,bg='white')
        btn_frame1.place(x=3,y=235,width=708,height=37)

        take_photo_btn=Button(btn_frame1,command=self.generate_data,width=38,text="Take Photo sample",font=('times new roman',12,"bold"),bg="green",fg='white')
        take_photo_btn.grid(row=0,column=0)

        reset_btn=Button(btn_frame1,width=38,text="Update Photo sample",font=('times new roman',12,"bold"),bg="green",fg='white')
        reset_btn.grid(row=0,column=1)
     
        


        # right Frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font=('times new roman',12,"bold"))
        right_frame.place(x=755,y=10,width=730,height=580)

        # right Image
        img_right=Image.open(r"G:\face recognition attendance system\images\stutable.jpg")
        img_right=img_right.resize((721,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=721,height=130)

        # ==========================Search System Frame==========================
        searchSystem_frame=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE,text="Search System",font=('times new roman',12,"bold"))
        searchSystem_frame.place(x=3,y=135,width=721,height=70)

        searchBy=Label(searchSystem_frame,text="Search By:",font=('times new roman',15,"bold"),bg="white")
        searchBy.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        searchCombo=ttk.Combobox(searchSystem_frame,font=('times new roman',12,"bold"),state="readonly")
        searchCombo["values"]=("Select","Roll No","Phone No")
        searchCombo.current(0)
        searchCombo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        searchEntry=ttk.Entry(searchSystem_frame,width=20,font=('times new roman',12,"bold"))
        searchEntry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        seach_btn=Button(searchSystem_frame,width=11,text="Search",font=('times new roman',12,"bold"),bg="green",fg='white')
        seach_btn.grid(row=0,column=3,padx=5,pady=5,)

        showAll_btn=Button(searchSystem_frame,width=11,text="Show All",font=('times new roman',12,"bold"),bg="green",fg='white')
        showAll_btn.grid(row=0,column=4,padx=5,pady=5,)

        # ==========================Table Frame==========================
        table_frame=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=3,y=209,width=721,height=345)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.studen_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.studen_table.xview)
        scroll_y.config(command=self.studen_table.yview)

        self.studen_table.heading("dep",text="Department")
        self.studen_table.heading("course",text="Course")
        self.studen_table.heading("year",text="Year")
        self.studen_table.heading("sem",text="Semester")
        self.studen_table.heading("id",text="StudentID")
        self.studen_table.heading("name",text="Name")
        self.studen_table.heading("div",text="Division")
        self.studen_table.heading("roll",text="Roll No")
        self.studen_table.heading("gender",text="Gender")
        self.studen_table.heading("dob",text="DOB")
        self.studen_table.heading("email",text="Email")
        self.studen_table.heading("phone",text="Phone")
        self.studen_table.heading("address",text="Address")
        self.studen_table.heading("teacher",text="Teacher")
        self.studen_table.heading("photo",text="Photo")
        self.studen_table["show"]="headings"

        self.studen_table.column("dep", width=100)   
        self.studen_table.column("course", width=100)
        self.studen_table.column("year", width=100)  
        self.studen_table.column("sem", width=100)   
        self.studen_table.column("id", width=100)    
        self.studen_table.column("name", width=100)  
        self.studen_table.column("div", width=100)   
        self.studen_table.column("roll", width=100)  
        self.studen_table.column("gender", width=100)
        self.studen_table.column("dob", width=100)   
        self.studen_table.column("email", width=100) 
        self.studen_table.column("phone", width=100) 
        self.studen_table.column("address", width=100)
        self.studen_table.column("teacher", width=100)
        self.studen_table.column("photo", width=150)

        self.studen_table.pack(fill=BOTH,expand=1)
        self.studen_table.bind("<ButtonRelease>", self.get_courser)
        self.fetch_data()
        
    #=======functions=======
        
    #=======dd_data=======
        
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password='07632',database='face_recognition')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}", parent=self.root)
    
    #======= fetch_data =======
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username='root',password='07632',database='face_recognition')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.studen_table.delete(*self.studen_table.get_children())
            for i in data:
                self.studen_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #======= get courser =======
    def get_courser(self,event=""):
        courser_focus=self.studen_table.focus()
        content=self.studen_table.item(courser_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username='root',password='07632',database='face_recognition')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,course=%s,year=%s,semester=%s,division=%s,name=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where id=%s",(   
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_name.get(),
                                                                                                                
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_id.get()
                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update complete", parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}", parent=self.root)
    
    
    # delete functrion
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete data","Do you want to delete data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username='root',password='07632',database='face_recognition')
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)    

    #========== Reset data =================
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set("")
        self.var_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #========== Generate Data set =================
    def generate_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password='07632',database='face_recognition')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,course=%s,year=%s,semester=%s,division=%s,name=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where id=%s",(   
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_name.get(),
                                                                                                                
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_id.get()==id+1
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            # ================== loading predefine frontal facedata=====================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3 minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        # file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        file_name_path=f"data/user.{id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed successfully")

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                print(es)

    



if __name__=="__main__":
    root=Tk()
    obj=Student_Details(root)
    root.mainloop()