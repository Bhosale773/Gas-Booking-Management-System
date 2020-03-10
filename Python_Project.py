from tkinter import *
import random
from datetime import *
import mysql.connector as db
from PIL import ImageTk, Image
   
def state(var,b9,b10):
    global x
    x=var.get()
    if x==1:
        b9.config(state='normal')
        b10.config(state='disabled')
    elif x==2:
        b9.config(state='disabled')
        b10.config(state='normal')
           
def buttonClick(root,c,val,e1=None,e2=None,e3=None,e4=None,e5=None,e6=None):
    global n,cons,mob,u,p,f,record,ref,current_date,pay,bd1
    if(val==1):
        c.destroy()
        Login(root)
    elif(val==3):
        c.destroy()
        f=1
        Register(root)
    elif(val==2):
        c.destroy()
        Feedback(root)
    elif(val==4):
        u=e1.get()
        p=e2.get()
        conn=db.connect(host='localhost',user='root',password='',database="python_project")
        cursor=conn.cursor()
        cursor.execute("select * from Registration_Details where Username = '%s'"%(u))
        record=cursor.fetchall()
        conn.commit()
        fnt = ('Times', 20, 'bold')
        l1=Label(c, text="USERNAME OR PASSWORD SHOULD NOT BE NULL       ", font=fnt, fg='red')
        l2=Label(c, text="PASSWORD SHOULD BE OF MINIMUM 8 CHARACTERS", font=fnt, fg='red')
        l3=Label(c, text="INVALID USERNAME OR PASSWORD\t\t\t", font=fnt, fg='red')  
        if(len(u)==0 or len(p)==0):
            l1.place(x=200,y=390)
        elif len(p)>0 and len(p)<8:
            l2.place(x=200,y=390)
        elif record==[]:
            l3.place(x=200,y=390)
        elif record[0][4]!=u or record[0][5]!=p:
            l3.place(x=200,y=390)
        else:
            c.destroy()
            Book(root)
    elif(val==5):
        f=0
        c.destroy()
        Register(root)
    elif(val==6):
        n=e1.get()
        cons=e2.get()
        mob=e3.get()
        u=e4.get()
        p=e5.get()
        confirm=e6.get()
        conn=db.connect(host='localhost',user='root',password='',database="python_project")
        cursor=conn.cursor()
        cursor.execute("select * from Registration_Details where Username = '%s'"%(u))
        record2=cursor.fetchall()
        cursor.execute("select * from Registration_Details where Password = '%s'"%(p))
        record3=cursor.fetchall()
        cursor.execute("select * from Registration_Details where Cons_No = '%s'"%(cons))
        record4=cursor.fetchall()
        cursor.execute("select * from Registration_Details where Mobile_No = '%s'"%(mob))
        record5=cursor.fetchall()
        conn.commit()
        fnt = ('Times', 20, 'bold')
        l1=Label(c, text="ALL FIELDS SHOULD BE COMPULSORY FILLED                            ", font=fnt, fg='red')
        l2=Label(c, text="INVALID CONSUMER NUMBER ( 12 DIGITS REUIRED )                     ", font=fnt, fg='red')
        l3=Label(c, text="INVALID MOBILE NUMBER                                                    ", font=fnt, fg='red')
        l4=Label(c, text="PASSWORD FIELDS NOT MATCHED                                       ", font=fnt, fg='red')
        l5=Label(c, text="PASSWORD SHOULD BE OF MINIMUM 8 CHARACTERS                        ", font=fnt, fg='red')
        l6=Label(c, text="YOU HAVE REGISTERED SUCCESSFULLY BACK TO LOGIN PAGE               ", font=fnt, fg='red')
        l7=Label(c, text="USERNAME OR PASSWORD IS ALREADY TAKEN\t\t\t", font=fnt, fg='red')
        l8=Label(c, text="CONSUMER NUMBER EXISTS ALREADY\t\t\t", font=fnt, fg='red')
        l9=Label(c, text="MOBILE NUMBER EXISTS ALREADY\t\t\t", font=fnt, fg='red')
        if(len(n)==0 or len(cons)==0 or len(mob)==0 or len(u)==0 or len(p)==0 or len(confirm)==0):
            l1.place(x=230,y=600)
        elif(len(cons)!=12):
            l2.place(x=230,y=600)
        elif(len(mob)!=10):
            l3.place(x=230,y=600)
        elif(len(p)<8 or len(confirm)<8):
            l5.place(x=230,y=600)
        elif(p!=confirm):
            l4.place(x=230,y=600)
        elif(record2==[] and record3==[] and record4==[] and record5==[]):
            conn=db.connect(host='localhost',user='root',password='',database="python_project")
            cursor=conn.cursor()
            s="insert into Registration_Details(Name, Cons_No, Mobile_No, Username, Password) values('%s','%s','%s','%s','%s')"
            args=(n,cons,mob,u,p)
            cursor.execute(s % args)
            conn.commit()
            l6.place(x=230,y=600)
        elif(record2!=[] or record3!=[]):
            l7.place(x=230,y=600)
        elif(record4!=[]):
            l8.place(x=230,y=600)
        elif(record5!=[]):
            l9.place(x=230,y=600)          
    elif(val==7):
        if f==0:
            c.destroy()
            Login(root)
        elif f==1:
            c.destroy()
            f=0
            Welcome(root)
    elif(val==8):
        c.destroy()
        Welcome(root)
    elif(val==9):
        conn=db.connect(host='localhost',user='root',password='',database="python_project")
        cursor=conn.cursor()
        cursor.execute("select * from Booking_History where Consumer_No = '%s'"%(record[0][2]))
        record1=cursor.fetchall()
        conn.commit()
        if record1!=[]:
            bd=record1[0][4]
            bd1=bd
            bd=datetime.strptime(bd,'%d-%m-%Y')
            bd = bd + timedelta(days=30)
            cd=date.today()
            cd=cd.strftime("%d-%m-%Y")
            cd=datetime.strptime(cd,'%d-%m-%Y')
            if bd<cd:
                c.destroy()
                Confirm(root)
            else:
                c.destroy()
                Popup(root)
        else:
            c.destroy()
            Confirm(root)     
    elif(val==10):
        conn=db.connect(host='localhost',user='root',password='',database="python_project")
        cursor=conn.cursor()
        cursor.execute("select * from Booking_History where Consumer_No = '%s'"%(record[0][2]))
        record1=cursor.fetchall()
        conn.commit()
        if record1!=[]:
            bd=record1[0][4]
            bd1=bd
            bd=datetime.strptime(bd,'%d-%m-%Y')
            bd = bd + timedelta(days=30)
            cd=date.today()
            cd=cd.strftime("%d-%m-%Y")
            cd=datetime.strptime(cd,'%d-%m-%Y')
            if bd<cd:
                c.destroy()
                Pay(root)
            else:
                c.destroy()
                Popup(root)
        else:
            c.destroy()
            Pay(root)
    elif(val==11):
        c.destroy()
        Login(root)
    elif(val==12):
        conn=db.connect(host='localhost',user='root',password='',database="python_project")
        cursor=conn.cursor()
        s="insert into Booking_History(Name, Consumer_No, Reference_No, Booking_Date, Payment_Method) values('%s','%s','%s','%s','%s')"
        args=(record[0][1],record[0][2],ref,current_date,pay)
        cursor.execute(s % args)
        conn.commit()
        c.destroy()
        Logout(root)
    elif(val==13):
        atm=e1.get()
        cvv=e2.get()
        bank=e3.get()
        conn=db.connect(host='localhost',user='root',password='',database="python_project")
        cursor=conn.cursor()
        cursor.execute("select * from Bank_Details where Bank_Name = '%s' and ATM_Card_No = '%s' and CVV = '%s'" % (bank,atm,cvv))
        rec=cursor.fetchall()
        conn.commit()
        fnt = ('Times', 20, 'bold')
        l1=Label(c, text="\tINVALID CREDENTIALS\t\t   ", font=fnt, fg='red')
        l2=Label(c, text="\tTRANSACTION SUCCESSFULL\t\t   ", font=fnt, fg='red')
        if rec==[]:
            l1.place(x=230,y=550)
        else:
            e4.config(state='disabled')
            e5.config(state='normal')
            e6.config(state='disabled')
            l2.place(x=230,y=550)       
    elif(val==14):
        c.destroy()
        Confirm(root)
    elif(val==15):
        c.destroy()
        Book(root)
    elif(val==16):
        fb=e1.get("1.0","end-1c")
        conn=db.connect(host='localhost',user='root',password='',database="python_project")
        cursor=conn.cursor()
        s="insert into Feedback(Feedback) values('%s')"
        args=(fb)
        cursor.execute(s % args)
        conn.commit()
        fnt = ('Times', 20, 'bold')
        l1=Label(c, text="THANK YOU FOR YOUR VALUABLE FEEDBACK . . .", font=fnt, fg='red')
        l1.place(x=300,y=670)
    elif(val==17):
        c.destroy()
        Welcome(root)
    elif(val==18):
        c.destroy()
        Welcome(root)
    elif(val==19):
        c.destroy()
        Book(root)

def Welcome(root):
    root.title("Welcome Screen")
    root.geometry("1920x1080")
    c = Canvas(root, bg='cyan', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("welcome.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    c.create_polygon(430, 50, 1070, 50, 1100, 80, 1100, 200, 400, 200, 400, 80, width=3, fill='red', outline='green')
    c.create_polygon(1100, 150, 1230, 150, 1150, 200, 1230, 250, 1050, 250, width=3, fill='green', outline='red')
    c.create_polygon(400, 150, 270, 150, 350, 200, 270, 250, 450, 250, width=3, fill='green', outline='red')
    fnt = ('Times', 38, 'bold')
    c.create_text(730, 90, text="WELCOME TO", font=fnt, fill='white', activefill='indigo')
    c.create_text(750, 150, text="BHARAT GAS SERVICE", font=fnt, fill='white', activefill='indigo')
    c.create_oval(190, 350, 490, 550, width=5, fill='orange', outline='red')
    c.create_oval(1030, 350, 1330, 550, width=5, fill='orange', outline='red')
    c.create_oval(620, 530, 920, 730, width=5, fill='orange', outline='red')
    fnt = ('Times', 34, 'bold')
    c.create_text(340, 430, text="     BOOK \nCYLINDER", font=fnt, fill='blue', activefill='green')
    c.create_text(1180, 430, text="      GIVE \nFEEDBACK", font=fnt, fill='blue', activefill='green')
    fnt = ('Times', 28, 'bold')
    c.create_text(770, 610, text="     NEW USER \nREGISTRATION", font=fnt, fill='blue', activefill='green')
    fnt = ('Times', 17, 'bold')
    b1=Button(c, text="CLICK", font=fnt, bg='yellow', fg='black', activeforeground='red', activebackground='green', command= lambda: buttonClick(root,c,1))
    b2=Button(c, text="CLICK", font=fnt, bg='yellow', fg='black', activeforeground='red', activebackground='green',command= lambda: buttonClick(root,c,2))
    b3=Button(c, text="CLICK", font=fnt, bg='yellow', fg='black', activeforeground='red', activebackground='green',command= lambda: buttonClick(root,c,3))
    b1.place(x=300, y=490, width=100, height=30)
    b2.place(x=1140, y=490, width=100, height=30)
    b3.place(x=730, y=670, width=100, height=30)   
    root.mainloop()

def Login(root):
    root.title("Login Screen")
    root.geometry("1920x1080")
    c = Canvas(root, bg='cyan', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("login.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    fnt = ('Times', 28, 'bold','underline')
    c.create_text(360, 100, text="FIRST LOGIN HERE . . .", font=fnt, fill='BLACK')
    fnt = ('Times', 24, 'bold')
    c.create_text(300, 200, text="USERNAME :", font=fnt, fill='white')
    c.create_text(300, 250, text="PASSWORD :", font=fnt, fill='white')
    e1=Entry(c, width=18, bg='LightGreen', fg='black', font=('Times', 20))
    e2=Entry(c, width=18, bg='LightGreen', fg='black', font=('Times', 20), show="*")
    e1.place(x=420, y=185)
    e2.place(x=420, y=235)
    fnt = ('Times', 18, 'bold')
    b4=Button(c, text="LOGIN", font=fnt, command= lambda: buttonClick(root,c,4,e1,e2))
    b5=Button(c, text="NEW USER ?", font=fnt, command= lambda: buttonClick(root,c,5))
    b8=Button(c, text="BACK", font=fnt, command= lambda: buttonClick(root,c,8))
    b8.place(x=1250, y=50, width=170, height=50)
    b4.place(x=200, y=300, width=200, height=50)
    b5.place(x=450, y=300, width=200, height=50)   
    root.mainloop()
    
def Register(root):
    root.title("Sign Up Screen")
    root.geometry("1920x1080")
    c = Canvas(root, bg='cyan', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("register.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    fnt = ('Times', 28, 'bold','underline')
    c.create_text(600, 100, text="FOLLOW STEPS TO REGISTER YOURSELF . . .", font=fnt, fill='BLACK')
    fnt = ('Times', 21, 'bold')
    c.create_text(280, 200, text="NAME :", font=fnt, fill='white')
    c.create_text(400, 250, text="12 DIGIT CONSUMER NO :", font=fnt, fill='white')
    c.create_text(318, 305, text="MOBILE NO :", font=fnt, fill='white')
    c.create_text(377, 360, text="CREATE USERNAME :", font=fnt, fill='white')
    c.create_text(375, 418, text="CREATE PASSWORD :", font=fnt, fill='white')
    c.create_text(385, 470, text="CONFIRM PASSWORD :", font=fnt, fill='white')
    e1=Entry(c, width=22, bg='LightGreen', fg='black', font=('Times', 20))
    e2=Entry(c, width=22, bg='LightGreen', fg='black', font=('Times', 20))
    e3=Entry(c, width=22, bg='LightGreen', fg='black', font=('Times', 20))
    e4=Entry(c, width=22, bg='LightGreen', fg='black', font=('Times', 20))
    e5=Entry(c, width=22, bg='LightGreen', fg='black', font=('Times', 20), show='*')
    e6=Entry(c, width=22, bg='LightGreen', fg='black', font=('Times', 20), show='*')
    e1.place(x=600, y=185)
    e2.place(x=600, y=235)
    e3.place(x=600, y=290)
    e4.place(x=600, y=345)
    e5.place(x=600, y=405)
    e6.place(x=600, y=455)
    fnt = ('Times', 18, 'bold')
    b6=Button(c, text="SUBMIT", font=fnt, command= lambda: buttonClick(root,c,6,e1,e2,e3,e4,e5,e6))
    b6.place(x=480, y=530, width=200, height=40)
    b7=Button(c, text="BACK", font=fnt, command= lambda: buttonClick(root,c,7))
    b7.place(x=1250, y=50, width=170, height=50)
    root.mainloop()

def Book(root):
    root.title("Book Your Cylinder")
    root.geometry("1920x1080")
    c = Canvas(root, bg='cyan', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("book.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    fnt = ('Times', 26, 'bold','underline')
    c.create_text(350, 50, text="HELLO  Mr/Mrs  "+record[0][1]+" ,", font=fnt, fill='BLACK')
    m=Message(c, text="\n    VERIFY YOUR DETAILS :-\n\n    * Your Order : LPG Refill ( Domestic )\n\n    * Distributor : Bharat Gas Service\n\n    * Consumer Number : "+record[0][2]+"\n\n    * Registered Mobile Number : "+record[0][3]+"\n\n    [ Refill Boook SMS will be send to Registered Mobile Number ]\n", width=900, font=('Roman', 20, 'bold'), fg='white', bg='gray')
    m.place(x=180,y=120)
    fnt = ('Times', 22, 'bold')
    c.create_text(410, 600, text="Payment Option : ", font=fnt, fill='black')
    b9=Button(c, text="BOOK NOW", font=fnt, state = DISABLED, command= lambda: buttonClick(root,c,9))
    b9.place(x=310, y=690, width=200, height=40)
    b10=Button(c, text="PAY NOW", font=fnt, state = DISABLED, command= lambda: buttonClick(root,c,10))
    b10.place(x=590, y=690, width=200, height=40)
    b11=Button(c, text="BACK", font=fnt, command= lambda: buttonClick(root,c,11))
    b11.place(x=1250, y=50, width=170, height=50)
    var = IntVar()
    r1=Radiobutton(c, text="Cash On Delivery", bg='orange', fg='black', variable = var, value=1, font=('Times', 22, 'bold'), command=lambda: state(var,b9,b10))
    r2=Radiobutton(c, text="Online Payment   ", bg='orange', fg='black', variable = var, value=2, font=('Times', 22, 'bold'), command=lambda: state(var,b9,b10))
    r1.place(x=530, y=580)
    r2.place(x=530, y=615)
    root.mainloop()
    
def Confirm(root):
    global ref,current_date,pay
    root.title("Order Confirmation Page")
    root.geometry("1920x1080")
    c = Canvas(root, bg='cyan', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("confirm.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    fnt = ('Times', 26, 'bold','underline')
    c.create_text(470, 40, text="ORDER  CONFIRMATION  DETAILS :", font=fnt, fill='black')
    ref=random.randint(10000000,99999999)
    d1=date.today()
    current_date = d1.strftime("%d-%m-%Y")
    d2 = d1 + timedelta(days=5)
    target_date = d2.strftime("%d-%m-%Y")
    if x==1:
        pay="Cash On Delivery"
    elif x==2:
        pay="Paid Online"
    m=Message(c, text="\n    DEAR MR/MRS "+record[0][1]+" :\n\n       Your Refill Booking Request Has Been Placed Successfully . . .     \n\n       * Distributor : Bharat Gas Service\n\n       * Consumer Number : "+record[0][2]+"\n\n       * Reference Number : "+str(ref)+"\n\n       * Base Amount : RS 550    * Subsidy Amount : RS 130\n\n       * Total Amount : RS 680\n\n       * Payment Method : "+pay+"\n\n       * Date of Booking : "+current_date+"\n\n       * Expected Delivery Date : "+target_date+"\n\n    THANK YOU . . .", width=900, font=('Roman', 20, 'bold'), fg='white', bg='gray')
    m.place(x=180,y=80)
    fnt = ('Times', 22, 'bold')
    b12=Button(c, text="LOGOUT", font=fnt, command= lambda: buttonClick(root,c,12))
    b12.place(x=1250, y=50, width=170, height=50)
    root.mainloop()
    
def Pay(root):
    root.title("Online Payment Screen")
    root.geometry("1920x1080")
    c = Canvas(root, bg='cyan', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("pay.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    c.create_rectangle(200, 230, 900, 450, fill='white')
    fnt = ('Times', 26, 'bold','underline')
    c.create_text(550, 90, text="THANK  YOU  FOR  CHOOSING  ONLINE  PAYMENT . . .", font=fnt, fill='BLACK')
    c.create_text(300, 170, text="PAY HERE :", font=fnt, fill='indigo')
    fnt = ('Times', 21, 'bold')
    c.create_text(340, 280, text="SELECT BANK :", font=fnt, fill='indigo')
    c.create_text(380, 340, text="ATM CARD NUMBER :", font=fnt, fill='indigo')
    c.create_text(345, 395, text="ATM CARD CVV :", font=fnt, fill='indigo')
    e1=Entry(c, width=22, bg='LightGreen', fg='black', font=('Times', 20))
    e2=Entry(c, width=22, bg='LightGreen', fg='black', font=('Times', 20))
    e1.place(x=545, y=325)
    e2.place(x=545, y=380)
    var = StringVar()
    s=Spinbox(c, values=('SBI BANK', 'HDFC BANK', 'ICICI BANK', 'PMC BANK', 'BANK OF BARODA'), textvariable = var, width=21, bg='LightGreen', fg='black', font=('Times', 20))
    s.place(x=545, y=270)
    fnt = ('Times', 22, 'bold')
    b14=Button(c, text="BOOK NOW",state = DISABLED, font=fnt, command= lambda: buttonClick(root,c,14))
    b14.place(x=450, y=610, width=200, height=40)
    b15=Button(c, text="BACK", font=fnt, command= lambda: buttonClick(root,c,15))
    b15.place(x=1250, y=50, width=170, height=50)
    b13=Button(c, text="SUBMIT", font=fnt, command= lambda: buttonClick(root,c,13,e1,e2,var,b13,b14,b15))
    b13.place(x=450, y=485, width=200, height=40)
    fnt = ('Times', 20, 'bold')
    l=Label(c, text="      CAREFULLY FILL YOUR CREDENTIALS       ", font=fnt, fg='black')
    l.place(x=230,y=550)
    root.mainloop()

def Feedback(root):
    root.title("Feedback Page")
    root.geometry("1920x1080")
    c = Canvas(root, bg='cyan', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("feedback.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    fnt = ('Times', 26, 'bold','underline')
    c.create_text(450, 50, text="GIVE YOUR VALUABLE FEEDBACK HERE :", font=fnt, fill='BLACK')
    t=Text(c, width=70, height=14, font=('Times',20,'bold'),fg='black', bg='white')
    t.insert(END, "WRITE HERE ")
    t.place(x=150,y=120)
    fnt = ('Times', 22, 'bold')
    b16 = Button(c, text="SUBMIT", font=fnt, command = lambda:buttonClick(root, c, 16, t))
    b16.place(x=530,y=600,width=200,height=50)
    b17 = Button(c, text="BACK", font=fnt, command= lambda: buttonClick(root,c,17))
    b17.place(x=1250, y=50, width=170, height=50)
    root.mainloop()

def Logout(root):
    root.title("Logout Confirmation")
    root.geometry("1920x1080")
    c = Canvas(root, bg='gray', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("popup.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    fnt = ('Times', 60, 'bold')
    c.create_text(700, 250, text="       LOGOUT\nSUCCESSFULLY", font=fnt, fill='black')
    fnt = ('Times', 22, 'bold')
    b18 = Button(c, text="OK", font=fnt, command= lambda: buttonClick(root,c,18))
    b18.place(x=620, y=400, width=170, height=50)
    root.mainloop()

def Popup(root):
    global bd1
    root.title("ERROR - Something Wrong")
    root.geometry("1920x1080")
    c = Canvas(root, bg='gray', height=1080, width=1920)
    c.pack()
    img = ImageTk.PhotoImage(Image.open("popup.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    fnt = ('Times', 30, 'bold')
    c.create_text(700, 200, text="ERROR :\n\n* YOUR LAST REFILL BOOKING DATE IS "+bd1+"\n\n* YOU CAN'T BOOK MORE THAN ONE REFILL IN A MONTH", font=fnt, fill='black')
    fnt = ('Times', 22, 'bold')
    b19 = Button(c, text="OK", font=fnt, command= lambda: buttonClick(root,c,19))
    b19.place(x=600, y=370, width=170, height=50)
    root.mainloop()

        
root=Tk()
conn=db.connect(host='localhost',user='root',password='',database="python_project")
cursor=conn.cursor()
cursor.execute("create table if not exists Registration_Details(SrNo int AUTO_INCREMENT primary key, Name text, Cons_No text, Mobile_No text, Username text, Password text)")
cursor.execute("create table if not exists Booking_History(SrNo int AUTO_INCREMENT primary key, Name text, Consumer_No text, Reference_No text, Booking_Date text, Payment_Method text)")
cursor.execute("create table if not exists Feedback(SrNo int AUTO_INCREMENT primary key, Feedback text)")
'''
cursor.execute("create table if not exists Bank_Details(SrNo int AUTO_INCREMENT primary key, Bank_Name text, ATM_Card_No text, CVV text)")
b=['SBI BANK', 'HDFC BANK', 'ICICI BANK', 'PMC BANK', 'BANK OF BARODA']
atm=[111111111111,222222222222,333333333333,444444444444,555555555555]
cvv=[111,222,333,444,555]
for i in range(len(b)):
cursor.execute("insert into Bank_Details(Bank_Name, ATM_Card_No, CVV) values('%s','%s','%s')" % (b[i],atm[i],cvv[i]))
'''    
conn.commit()   
Welcome(root)



    
