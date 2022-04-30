from tkinter import *
from tkinter import ttk
import mysql.connector as con
import random
import datetime
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()
root.title("SAATHI")
root.geometry("1500x1000+0+0")
l=[]
for i in range(1,13):
    l.append(i)
k=['A','B','C','D','E']
value=random.choice(k)
j=['Fantastic','Superb','Awesome','Very Good','Good']    
value1=random.choice(j)

def feepay():

    root1.withdraw()
    global top4
    top4=Toplevel()
    top4.geometry("1500x1000+0+0")
    labelframe7 = LabelFrame(top4, text="STUDENT",bd=10,font=("times new roman", 18))
    labelframe7.place(x=10,y=40)
    lb11=Label(labelframe7 ,text="Name :-",font=("andalus",18)).grid(row=0,column=0,pady=20,sticky=W)
    global e11
    e11=Entry(labelframe7 ,relief="solid",bg="white",font=("andalus",16))
    e11.grid(row=0,column=1,pady=20)
    lb12=Label(labelframe7 ,text="Age :-",font=("andalus",18)).grid(row=1,column=0,pady=20,sticky=W)
    global e12
    e12=Entry(labelframe7 ,relief="solid",bg="white",font=("andalus",16))
    e12.grid(row=1,column=1,pady=20)
    lb13=Label(labelframe7 ,text="Gender :-",font=("andalus",18)).grid(row=2,column=0,pady=20,sticky=W)
    lb14=Label(labelframe7 ,text="Class :-  ",font=("andalus",18)).grid(row=3,column=0,pady=20,sticky=W)
    lb15=Label(labelframe7 ,text="Section allocated :-  ",font=("andalus",18)).grid(row=4,column=0,pady=20,sticky=W)
    global e16
    e16=Entry(labelframe7 ,relief="solid",bg="white",font=("andalus",16))
    e16.grid(row=4,column=1,pady=20)
    lb16=Label(labelframe7 ,text="Enter ROLL NO. :-  ",font=("andalus",18)).grid(row=5,column=0,pady=20,sticky=W)
    global e17
    e17=Entry(labelframe7 ,width=10,relief="solid",bg="white",font=("andalus",16))
    e17.grid(row=5,column=1,pady=20,sticky=W)
    lb17=Label(labelframe7 ,text="Fees :-  ",font=("andalus",18)).grid(row=6,column=0,pady=20,sticky=W)
    global e18
    e18=Entry(labelframe7 ,width=10,relief="solid",bg="white",font=("andalus",16))
    e18.grid(row=6,column=1,pady=20,sticky=W)
    bt11=Button(top4,text="PAY FEES",activebackground="#78d6ff",padx=92,pady=28,bg="green",fg="white",command=click_confirm5,relief="groove").place(x=11,y=495)
    global clicked4
    clicked4=IntVar()
    OptionMenu(labelframe7 ,clicked2,*l).grid(row=3,column=1,pady=20,ipadx=92)
    global clicked5
    clicked5=StringVar()
    OptionMenu(labelframe7 ,clicked3,"M","F","TRANSGENDER").grid(row=2,column=1,pady=20,ipadx=58)
    
    b=24000

def newadm():
    root.withdraw()
    global top
    top=Toplevel()
    top.geometry("1500x1000+0+0")
    l1=Label(top,text="Name :-",font=("andalus",18)).place(x=15,y=60)
    
    global e
    e=Entry(top,relief="solid",bg="white",font=("andalus",16))
    e.place(x=105,y=50,width=191,height=40)
    l2=Label(top,text="Age :-",font=("andalus",18)).place(x=15,y=132)
    global e1
    e1=Entry(top,relief="solid",bg="white",font=("andalus",16))
    e1.place(x=105,y=117,width=68,height=40)
    l2=Label(top,text="Gender :-",font=("andalus",18)).place(x=11,y=203)
    l3=Label(top,text="Mobile number:-  ",font=("andalus",18)).place(x=11,y=269)
    l4=Label(top,text="State :-  ",font=("andalus",18)).place(x=11,y=335)
    global e19
    e19=Entry(top,width=20,relief="solid",bg="white",font=("andalus",16))
    e19.place(x=215,y=328)
    l5=Label(top,text="District :-  ",font=("andalus",18)).place(x=11,y=410)
    global e3
    e3=Entry(top,width=40,relief="solid",bg="white",font=("andalus",16))
    e3.place(x=231,y=400,width=68,height=40)
    b1=Button(top,text="APPLY",activebackground="#78d6ff",padx=95,pady=28,bg="green",command=click_confirm1,relief="groove").place(x=11,y=495)
    global e5
    e5=Entry(top,width=40,relief="solid",bg="white",font=("andalus",16))
    e5.place(x=194,y=259,width=178,height=40)
    global clicked1
    clicked1=StringVar()
    OptionMenu(top,clicked1,"M","F","TRANSGENDER").place(x=115,y=191,width=191,height=40)
    l7=Label(top,text="City:-",font=("andalus",18)).place(x=431,y=60)
    global e4
    e4=Entry(top,relief="solid",bg="white",font=("andalus",16))
    e4.place(x=559,y=50,width=191,height=40)
    l8=Label(top,text="House number:-",font=("andalus",18)).place(x=431,y=160)
    global e20
    e20=Entry(top,relief="solid",bg="white",font=("andalus",16))
    e20.place(x=669,y=150,width=191,height=40)
    l9=Label(top,text="Disability:-",font=("andalus",18)).place(x=631,y=260)
    e21=Entry(top,relief="solid",bg="white",font=("andalus",16))
    e21.place(x=769,y=250,width=191,height=40)
    l10=Label(top,text="Occupation:-",font=("andalus",18)).place(x=631,y=360)
    global clicked9
    clicked9=StringVar()
    OptionMenu(top,clicked9,"Civilian","Defence").place(x=769,y=350,width=191,height=40)
    l11=Label(top,text="Pincode:-",font=("andalus",18)).place(x=631,y=460)
    e22=Entry(top,relief="solid",bg="white",font=("andalus",16))
    e22.place(x=769,y=450,width=191,height=40)87




    
def stdlogin1():
    root1.withdraw()
    global top1
    top1=Toplevel()
    top1.geometry("1500x1000+0+0")
    labelframe4 = LabelFrame(top1, text="STUDENT",bd=10,font=("times new roman", 18))
    labelframe4.place(x=10,y=40)
    lb1=Label(labelframe4 ,text="Name :-",font=("andalus",18)).grid(row=0,column=0,pady=20,sticky=W)
    global e6
    e6=Entry(labelframe4 ,relief="solid",bg="white",font=("andalus",16))
    e6.grid(row=0,column=1,pady=20)
    lb2=Label(labelframe4 ,text="Age :-",font=("andalus",18)).grid(row=1,column=0,pady=20,sticky=W)
    global e7
    e7=Entry(labelframe4 ,relief="solid",bg="white",font=("andalus",16))
    e7.grid(row=1,column=1,pady=20)
    lb3=Label(labelframe4 ,text="Gender :-",font=("andalus",18)).grid(row=2,column=0,pady=20,sticky=W)
    lb4=Label(labelframe4 ,text="Class :-  ",font=("andalus",18)).grid(row=3,column=0,pady=20,sticky=W)
    lb5=Label(labelframe4 ,text="Section allocated :-  ",font=("andalus",18)).grid(row=4,column=0,pady=20,sticky=W)
    global e9
    e9=Entry(labelframe4 ,relief="solid",bg="white",font=("andalus",16))
    e9.grid(row=4,column=1,pady=20)
    lb7=Label(labelframe4 ,text="Enter ROLL NO. in the range 1 to 40 :-  ",font=("andalus",18)).grid(row=5,column=0,pady=20,sticky=W)
    global e8
    e8=Entry(labelframe4 ,width=10,relief="solid",bg="white",font=("andalus",16))
    e8.grid(row=5,column=1,pady=20,sticky=W)
    lb8=Label(labelframe4 ,text="Fees :-  ",font=("andalus",18)).grid(row=6,column=0,pady=20,sticky=W)
    global e10
    e10=Entry(labelframe4 ,width=10,relief="solid",bg="white",font=("andalus",16))
    e10.grid(row=6,column=1,pady=20,sticky=W)
    bt1=Button(top1 ,text="UPDATE",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm2,relief="groove").place(x=48,y=640)
    bt2=Button(top1 ,text="SEARCH",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm3,relief="groove").place(x=292,y=640)
    bt3=Button(top1 ,text="DISPLAY ALL",activebackground="#78d6ff",padx=82,pady=28,bg="green",fg="white",command=click_confirm4,relief="groove").place(x=48,y=720)
    bt4=Button(top1,text="PAY FEES",activebackground="#78d6ff",padx=92,pady=28,bg="green",fg="white",command=click_confirm5,relief="groove").place(x=292,y=720)
    global clicked2
    clicked2=IntVar()
    OptionMenu(labelframe4 ,clicked2,*l).grid(row=3,column=1,pady=20,ipadx=92)
    global clicked3
    clicked3=StringVar()
    OptionMenu(labelframe4 ,clicked3,"M","F","TRANSGENDER").grid(row=2,column=1,pady=20,ipadx=58)
    global b
    b=24000
    

        

def stdlogin():
    global root1
    root1=Toplevel()
    root1.geometry("690x350")
    labelframe5 = LabelFrame(root1, text="LOGIN WINDOW",font=("impact",22),bg="green",relief="ridge",bd=30,padx=25,pady=25)
    labelframe5.place(x=120,y=40)
    lbl1=Label(labelframe5 ,text="Username:-",font=("andalus",16),bg="green",fg="white").grid(row=0,column=0)
    lbl2=Label(labelframe5 ,text="Password:-",font=("andalus",16),bg="green",fg="white").grid(row=1,column=0)
    lbl3=Label(root1 ,text="You need to enter roll number of a student in order access all student database  ",font=("monotype corsiva",17),bg="black",fg="white").place(x=10,y=290)
    global en1
    en1=Entry(labelframe5,width=12,font=("andalus",16),relief="solid",bg="white",show="#")
    en1.grid(row=0,column=1)
    global en2
    en2=Entry(labelframe5,width=12,font=("andalus",16),relief="solid",bg="white",show="*")
    en2.grid(row=1,column=1)
    btn1=Button(labelframe5 ,text="LOGIN",font=("andalus",16),bg="green",fg="white",command=loginwin).grid(row=2,column=0)
    btn2=Button(labelframe5 ,text="RESET",font=("andalus",16),bg="green",fg="white",command=resetpw).grid(row=2,column=1)
    btn3=Button(labelframe5 ,text="EXIT",font=("andalus",16),bg="green",fg="white",command=root1.destroy).grid(row=2,column=2)
    
    
def resetpw():
    global us
    us=en1.get()
    global pw
    pw=en2.get()

def loginwin():
    if pw==str(en2.get()) and us==str(en1.get()):
        stdlogin1()
    else:
        messagebox.showerror("SAATHI","Incorrect username or password!!!\n please try again")


def feepay():
    root.withdraw()
    global top4
    top4=Toplevel()
    top4.geometry("1500x1000+0+0")
    labelframe7 = LabelFrame(top4, text="STUDENT",bd=10,font=("times new roman", 18))
    labelframe7.place(x=10,y=40)
    lb11=Label(labelframe7 ,text="Name :-",font=("andalus",18)).grid(row=0,column=0,pady=20,sticky=W)
    global e11
    e11=Entry(labelframe7 ,relief="solid",bg="white",font=("andalus",16))
    e11.grid(row=0,column=1,pady=20)
    lb12=Label(labelframe7 ,text="Age :-",font=("andalus",18)).grid(row=1,column=0,pady=20,sticky=W)
    global e12
    e12=Entry(labelframe7 ,relief="solid",bg="white",font=("andalus",16))
    e12.grid(row=1,column=1,pady=20)
    lb13=Label(labelframe7 ,text="Gender :-",font=("andalus",18)).grid(row=2,column=0,pady=20,sticky=W)
    lb14=Label(labelframe7 ,text="Class :-  ",font=("andalus",18)).grid(row=3,column=0,pady=20,sticky=W)
    lb15=Label(labelframe7 ,text="Section allocated :-  ",font=("andalus",18)).grid(row=4,column=0,pady=20,sticky=W)
    global e16
    e16=Entry(labelframe7 ,relief="solid",bg="white",font=("andalus",16))
    e16.grid(row=4,column=1,pady=20)
    lb16=Label(labelframe7 ,text="Enter ROLL NO. in the range 1 to 40 :-  ",font=("andalus",18)).grid(row=5,column=0,pady=20,sticky=W)
    global e8
    e8=Entry(labelframe7 ,width=10,relief="solid",bg="white",font=("andalus",16))
    e8.grid(row=5,column=1,pady=20,sticky=W)
    lb17=Label(labelframe7 ,text="Fees :-  ",font=("andalus",18)).grid(row=6,column=0,pady=20,sticky=W)
    global e10
    e10=Entry(labelframe7 ,width=10,relief="solid",bg="white",font=("andalus",16))
    e10.grid(row=6,column=1,pady=20,sticky=W)
    bt11=Button(top4,text="PAY FEES",activebackground="#78d6ff",padx=92,pady=28,bg="green",fg="white",command=click_confirm5,relief="groove").place(x=11,y=595)
    global clicked4
    clicked4=IntVar()
    OptionMenu(labelframe7 ,clicked4,*l).grid(row=3,column=1,pady=20,ipadx=92)
    global clicked5
    clicked5=StringVar()
    OptionMenu(labelframe7 ,clicked5,"M","F","TRANSGENDER").grid(row=2,column=1,pady=20,ipadx=58)
    global b
    b=24000
    
    


def transfer_certificate():
    root.withdraw()
    global top6
    top6=Toplevel()
    top6.geometry("1500x1000+0+0")
    labelframe8 = LabelFrame(top6, text="STUDENT",bd=10,font=("times new roman", 18))
    labelframe8.place(x=10,y=40)
    lb1=Label(labelframe8 ,text="Name :-",font=("andalus",18)).grid(row=0,column=0,pady=20,sticky=W)
    global e6
    e6=Entry(labelframe8 ,relief="solid",bg="white",font=("andalus",16))
    e6.grid(row=0,column=1,pady=20)
    lb2=Label(labelframe8 ,text="Age :-",font=("andalus",18)).grid(row=1,column=0,pady=20,sticky=W)
    global e7
    e7=Entry(labelframe8 ,relief="solid",bg="white",font=("andalus",16))
    e7.grid(row=1,column=1,pady=20)
    lb3=Label(labelframe8 ,text="Gender :-",font=("andalus",18)).grid(row=2,column=0,pady=20,sticky=W)
    lb4=Label(labelframe8 ,text="Class :-  ",font=("andalus",18)).grid(row=3,column=0,pady=20,sticky=W)
    lb5=Label(labelframe8 ,text="Section allocated :-  ",font=("andalus",18)).grid(row=4,column=0,pady=20,sticky=W)
    global e9
    e9=Entry(labelframe8 ,relief="solid",bg="white",font=("andalus",16))
    e9.grid(row=4,column=1,pady=20)
    lb7=Label(labelframe8 ,text="Enter ROLL NO.  :-  ",font=("andalus",18)).grid(row=5,column=0,pady=20,sticky=W)
    global e8
    e8=Entry(labelframe8 ,width=10,relief="solid",bg="white",font=("andalus",16))
    e8.grid(row=5,column=1,pady=20,sticky=W)
    bt1=Button(top6 ,text="DELETE",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm7,relief="groove").place(x=48,y=640)
    bt2=Button(top6 ,text="SEARCH",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm8,relief="groove").place(x=292,y=640)
    global clicked2
    clicked2=IntVar()
    OptionMenu(labelframe8 ,clicked2,*l).grid(row=3,column=1,pady=20,ipadx=92)
    global clicked3
    clicked3=StringVar()
    OptionMenu(labelframe8 ,clicked3,"M","F","TRANSGENDER").grid(row=2,column=1,pady=20,ipadx=58)
    
    
def click_confirm1():
#    try  :
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="disable")
        cursor=mycon.cursor()
        st="insert into dys values('{}','{}',{},{},'{}','{}','{}','{}',{},'{}','{})".format(str(e.get()),str(clicked1.get()),int(e1.get()),int(e5.get()),str(e19.get()),str(e3.get()),str(e4.get()),str(e20.get(),int(e22.get()),str(e21.get()),str(clicked9.get())))
        cursor.execute(st)
        mycon.commit()
        mycon.close()
'''        e3.delete(0,END)
        e.delete(0,END)
        e1.delete(0,END)
        e4.delete(0,END)
        e9.delete(0,END)
        clicked.set(" ")
        clicked1.set(" ")'''                                                
#    except :
#        messagebox.showerror("SAATHI","S\nPlease pay the fees to continue")
        
def click_confirm2():
            mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
            cursor=mycon.cursor()
            cursor.execute("update student set Name='{}' where roll_no={}".format(str(e6.get()),int(e8.get())))
            cursor.execute("update student set Age={} where roll_no={}".format(int(e7.get()),int(e8.get())))
            cursor.execute("update student set Class={} where roll_no={}".format(int(clicked2.get()),int(e8.get())))
            cursor.execute("update student set section='{}' where roll_no={}".format(str(e9.get()),int(e8.get())))
            cursor.execute("update student set gender='{}' where roll_no={}".format(str(clicked3.get()),int(e8.get())))
            mycon.commit()
            mycon.close()
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
            e9.delete(0,END)
            clicked3.set(" ")
            clicked2.set(" ")


            
def click_confirm3():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st="select*from student where roll_no={}".format(int(e8.get()))
        cursor.execute(st)
        global labelframe6
        labelframe6 = LabelFrame(top1, text="STUDENT DATABASE",bd=10,font=("times new roman", 18))
        labelframe6.place(x=710,y=40)
        tree=ttk.Treeview(labelframe6,height=34)
        tree['columns']=('Roll no','Name','Age','Class','Section','Gender','Remark by teacher','New admission fees','Fees')
        tree.column('#0',width=0,stretch=NO)
        tree.column('Roll no',width=90,minwidth=15,anchor=W)
        tree.column('Name',width=110,minwidth=15,anchor=CENTER)
        tree.column('Age',width=60,minwidth=15,anchor=CENTER)
        tree.column('Class',width=90,minwidth=15,anchor=CENTER)
        tree.column('Section',width=90,minwidth=15,anchor=CENTER)
        tree.column('Gender',width=90,minwidth=15,anchor=CENTER)
        tree.column('Remark by teacher',width=125,minwidth=15,anchor=CENTER)
        tree.column('New admission fees',width=145,minwidth=15,anchor=CENTER)
        tree.column('Fees',width=50,minwidth=15,anchor=CENTER)

        tree.heading('Roll no',text="Roll no",anchor=W)
        tree.heading('Name',text="Name",anchor=CENTER)
        tree.heading('Age',text="Age",anchor=CENTER)
        tree.heading('Class',text="Class",anchor=CENTER)
        tree.heading('Section',text="Section",anchor=CENTER)
        tree.heading('Gender',text="Gender",anchor=CENTER)
        tree.heading('Remark by teacher',text="Remark by teacher",anchor=CENTER)
        tree.heading('New admission fees',text="New admission fees",anchor=CENTER)
        tree.heading('Fees',text="Fees",anchor=CENTER)
        global data
        data=cursor.fetchall()
        j=[]
        for row in data:
            j.append(row)
        count=0
        for record in j:
            tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
            count=count+1
        tree.grid(row=0,column=0)
        mycon.close()
    except:
        messagebox.showerror("SAATHI","Please try again.\nFill integer value in the ROLL NO. section. ")

def click_confirm4():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st1="select*from student order by roll_no"
        cursor.execute(st1)
        tree=ttk.Treeview(labelframe6,height=34)
        tree['columns']=('Roll no','Name','Age','Class','Section','Gender','Remark by teacher','New admission fees','Fees')
        tree.column('#0',width=0,stretch=NO)
        tree.column('Roll no',width=90,minwidth=15,anchor=W)
        tree.column('Name',width=110,minwidth=15,anchor=CENTER)
        tree.column('Age',width=60,minwidth=15,anchor=CENTER)
        tree.column('Class',width=90,minwidth=15,anchor=CENTER)
        tree.column('Section',width=90,minwidth=15,anchor=CENTER)
        tree.column('Gender',width=90,minwidth=15,anchor=CENTER)
        tree.column('Remark by teacher',width=125,minwidth=15,anchor=CENTER)
        tree.column('New admission fees',width=145,minwidth=15,anchor=CENTER)
        tree.column('Fees',width=125,minwidth=15,anchor=CENTER)

        tree.heading('Roll no',text="Roll no",anchor=W)
        tree.heading('Name',text="Name",anchor=CENTER)
        tree.heading('Age',text="Age",anchor=CENTER)
        tree.heading('Class',text="Class",anchor=CENTER)
        tree.heading('Section',text="Section",anchor=CENTER)
        tree.heading('Gender',text="Gender",anchor=CENTER)
        tree.heading('Remark by teacher',text="Remark by teacher",anchor=CENTER)
        tree.heading('New admission fees',text="New admission fees",anchor=CENTER)
        tree.heading('Fees',text="Fees",anchor=CENTER)
        global data
        data=cursor.fetchall()
        j=[]
        for row in data:
            j.append(row)
        count=0
        for record in j:
            tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
            count=count+1
        tree.grid(row=0,column=0)
        mycon.close()
    except:
        messagebox.showwarning("SAATHI","Please fill  at least ROLL NUMBER to continue ")

def click_choice(option):
    if option==("yes"):
        top2.destroy()
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        cursor.execute("update student set Fees={} where roll_no={}".format(int(e10.get()),int(e8.get())))
        mycon.commit()
        mycon.close()
    else:
        top2.destroy()



def click_confirm5():
    try:
        if int(e10.get())==b:
            global top2
            top2=Toplevel()
            top2.geometry("400x150")
            top2.title("SAATHI")
            mylabel=Label(top2,text="Do you want to continue?",font=("andalus",18)).pack()
            mybutton=ttk.Button(top2,text="Yes",command=lambda:click_choice("yes")).place(x=110,y=60)
            mybutton1=ttk.Button(top2,text="No",command=lambda:click_choice("no")).place(x=220,y=60)
        else:
            global top3
            top3=Toplevel()
            top3.geometry("500x150")
            top3.title("SAATHI")
            mylabel=Label(top3,text="Please pay Rs.24000 as quaterly fees.",font=("andalus",18)).pack()
            mybutton=ttk.Button(top3,text="Yes",command=lambda:click_choice1("ok")).place(x=210,y=60)
    except:
        messagebox.showerror("SAATHI","ERROR!!!,Please try again.")


def click_confirm7():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st2="delete from student where roll_no={}".format(int(e8.get()))
        cursor.execute(st2)
        mycon.commit()
        mycon.close()
    except:
        messagebox.showerror("SAATHI","Record no found!!!")

def click_confirm8():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st="select*from student where roll_no={}".format(int(e8.get()))
        cursor.execute(st)
        global labelframe6
        labelframe9 = LabelFrame(top6, text="STUDENT DATABASE",bd=10,font=("times new roman", 18))
        labelframe9.place(x=710,y=40)
        tree=ttk.Treeview(labelframe9,height=34)
        tree['columns']=('Roll no','Name','Age','Class','Section','Gender','Remark by teacher','New admission fees','Fees')
        tree.column('#0',width=0,stretch=NO)
        tree.column('Roll no',width=90,minwidth=15,anchor=W)
        tree.column('Name',width=110,minwidth=15,anchor=CENTER)
        tree.column('Age',width=60,minwidth=15,anchor=CENTER)
        tree.column('Class',width=90,minwidth=15,anchor=CENTER)
        tree.column('Section',width=90,minwidth=15,anchor=CENTER)
        tree.column('Gender',width=90,minwidth=15,anchor=CENTER)
        tree.column('Remark by teacher',width=125,minwidth=15,anchor=CENTER)
        tree.column('New admission fees',width=145,minwidth=15,anchor=CENTER)
        tree.column('Fees',width=50,minwidth=15,anchor=CENTER)

        tree.heading('Roll no',text="Roll no",anchor=W)
        tree.heading('Name',text="Name",anchor=CENTER)
        tree.heading('Age',text="Age",anchor=CENTER)
        tree.heading('Class',text="Class",anchor=CENTER)
        tree.heading('Section',text="Section",anchor=CENTER)
        tree.heading('Gender',text="Gender",anchor=CENTER)
        tree.heading('Remark by teacher',text="Remark by teacher",anchor=CENTER)
        tree.heading('New admission fees',text="New admission fees",anchor=CENTER)
        tree.heading('Fees',text="Fees",anchor=CENTER)
        global data
        data=cursor.fetchall()
        j=[]
        for row in data:
            j.append(row)
        count=0
        for record in j:
            tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
            count=count+1
        tree.grid(row=0,column=0)
        mycon.close()
    except:
        messagebox.showerror("SAATHI","Please try again.\nFill integer value in the ROLL NO. section. ")
    
def newtchr():
    root.withdraw()
    global top5
    top5=Toplevel()
    top5.geometry("1500x1000+0+0")
    l20=Label(top5,text="Name :-",font=("andalus",18)).place(x=15,y=60)
    
    global e20
    e20=Entry(top5,relief="solid",bg="white",font=("andalus",16))
    e20.place(x=105,y=50,width=191,height=40)
    l21=Label(top5,text="Age :-",font=("andalus",18)).place(x=15,y=132)
    global e21
    e21=Entry(top5,relief="solid",bg="white",font=("andalus",16))
    e21.place(x=105,y=117,width=68,height=40)
    l22=Label(top5,text="Gender :-",font=("andalus",18)).place(x=11,y=203)
    l26=Label(top5,text="Subject :-",font=("andalus",18)).place(x=11,y=269)
    global e27
    e27=Entry(top5,width=10,relief="solid",bg="white",font=("andalus",16))
    e27.place(x=121,y=261,width=368,height=40)
    l23=Label(top5,text="Class allocated :-  ",font=("andalus",18)).place(x=11,y=335)
    l24=Label(top5,text="Section allocated :-  ",font=("andalus",18)).place(x=11,y=401)
    global e26
    e26=Entry(top5,width=10,relief="solid",bg="white",font=("andalus",16))
    e26.place(x=231,y=395,width=68,height=40)
    l25=Label(top5,text="Enter id :-  ",font=("andalus",18)).place(x=11,y=470)
    global e25
    e25=Entry(top5,width=10,relief="solid",bg="white",font=("andalus",16))
    e25.place(x=131,y=460,width=68,height=40)
    b1=Button(top5,text="APPLY",activebackground="#78d6ff",padx=95,pady=28,bg="green",command=click_confirm6,relief="groove").place(x=11,y=545)

    global clicked7
    clicked7=IntVar()
    OptionMenu(top5,clicked7,*l).place(x=200,y=321,width=68,height=40)
    global clicked8
    clicked8=StringVar()
    OptionMenu(top5,clicked8,"M","F","TRANSGENDER").place(x=115,y=191,width=191,height=40)
     
def click_confirm6():
    try:
        response=messagebox.askquestion("SAATHI","Please check your responses thoroughly.\nClick OK if they are correct or else go back.")
        if response=="yes" :
            mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
            cursor=mycon.cursor()
            st="insert into teacher values({},'{}',{},'{}','{}',{},'{}',{})".format(int(e25.get()),str(e20.get()),int(e21.get()),str(clicked8.get()),str(e27.get()),int(clicked7.get()),str(e26.get()),0)
            cursor.execute(st)
            mycon.commit()
            mycon.close()
            e25.delete(0,END)
            e20.delete(0,END)
            e21.delete(0,END)
            e27.delete(0,END)
            e26.delete(0,END)
            clicked8.set(" ")
            clicked7.set(" ")
            message='''                                                                 IMPORTANT POINTS FOR NEW ADMIT'S:


    1.After completing the induction formalities you will be able to access the teacher login section in order to get your detail's as \nregistered with the school.
    2.Username=AD@34 , Password=AJ#23 all character's are case sensitive.
    3.Please do not share these with anyone as it will result in your harm only.It will also prompt strict action from school authorities.
    4.Please limit your access to teacher section of the main page only.DO NOT TRESSPASS TO OTHER SECTIONS.
    5.Other details will be shared with you in due course of time.

                                                                                                            THANK YOU
                                                                                                            -SAATHI'''
            text_box=Text(top5,font=("Monotype Corsiva",16))
            text_box.place(x=550,y=70,width=1015,height=610)
            text_box.insert('end',message)
            text_box.config(state='disabled')
        else:
            pass
    except:
        messagebox.showerror("SAATHI","ERROR!!!\nIncorrect detail's filled.\nPlease try again. ")

def click_confirm9():
    mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
    cursor=mycon.cursor()
    cursor.execute("update teacher set Name='{}' where id={}".format(str(e20.get()),int(e25.get())))
    cursor.execute("update teacher set Age={} where id={}".format(int(e21.get()),int(e25.get())))
    cursor.execute("update teacher set Gender='{}' where id={}".format(str(clicked8.get()),int(e25.get())))
    cursor.execute("update teacher set subject='{}' where id={}".format(str(e27.get()),int(e25.get())))
    cursor.execute("update teacher set class_allocated={} where id={}".format(int(clicked7.get()),int(e25.get())))
    cursor.execute("update teacher set section_allocated='{}' where id={}".format(str(e26.get()),int(e25.get())))
    cursor.execute("update teacher set salary={} where id={}".format(int(e28.get()),int(e25.get())))
    mycon.commit()
    mycon.close()
    e20.delete(0,END)
    e25.delete(0,END)
    e27.delete(0,END)
    e28.delete(0,END)
    e21.delete(0,END)
    clicked7.set(" ")
    clicked8.set(" ")

def click_confirm10():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st="select*from teacher where id={}".format(int(e25.get()))
        cursor.execute(st)
        global labelframe10
        labelframe10 = LabelFrame(top5, text="TEACHER DATABASE",bd=10,font=("times new roman", 18))
        labelframe10.place(x=710,y=40)
        tree=ttk.Treeview(labelframe10,height=34)
        tree['columns']=('Id','Name','Age','Gender','Subject','Class allocated','Section allocated','Salary')
        tree.column('#0',width=0,stretch=NO)
        tree.column('Id',width=90,minwidth=15,anchor=W)
        tree.column('Name',width=110,minwidth=15,anchor=CENTER)
        tree.column('Age',width=60,minwidth=15,anchor=CENTER)
        tree.column('Gender',width=90,minwidth=15,anchor=CENTER)
        tree.column('Subject',width=90,minwidth=15,anchor=CENTER)
        tree.column('Class allocated',width=125,minwidth=15,anchor=CENTER)
        tree.column('Section allocated',width=125,minwidth=15,anchor=CENTER)
        tree.column('Salary',width=90,minwidth=15,anchor=CENTER)

        tree.heading('Id',text="Id",anchor=W)
        tree.heading('Name',text="Name",anchor=CENTER)
        tree.heading('Age',text="Age",anchor=CENTER)
        tree.heading('Gender',text="Gender",anchor=CENTER)
        tree.heading('Subject',text="Subject",anchor=CENTER)
        tree.heading('Class allocated',text="Class allocated",anchor=CENTER)
        tree.heading('Section allocated',text="Section allocated",anchor=CENTER)
        tree.heading('Salary',text="Salary",anchor=CENTER)
        global data1
        data1=cursor.fetchall()
        j=[]
        for row in data1:
            j.append(row)
        count=0
        for record in j:
            tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
            count=count+1
        tree.grid(row=0,column=0)
        mycon.close()
    except:
        messagebox.showerror("SAATHI","Please try again.\nFill integer value in the ROLL NO. section. ")



def click_confirm11():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st1="select*from teacher order by id"
        cursor.execute(st1)
        tree=ttk.Treeview(labelframe10,height=34)
        tree['columns']=('Id','Name','Age','Gender','Subject','Class allocated','Section allocated','Salary')
        tree.column('#0',width=0,stretch=NO)
        tree.column('Id',width=90,minwidth=15,anchor=W)
        tree.column('Name',width=110,minwidth=15,anchor=CENTER)
        tree.column('Age',width=60,minwidth=15,anchor=CENTER)
        tree.column('Gender',width=90,minwidth=15,anchor=CENTER)
        tree.column('Subject',width=90,minwidth=15,anchor=CENTER)
        tree.column('Class allocated',width=125,minwidth=15,anchor=CENTER)
        tree.column('Section allocated',width=125,minwidth=15,anchor=CENTER)
        tree.column('Salary',width=90,minwidth=15,anchor=CENTER)

        tree.heading('Id',text="Id",anchor=W)
        tree.heading('Name',text="Name",anchor=CENTER)
        tree.heading('Age',text="Age",anchor=CENTER)
        tree.heading('Gender',text="Gender",anchor=CENTER)
        tree.heading('Subject',text="Subject",anchor=CENTER)
        tree.heading('Class allocated',text="Class allocated",anchor=CENTER)
        tree.heading('Section allocated',text="Section allocated",anchor=CENTER)
        tree.heading('Salary',text="Salary",anchor=CENTER)
        global data1
        data1=cursor.fetchall()
        j=[]
        for row in data1:
            j.append(row)
        count=0
        for record in j:
            tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
            count=count+1
        tree.grid(row=0,column=0)
        mycon.close()
    except:
        messagebox.showwarning("SAATHI","Please fill  Id to continue ")
def click_confirm12():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st2="delete from teacher where id={}".format(int(e25.get()))
        cursor.execute(st2)
        mycon.commit()
        mycon.close()
    except:
        messagebox.showerror("SAATHI","Record no found!!!")
    
def click_confirm13():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st="select*from teacher where id={}".format(int(e25.get()))
        cursor.execute(st)
        global labelframe13
        labelframe13 = LabelFrame(top7, text="TEACHER DATABASE",bd=10,font=("times new roman", 18))
        labelframe13.place(x=710,y=40)
        tree=ttk.Treeview(labelframe13,height=34)
        tree['columns']=('Id','Name','Age','Gender','Subject','Class allocated','Section allocated','Salary')
        tree.column('#0',width=0,stretch=NO)
        tree.column('Id',width=90,minwidth=15,anchor=W)
        tree.column('Name',width=110,minwidth=15,anchor=CENTER)
        tree.column('Age',width=60,minwidth=15,anchor=CENTER)
        tree.column('Gender',width=90,minwidth=15,anchor=CENTER)
        tree.column('Subject',width=90,minwidth=15,anchor=CENTER)
        tree.column('Class allocated',width=125,minwidth=15,anchor=CENTER)
        tree.column('Section allocated',width=125,minwidth=15,anchor=CENTER)
        tree.column('Salary',width=90,minwidth=15,anchor=CENTER)

        tree.heading('Id',text="Id",anchor=W)
        tree.heading('Name',text="Name",anchor=CENTER)
        tree.heading('Age',text="Age",anchor=CENTER)
        tree.heading('Gender',text="Gender",anchor=CENTER)
        tree.heading('Subject',text="Subject",anchor=CENTER)
        tree.heading('Class allocated',text="Class allocated",anchor=CENTER)
        tree.heading('Section allocated',text="Section allocated",anchor=CENTER)
        tree.heading('Salary',text="Salary",anchor=CENTER)
        global data1
        data1=cursor.fetchall()
        j=[]
        for row in data1:
            j.append(row)
        count=0
        for record in j:
            tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
            count=count+1
        tree.grid(row=0,column=0)
        mycon.close()
    except:
        messagebox.showerror("SAATHI","Please try again.\nFill integer value in the ROLL NO. section. ")
    
def tchrlogin():
    global root2
    root2=Toplevel()
    root2.geometry("690x350")
    labelframe5 = LabelFrame(root2, text="LOGIN WINDOW",font=("impact",22),bg="green",relief="ridge",bd=30,padx=25,pady=25)
    labelframe5.place(x=120,y=40)
    lbl1=Label(labelframe5 ,text="Username:-",font=("andalus",16),bg="green",fg="white").grid(row=0,column=0)
    lbl2=Label(labelframe5 ,text="Password:-",font=("andalus",16),bg="green",fg="white").grid(row=1,column=0)
    lbl3=Label(root2 ,text="You need to enter ID of a teacher in order access all teacher database  ",font=("monotype corsiva",17),bg="black",fg="white").place(x=10,y=290)
    global en3
    en3=Entry(labelframe5,width=12,font=("andalus",16),relief="solid",bg="white",show="#")
    en3.grid(row=0,column=1)
    global en4
    en4=Entry(labelframe5,width=12,font=("andalus",16),relief="solid",bg="white",show="*")
    en4.grid(row=1,column=1)
    btn1=Button(labelframe5 ,text="LOGIN",font=("andalus",16),bg="green",fg="white",command=loginwin1).grid(row=2,column=0)
    btn2=Button(labelframe5 ,text="RESET",font=("andalus",16),bg="green",fg="white",command=resetpw1).grid(row=2,column=1)
    btn3=Button(labelframe5 ,text="EXIT",font=("andalus",16),bg="green",fg="white",command=root2.destroy).grid(row=2,column=2)

def resetpw1():
    global usn
    usn=en3.get()
    global pwd
    pwd=en4.get()

def loginwin1():
    if pwd==str(en4.get()) and usn==str(en3.get()):
        tchrlogin1()
    else:
        messagebox.showerror("SAATHI","Incorrect username or password!!!\n please try again")


def tchrlogin1():
    root.withdraw()
    global top5
    top5=Toplevel()
    top5.geometry("1500x1000+0+0")
    labelframe11 = LabelFrame(top5, text="TEACHER",bd=10,font=("times new roman", 18))
    labelframe11.place(x=10,y=40)
    l20=Label(labelframe11,text="Name :-",font=("andalus",18)).grid(row=0,column=0,pady=20,sticky=W)
    
    global e20
    e20=Entry(labelframe11,relief="solid",bg="white",font=("andalus",16))
    e20.grid(row=0,column=1,pady=20)
    l21=Label(labelframe11,text="Age :-",font=("andalus",18)).grid(row=1,column=0,pady=20,sticky=W)
    global e21
    e21=Entry(labelframe11,relief="solid",bg="white",font=("andalus",16))
    e21.grid(row=1,column=1,pady=20)
    l22=Label(labelframe11,text="Gender :-",font=("andalus",18)).grid(row=2,column=0,pady=20,sticky=W)
    l26=Label(labelframe11,text="Subject :-",font=("andalus",18)).grid(row=3,column=0,pady=20,sticky=W)
    global e27
    e27=Entry(labelframe11,width=10,relief="solid",bg="white",font=("andalus",16))
    e27.grid(row=3,column=1,pady=20)
    l23=Label(labelframe11,text="Class allocated :-  ",font=("andalus",18)).grid(row=4,column=0,pady=20,sticky=W)
    l24=Label(labelframe11,text="Section allocated :-  ",font=("andalus",18)).grid(row=5,column=0,pady=20,sticky=W)
    global e26
    e26=Entry(labelframe11,width=10,relief="solid",bg="white",font=("andalus",16))
    e26.grid(row=5,column=1,pady=20)
    l25=Label(labelframe11,text="Enter id :-  ",font=("andalus",18)).grid(row=6,column=0,pady=20,sticky=W)
    global e25
    e25=Entry(labelframe11,width=10,relief="solid",bg="white",font=("andalus",16))
    e25.grid(row=6,column=1,pady=20,sticky=W)
    l26=Label(labelframe11,text="Salary :-",font=("andalus",18)).grid(row=7,column=0,pady=20,sticky=W)
    global e28
    e28=Entry(labelframe11,width=13,relief="solid",bg="white",font=("andalus",16))
    e28.grid(row=7,column=1,pady=20)
    b1=Button(top5,text="UPDATE",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm9,relief="groove").place(x=11,y=655)
    bt2=Button(top5 ,text="SEARCH",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm10,relief="groove").place(x=222,y=655)
    bt3=Button(top5 ,text="DISPLAY ALL",activebackground="#78d6ff",padx=82,pady=28,bg="green",fg="white",command=click_confirm11,relief="groove").place(x=100,y=734)
    global clicked7
    clicked7=IntVar()
    OptionMenu(labelframe11,clicked7,*l).grid(row=4,column=1,pady=20)
    global clicked8
    clicked8=StringVar()
    OptionMenu(labelframe11,clicked8,"M","F","TRANSGENDER").grid(row=2,column=1,pady=20)

def tchrtrnsfr():
    root.withdraw()
    global top7
    top7=Toplevel()
    top7.geometry("1500x1000+0+0")
    labelframe12 = LabelFrame(top7, text="STUDENT",bd=10,font=("times new roman", 18))
    labelframe12.place(x=10,y=40)
    l20=Label(labelframe12,text="Name :-",font=("andalus",18)).grid(row=0,column=0,pady=20,sticky=W)
    
    global e20
    e20=Entry(labelframe12,relief="solid",bg="white",font=("andalus",16))
    e20.grid(row=0,column=1,pady=20)
    l21=Label(labelframe12,text="Age :-",font=("andalus",18)).grid(row=1,column=0,pady=20,sticky=W)
    global e21
    e21=Entry(labelframe12,relief="solid",bg="white",font=("andalus",16))
    e21.grid(row=1,column=1,pady=20)
    l22=Label(labelframe12,text="Gender :-",font=("andalus",18)).grid(row=2,column=0,pady=20,sticky=W)
    l26=Label(labelframe12,text="Subject :-",font=("andalus",18)).grid(row=3,column=0,pady=20,sticky=W)
    global e27
    e27=Entry(labelframe12,width=10,relief="solid",bg="white",font=("andalus",16))
    e27.grid(row=3,column=1,pady=20)
    l23=Label(labelframe12,text="Class allocated :-  ",font=("andalus",18)).grid(row=4,column=0,pady=20,sticky=W)
    l24=Label(labelframe12,text="Section allocated :-  ",font=("andalus",18)).grid(row=5,column=0,pady=20,sticky=W)
    global e26
    e26=Entry(labelframe12,width=10,relief="solid",bg="white",font=("andalus",16))
    e26.grid(row=5,column=1,pady=20)
    l25=Label(labelframe12,text="Enter id :-  ",font=("andalus",18)).grid(row=6,column=0,pady=20,sticky=W)
    global e25
    e25=Entry(labelframe12,width=10,relief="solid",bg="white",font=("andalus",16))
    e25.grid(row=6,column=1,pady=20,sticky=W)
    b1=Button(top7,text="DELETE",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm12,relief="groove").place(x=11,y=655)
    bt2=Button(top7 ,text="SEARCH",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm13,relief="groove").place(x=222,y=655)
    global clicked7
    clicked7=IntVar()
    OptionMenu(labelframe12,clicked7,*l).grid(row=4,column=1,pady=20)
    global clicked8
    clicked8=StringVar()
    OptionMenu(labelframe12,clicked8,"M","F","TRANSGENDER").grid(row=2,column=1,pady=20)

def salarylogin():
    global root3
    root3=Toplevel()
    root3.geometry("590x350")
    labelframe14 = LabelFrame(root3, text="LOGIN WINDOW",font=("impact",22),bg="green",relief="ridge",bd=30,padx=25,pady=25)
    labelframe14.place(x=120,y=40)
    lbl1=Label(labelframe14 ,text="Username:-",font=("andalus",16),bg="green",fg="white").grid(row=0,column=0)
    lbl2=Label(labelframe14 ,text="Password:-",font=("andalus",16),bg="green",fg="white").grid(row=1,column=0)
    global en5
    en5=Entry(labelframe14,width=12,font=("andalus",16),relief="solid",bg="white",show="#")
    en5.grid(row=0,column=1)
    global en6
    en6=Entry(labelframe14,width=12,font=("andalus",16),relief="solid",bg="white",show="*")
    en6.grid(row=1,column=1)
    btn1=Button(labelframe14 ,text="LOGIN",font=("andalus",16),bg="green",fg="white",command=loginwin2).grid(row=2,column=0)
    btn2=Button(labelframe14 ,text="RESET",font=("andalus",16),bg="green",fg="white",command=resetpw2).grid(row=2,column=1)
    btn3=Button(labelframe14 ,text="EXIT",font=("andalus",16),bg="green",fg="white",command=root3.destroy).grid(row=2,column=2)
    
    
def resetpw2():
    global usnm
    usnm=en5.get()
    global pswd
    pswd=en6.get()

def loginwin2():
    if pswd==str(en5.get()) and usnm==str(en6.get()):
        salarylogin1()
    else:
        messagebox.showerror("SAATHI","Incorrect username or password!!!\n please try again")

def salarylogin1():
    root.withdraw()
    global top8
    top8=Toplevel()
    top8.geometry("1500x1000+0+0")
    labelframe15 = LabelFrame(top8, text="SALARY",bd=10,font=("times new roman", 18))
    labelframe15.place(x=10,y=40)
    l30=Label(labelframe15,text="Teacher Id",font=("andalus",18)).grid(row=0,column=0,pady=20,sticky=W)
    global e30
    e30=Entry(labelframe15,relief="solid",bg="white",font=("andalus",16))
    e30.grid(row=0,column=1,pady=20)
    l31=Label(labelframe15,text="Employee Id :-",font=("andalus",18)).grid(row=1,column=0,pady=20,sticky=W)
    global e31
    e31=Entry(labelframe15,relief="solid",bg="white",font=("andalus",16))
    e31.grid(row=1,column=1,pady=20)
    bt2=Button(top8 ,text="SEARCH",activebackground="#78d6ff",padx=95,pady=28,bg="green",fg="white",command=click_confirm14,relief="groove").place(x=10,y=255)
    
    
def click_confirm14():
    try:
        mycon=con.connect(host="localhost",user="root",passwd="jitu75",database="studentdetail")
        cursor=mycon.cursor()
        st="select*from teacher where id={}".format(int(e30.get()))
        cursor.execute(st)
        global labelframe16
        labelframe16 = LabelFrame(top8, text="SALARY DATABASE",bd=10,font=("times new roman", 18))
        labelframe16.place(x=710,y=40)
        tree=ttk.Treeview(labelframe16,height=30)
        tree['columns']=('Id','Name','Salary')
        tree.column('#0',width=0,stretch=NO)
        tree.column('Id',width=90,minwidth=15,anchor=W)
        tree.column('Name',width=110,minwidth=15,anchor=CENTER)
        tree.column('Salary',width=90,minwidth=15,anchor=CENTER)

        tree.heading('Id',text="Id",anchor=W)
        tree.heading('Name',text="Name",anchor=CENTER)
        tree.heading('Salary',text="Salary",anchor=CENTER)
        global data3
        data3=cursor.fetchall()
        j=[]
        for row in data3:
            j.append(row)
        count=0
        for record in j:
            tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[7]))
            count=count+1
        tree.grid(row=0,column=0)
        mycon.close()
    except:
        messagebox.showerror("SAATHI","Please try again.\nFill integer value in the ID section. ")

label1=Label(root,text="SATHI",font=("times new roman", 35),bg="Black",fg="White").pack(side=TOP,fill=X)
labelframe = LabelFrame(root, text="NEW USER",bd=10,font=("times new roman", 18),bg="blue",fg="white")
labelframe.place(x=610,y=80)
button1=Button(labelframe,text="REGISTER",command=newadm,padx=78,pady=50,bg="green",fg="white").pack(padx=20,pady=20)
#button2=Button(labelframe,text="",command=transfer_certificate,padx=62,pady=50,bg="green",fg="white").pack(padx=20,pady=20)
button3=Button(labelframe,text="LOGIN",command=stdlogin,padx=81,pady=55,bg="green",fg="white").pack(padx=20,pady=20)
#button4=Button(labelframe,text="",command=feepay,padx=88,pady=55,bg="green",fg="white").pack(padx=20,pady=20)

'''labelframe1 = LabelFrame(root, text="TEACHER",bd=10,font=("times new roman", 18),bg="blue",fg="white")
labelframe1.place(x=610,y=80)
button5=Button(labelframe1,text="NEW TEACHER",command=newtchr,padx=85,pady=50,bg="green",fg="white").pack(padx=20,pady=20)
button6=Button(labelframe1,text="TRANSFER CERTIFICATE",command=tchrtrnsfr,padx=62,pady=50,bg="green",fg="white").pack(padx=20,pady=20)
button7=Button(labelframe1,text="TEACHER LOGIN",command=tchrlogin,padx=81,pady=55,bg="green",fg="white").pack(padx=20,pady=20)

labelframe2 = LabelFrame(root, text="ADMIN",bd=10,font=("times new roman", 18),bg="blue",fg="white")
labelframe2.place(x=1178,y=80)
button5=Button(labelframe2,text="ADMINISTRATOR LOGIN",padx=78,pady=50,bg="green",fg="white").pack(padx=20,pady=20)
button7=Button(labelframe2,text="STUDENT DETAILS",padx=94,pady=55,command=stdlogin,bg="green",fg="white").pack(padx=20,pady=20)
button8=Button(labelframe2,text="TEACHER DETAILS",padx=93,pady=55,command=tchrlogin,bg="green",fg="white").pack(padx=20,pady=20)
button9=Button(labelframe2,text="SALARY DETAILS",padx=98,pady=55,command=salarylogin,bg="green",fg="white").pack(padx=20,pady=20)
'''
root.mainloop()
