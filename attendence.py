from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendence:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.root.title("Face Recognition System")
        # =========variables================
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_department=StringVar()    
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendence=StringVar()    
        
        

         # 1st Image
        img=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # 2nd Image
        img2=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        img2=img.resize((800,200))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # bg Image
        bgimg=Image.open(r"G:\face recognition attendance system\images\bg.jpg")
        bgimg=bgimg.resize((1530,710))
        self.photoimgbg=ImageTk.PhotoImage(bgimg)
        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=200,width=1530,height=710)

        # Main label
        title_lbl=Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # MAIN FRAME
        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=15,y=55,width=1500,height=529)

        # left Frame
        left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Attendance Details",font=('times new roman',12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=505)

        # left Image
        img_left=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        img_left=img.resize((721,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=721,height=130)

        leftInside_frame=Frame(left_frame,bd=2,bg='white',relief=RIDGE)
        leftInside_frame.place(x=3,y=131,width=720,height=348)

        # Labbeld Entry
        #Attendens ID
        attendence_ID_lebel=Label(leftInside_frame,text="AttendenceID:",font=('times new roman',12,"bold"),bg="white")
        attendence_ID_lebel.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        attendence_ID_entry=ttk.Entry(leftInside_frame,textvariable=self.var_attend_id,width=20,font=('times new roman',12,"bold"))
        attendence_ID_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Roll
        Roll_lebel=Label(leftInside_frame,text="Roll No:",font=('times new roman',12,"bold"),bg="white")
        Roll_lebel.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        Roll_entry=ttk.Entry(leftInside_frame,textvariable=self.var_attend_roll,width=20,font=('times new roman',12,"bold"))
        Roll_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #Name
        name_lebel=Label(leftInside_frame,text="Name:",font=('times new roman',12,"bold"),bg="white")
        name_lebel.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        name_entry=ttk.Entry(leftInside_frame,textvariable=self.var_attend_name,width=20,font=('times new roman',12,"bold"))
        name_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #Department
        Department_lebel=Label(leftInside_frame,text="Department:",font=('times new roman',12,"bold"),bg="white")
        Department_lebel.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        Department_entry=ttk.Entry(leftInside_frame,textvariable=self.var_attend_department,width=20,font=('times new roman',12,"bold"))
        Department_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #Time
        Time_lebel=Label(leftInside_frame,text="Time:",font=('times new roman',12,"bold"),bg="white")
        Time_lebel.grid(row=2,column=0,padx=2,pady=5,sticky=W)

        Time_entry=ttk.Entry(leftInside_frame,textvariable=self.var_attend_time,width=20,font=('times new roman',12,"bold"))
        Time_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        #Date
        Date_lebel=Label(leftInside_frame,text="Date:",font=('times new roman',12,"bold"),bg="white")
        Date_lebel.grid(row=2,column=2,padx=2,pady=5,sticky=W)

        Date_entry=ttk.Entry(leftInside_frame,textvariable=self.var_attend_date,width=20,font=('times new roman',12,"bold"))
        Date_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #Attendce Statue
        attend_lebel=Label(leftInside_frame,text="Attendence Status:",font=('times new roman',12,"bold"),bg="white")
        attend_lebel.grid(row=3,column=0,padx=2,pady=5,sticky=W)

        div_combo=ttk.Combobox(leftInside_frame,textvariable=self.var_attend_attendence,font=('times new roman',12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Present","Absent")
        div_combo.current(0)
        div_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        #buttons Frame
        btn_frame=Frame(leftInside_frame,relief=RIDGE,bg='white')
        btn_frame.place(x=12,y=300,width=700,height=37)

        import_btn=Button(btn_frame,command=self.importCsv,width=18,text="Import csv",font=('times new roman',12,"bold"),bg="green",fg='white')
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,command=self.exportCsv,width=18,text="Export csv",font=('times new roman',12,"bold"),bg="green",fg='white')
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,width=18,text="Update",font=('times new roman',12,"bold"),bg="green",fg='white')
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset_data,width=18,text="Reset",font=('times new roman',12,"bold"),bg="green",fg='white')
        reset_btn.grid(row=0,column=3)

        # right Frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font=('times new roman',12,"bold"))
        right_frame.place(x=755,y=10,width=730,height=505)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=718,height=475)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTabel=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTabel.xview)
        scroll_y.config(command=self.AttendenceReportTabel.yview)

        self.AttendenceReportTabel.heading("id",text="Attendence ID")
        self.AttendenceReportTabel.heading("roll",text="Roll No")
        self.AttendenceReportTabel.heading("name",text="Name")
        self.AttendenceReportTabel.heading("department",text="Department")
        self.AttendenceReportTabel.heading("time",text="Time")
        self.AttendenceReportTabel.heading("date",text="Date")
        self.AttendenceReportTabel.heading("attendence",text="Attendence")
        self.AttendenceReportTabel["show"]="headings"
        self.AttendenceReportTabel.column("id",width=100)
        self.AttendenceReportTabel.column("roll",width=100)     
        self.AttendenceReportTabel.column("name",width=100)     
        self.AttendenceReportTabel.column("department",width=100)
        self.AttendenceReportTabel.column("time",width=100)     
        self.AttendenceReportTabel.column("date",width=100)     
        self.AttendenceReportTabel.column("attendence",width=100)

        self.AttendenceReportTabel.pack(fill=BOTH,expand=1)

        self.AttendenceReportTabel.bind("<ButtonRelease>",self.get_courser)
    def fetchData(self,rows):
        self.AttendenceReportTabel.delete(*self.AttendenceReportTabel.get_children())
        for i in rows:
            self.AttendenceReportTabel.insert("",END,values=i)
    # import CSV   
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file",".csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file",".csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="\n") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}", parent=self.root)
            
    # get courser
    def get_courser(self,event=""):
        cursor_row=self.AttendenceReportTabel.focus()
        content=self.AttendenceReportTabel.item(cursor_row)
        rows=content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_department.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendence.set(rows[6])
    
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_department.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendence.set("")


if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()