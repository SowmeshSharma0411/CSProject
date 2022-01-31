import time
from tkinter import *
from tkinter import ttk
import tkinter.ttk
from functools import partial

from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
from ReturnBook import *
from Auth import *
from fines import *
from ViewBorrowers import *
import Manage_Window
from Manage_Window import *
import searchfunc

import datetime

import mysql.connector

mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor(buffered=True)


def myfunc(root1):
   root1.destroy()

   global root,Entry1b,Entry2,Entry2b,Entry3,Entry3b,Entry4

   global member_var, srn_var, first_var, last_var, bookid_var, booktitle_var, author_var, dateborrowed_var, datedue_var, search_var
   root=Tk()
   root.title('Library Management System')
   root.geometry('1600x800')

   member_var=StringVar()
   srn_var=StringVar()
   first_var=StringVar()
   last_var = StringVar()
   bookid_var = StringVar()
   booktitle_var = StringVar()
   author_var = StringVar()
   dateborrowed_var = StringVar()
   datedue_var = StringVar()

   search_var=StringVar()




   l1=Label(text='LIBRARY MANAGEMENT SYSTEM',bg='#ff6e40',fg='black',borderwidth=10,relief=RIDGE,font=('Times New Roman',50,'bold',),padx=2,pady=6).place(x=0,y=0,width=1275,height=100)

   frame=Frame(root,bg='#ff6e40').place(x=0,y=102,width=1275,height=570)

   # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& FRONT END &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

   # =========================================================================DataFrameLeft====================================================

   DataFrameLeft=LabelFrame(frame,bg='#ff6e40',text='Library Member Information',fg='midnightblue',font=('algerian',15,'bold'),borderwidth='10',relief=RIDGE,padx=0,pady=0).place(x=0,y=102,width=750,height=445)

   lbl1=Label(frame,text='Member Type',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl1.place(relx=0.03,y=130)
   comMember=tkinter.ttk.Combobox(DataFrameLeft,font=('times new roman',18,'bold'),width=13,state='readonly',textvariable=member_var)  #adding drop down box
   comMember['value']=('Student','Lecturer')   #values in the drop down box
   comMember.place(relx=0.18, rely=0.19,relwidth=0.35)

   lbl1b=Label(DataFrameLeft,text='Book ID',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl1b.place(relx=0.03,rely=0.45)
   Entry1b=Entry(bg='white',width=30,font=('times new roman',18,'bold'),textvariable=bookid_var).place(relx=0.18,height=30.5,relwidth=0.35,rely=0.45)

   lbl2=Label(DataFrameLeft,text='SRN No',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl2.place(relx=0.03,rely=0.25)
   Entry2=Entry(bg='white',width=20,font=('times new roman',18,'bold'),textvariable=srn_var).place(relx=0.18,rely=0.25,height=30.5,relwidth=0.3)

   def autoUser():
      userid=srn_var.get()
      fetchuser = "SELECT * FROM users WHERE SRN = " + str(userid)
      cur.execute(fetchuser)
      info = []
      for i in cur:
         info.append(i)
      first_var.set(info[0][2])
      last_var.set(info[0][3])



   b1 = Button(root, bg='chocolate', fg='black', borderwidth=5, relief=RAISED, text='Fetch',
               font=('Times new roman', 15, 'bold'), command=autoUser).place(relx=0.49,rely=0.25,height=30.5,relwidth=0.08)

   lbl2b=Label(DataFrameLeft,text='Book Title',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl2b.place(relx=0.02,rely=0.53)
   Entry2b=Entry(bg='white',width=30,font=('times new roman',18,'bold'),textvariable=booktitle_var).place(relx=0.18,height=30.5,relwidth=0.35,rely=0.53)

   lbl3=Label(DataFrameLeft,text='First Name',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl3.place(relx=0.03,rely=0.31)
   Entry3=Entry(bg='white',width=20,font=('times new roman',18,'bold'),textvariable=first_var).place(relx=0.18,rely=0.31,height=30.5,relwidth=0.35)

   lbl3b=Label(DataFrameLeft,text='Author',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl3b.place(relx=0.03,rely=0.62)
   Entry3b=Entry(bg='white',width=30,font=('times new roman',18,'bold'),textvariable=author_var).place(relx=0.18,height=30.5,relwidth=0.35,rely=0.62)

   lbl4=Label(DataFrameLeft,text='Last Name',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl4.place(relx=0.03,rely=0.37)
   Entry4=Entry(bg='white',width=20,font=('times new roman',18,'bold'),textvariable=last_var).place(relx=0.18,rely=0.37,height=30.5,relwidth=0.35)

   '''lbl4b=Label(DataFrameLeft,text='Borrow Date',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl4b.place(x=340,y=235)
   Entry4b=Entry(bg='white',width=30,font=('times new roman',13,'bold'),textvariable=dateborrowed_var).place(x=460,y=235,height=30)'''

   '''lbl5=Label(DataFrameLeft,text='Address Line 1',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl5.place(x=10,y=270)
   Entry5=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=270,height=30)'''

   '''lbl5b=Label(DataFrameLeft,text='Due Date',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl5b.place(x=340,y=270)
   Entry5b=Entry(bg='white',width=30,font=('times new roman',13,'bold'),textvariable=datedue_var).place(x=460,y=270,height=30)'''

   '''lbl6=Label(DataFrameLeft,text='Address Line 2',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl6.place(x=10,y=305)
   Entry6=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=305,height=30)'''

   '''lbl6b=Label(DataFrameLeft,text='Overdue',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl6b.place(x=340,y=305)
   Entry6b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=305,height=30)'''

   '''lbl7=Label(DataFrameLeft,text='Postal code',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl7.place(x=10,y=340)
   Entry7=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=340,height=30)'''

   '''lbl7b=Label(DataFrameLeft,text='Overdue Fine',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl7b.place(x=340,y=340)
   Entry7b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=340,height=30)'''

   '''lbl8=Label(DataFrameLeft,text='Mobile',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl8.place(x=10,y=375)
   Entry8=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=375,height=30)'''

   '''lbl8b=Label(DataFrameLeft,text='Actual Price',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl8b.place(x=340,y=375)
   Entry8b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=375,height=30)'''

   # ===============================================================DataFrameRight=========================================================

   DataFrameRight=LabelFrame(frame,bg='#ff6e40',fg='midnightblue',text='Book Details',font=('algerian',15,'bold'),borderwidth='10',relief=RIDGE,padx=0,pady=0).place(x=750,y=102,width=525,height=445)

   # Taking Books from the database into a list :
   global b
   b = []
   author = []

   s = "SELECT title FROM books"
   cur.execute(s)

   for x in cur:
      b.append(x)

   s = "SELECT author FROM books"
   cur.execute(s)

   for x in cur:
      author.append(x)

   def select(event=""):
      info=[]
      value=str(a.get(a.curselection()))
      x=value[2:-3]
      s = "SELECT bid, title, author FROM books WHERE title = '%s'" %x
      cur.execute(s)
      for i in cur:
         info.append(i)
         break
      bookid_var.set(info[0][0])
      booktitle_var.set(info[0][1])
      author_var.set(info[0][2])

   a=Listbox(DataFrameRight,font=('times new roman',12,'bold'),width=59,height=17)
   a.bind("<<ListboxSelect>>",select)
   a.place(x=765,y=180)

   lbl8b = Label(DataFrameRight, text='Search', bg='#ff6e40', fg='black', font=('Times new roman', 18, 'bold'))
   lbl8b.place(x=765, y=130)
   Entry8b = Entry(bg='white', width=30, font=('times new roman', 18, 'bold'),textvariable=search_var)
   Entry8b.place(x=850, y=130, height=35, relwidth=0.24)

   def searching(b):
      searchfunc.search("books",1)
      con2 = mysql.connector.connect(host="localhost", user="root", password="root", database="db")
      cur2= con2.cursor(buffered=True)
      cur2.execute("SELECT title from books WHERE flag=1")
      b1=[]
      for i in cur2:
         b1.append(i)
      if(len(b1)==0)and(len(searchfunc.searchquery)==0):
         a.delete(0, END)
         for item in b:
            a.insert(END, item)
      else:
         b=[]
         b=b1
         a.delete(0,END)
         for item in b:
            a.insert(END, item)
      scrlbar = Scrollbar(DataFrameRight)
      scrlbar.place(x=1245, y=180, height=345)

      a.config(yscrollcommand=scrlbar.set)
      scrlbar.config(command=a.yview())

      scrlbar.config(command=a.yview)

      #cur.execute("Update books SET flag=0")
      #con.commit()
      #Cursor is taking rsults from the prev search

   #Hafta add a Go Button to get the thing working.
   b1 = Button(root, bg='chocolate', fg='black', borderwidth=5, relief=RAISED, text='Go',
               font=('Times new roman',15, 'bold'), command=partial(searching,b)).place(x=1170, y=130, height=35,relwidth=0.07)
      #cur.execute("UPDATE books SET flag=0 WHERE title =%s" %(info1[i]))
   #search_var = always str

   for item in b:
      a.insert(END,item)


   scrlbar=Scrollbar(DataFrameRight)
   scrlbar.place(x=1245,y=180,height=345)

   a.config(yscrollcommand=scrlbar.set)
   scrlbar.config(command=a.yview())

   scrlbar.config(command=a.yview)
   #txt=Text(DataFrameRight,font=('Times new roman',12,'bold'),width=30,height=17).place(x=1010,y=130)      #ListBox

   #extractBid = "select SRN, FirstName, LastName, Mobile, Email, Bookid, BookTitle, Author, DateBorrowed, datedue from borrowers where SRN = '" + str(srn_var) + "'"

   def autoRet():
      l=[]
      l.append(srn_var.get())
      l.append(first_var.get())
      l.append(last_var.get())
      extractBid = "SELECT Bookid, BookTitle, Author FROM borrowers WHERE SRN = '%s'" %l[0]
      cur.execute(extractBid)
      info = []
      for i in cur:
         info.append(i)
      bookid_var.set(info[0][0])
      booktitle_var.set(info[0][1])
      author_var.set(info[0][2])

      #time.sleep(5)
      returnn(l)

   def Exit():
      root.destroy()
      ManageUsers()

   def Reset():
      member_var.set(""),
      srn_var.set(""),
      first_var.set(""),
      last_var.set(""),
      booktitle_var.set(""),
      author_var.set(""),
      bookid_var.set(""),


   # ====================================Buttons===========================================

   frameBtn=Frame(root,bg='powder blue',borderwidth=10,relief=RIDGE,padx=20).place(x=0,y=550,width=1275,height=95)

   b1=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Issue',font=('Times new roman',35,'bold'),command=issuebook).place(x=6.8,y=556.8,relwidth=1/6,height=80)
   b2=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Return',font=('Times new roman',35,'bold'),command=autoRet).place(x=220,y=556.8,relwidth=1/6,height=80)
   b3=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Display Borrowers',font=('Times new roman',35,'bold'),command=partial(View,root,1)).place(x=433,y=556.8,relwidth=1/3,height=80)
   b4=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Reset',font=('Times new roman',35,'bold'),command=Reset).place(x=860,y=556.8,relwidth=1/6,height=80)
   b5=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Exit',font=('Times new roman',35,'bold'),command=partial(Manage_Window.ManageWindow,root)).place(x=1075,y=556.8,width=190,height=80)


   # ===================================================Info Bar==================================

   #Info=Frame(root,bg='powder blue',borderwidth=10,relief=RIDGE,padx=20).place(x=0,y=530,width=1275,height=120)

def issuebook():
   #con.commit()

   input_bookid = str(bookid_var.get())
   title = str(booktitle_var.get())
   author = str(author_var.get())
   input_userid = int(srn_var.get())
   name = str(first_var.get())
   last_name = str(last_var.get())

   '''con = mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
   cur = con.cursor()'''

   root2 = Tk()
   root2.title("Library")
   # root2.minsize(width=300,height=300)
   root2.geometry("600x500")
   valid = False
   type = "student"
   flag = 0

   cur.execute(
      "SELECT bid FROM books")
   for k in cur:
      a = k[0]
      if (a == input_bookid): # checks if the book id inputed is valid by cross checking with the existing book ids in the book database
         valid = True
   '''if valid == False:
      headingLabel = Label(root2, text="book id entered invalid", bg='black', fg='white', font=('Courier', 15))
      headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
      quitBtn = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
      quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
      root2.mainloop()
      return  # exits the program once the quit button is pressed and returns to the main menu'''

   # checking valid user id code, have not done it yet since there is no user database
   # checking which type the user is, faculty or student, have not done yet since there is no user database yet

   cur.execute("select * from borrowers where SRN=%s", (input_userid,))
   #If the person has some book already : He first has to return that : He will not be allowed to borrow any other book :
   l = []

   for k in cur:
      l.append(k)

   if(len(l)!=0):
      messagebox.showwarning("ERROR","Return the Book which you already have")
      return

   else:

      '''for k in cur:
         if k[8] != None:
      
            duedate2 = datetime.strptime(k[8], "%Y-%m-%d")
            if datetime.now() > duedate2:  # checks whether the current date is after the due date, have figured out how to compare dates (but for now I have used ">")
               l.append(k + (((
                                         datetime.now() - duedate2).days) * 2,))  # prints due books details such as book name, borrowed date,etc. it calculates fine for the due books and prints it ---Fine comes during return book only : 
               flag = 1'''

      #if type == "student" :
      #print("these books have fines pending for them, please pay the fine at the earliest to borrow a new book")

      # gui code for a dailog box specifying the above message
      '''headingLabel = Label(root2,
                           text="these books have fines pending for them, please pay the fine at the earliest to borrow a new book",
                           bg='black', fg='white', font=('Courier', 15))
      headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
      Label(root2, text="%-30s%-30s%-75s%-60s%-30s%-50s%-50s" % (
      'sl_no', 'book id', 'title', 'author', "id", "name", "last name"), bg='black', fg='white').place(relx=0.07,
                                                                                                       rely=0.1)
      Label(root2, text="----------------------------------------------------------------------------", bg='black',
            fg='white').place(relx=0.05, rely=0.2)

      c = 1
      y = 0.3
      print(l)
      for i in l:
         Label(root2, text="%-30s%-30s%-60s%-60s%-30s%-50s%-50s" % (str(c), i[1], i[2], i[3], i[4], i[5], i[6]),
               bg='black', fg='white').place(relx=0.08, rely=y)
         c += 1
         y += 0.1

      quitBtn = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
      quitBtn.place(relx=0.53, rely=0.6, relwidth=0.18, relheight=0.08)

      root2.mainloop()
      return  # exits the program once the quit button is pressed and returns to the main menu
      # exit button to exit program and return to main menu'''

      '''if type == "faculty":
         print("please return the book at the earliest to borrow a new book")
         # gui code for a dailog box specifying the above message
         # exit button to exit program and return to main menu'''

      fetchuser="SELECT SRN,name,Last_name,Branch,semester,mobile_no,email_id FROM users WHERE SRN = "+str(input_userid)
      cur.execute(fetchuser)

      l=[]
      for i in cur:
         l.append(i)

      borrow_date = datetime.date.today()
      duedate = borrow_date + datetime.timedelta(days=14)
      duedate = str(duedate)
      borrow_date = str(borrow_date)
      val = (input_userid,name,last_name,l[0][-2],l[0][-1],input_bookid,title,author,borrow_date,duedate)
      cur.execute(
         "INSERT INTO borrowers (SRN,FirstName,LastName,Mobile,Email,Bookid,BookTitle,Author,DateBorrowed,datedue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
         val)
      # inserts details of the borrowed book with user details into issued books table
      con.commit()

      fetchbooks = "SELECT copies FROM books WHERE title = '" + title + "'"
      cur.execute(fetchbooks)

      for i in cur:
         cpy = int(i[0][0])
      cpy -= 1
      addSql = "UPDATE books \nSET copies = '%s' \nWHERE title = '%s';" %(str(cpy),str(title))
      cur.execute(addSql)
      con.commit()
      # basic gui code for a dialog box----A summary Box must be displayed too :
      #print("success, book has been issued")

      Canvas1 = Canvas(root2)

      Canvas1.config(bg="#006B38")
      Canvas1.pack(expand=True, fill=BOTH)

      headingFrame1 = Frame(root2, bg="#FFBB00", bd=5)
      headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

      headingLabel = Label(headingFrame1, text="Issue Summary", bg='black', fg='white', font=('Courier', 15))
      headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

      labelFrame = Frame(root2, bg='black')
      labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

      game_scroll = Scrollbar(labelFrame)
      game_scroll.pack(side=RIGHT, fill=Y)

      game_scroll = Scrollbar(labelFrame, orient='horizontal')
      game_scroll.pack(side=BOTTOM, fill=X)

      my_game = ttk.Treeview(labelFrame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

      my_game.pack(fill=BOTH, expand=True)

      game_scroll.config(command=my_game.yview)
      game_scroll.config(command=my_game.xview)

      my_game['columns'] = (
         'sl_no','SRN', 'FirstName', 'LastName', 'Mobile', 'Email', 'Bookid', 'BookTitle', 'Author', 'DateBorrowed', 'datedue')

      # format our column
      my_game.column("#0", width=0, stretch=NO)
      my_game.column("sl_no", anchor=CENTER, width=20)
      my_game.column("SRN", anchor=CENTER, width=30)
      my_game.column("FirstName", anchor=CENTER, width=80)
      my_game.column("LastName", anchor=CENTER, width=80)
      my_game.column("Mobile", anchor=CENTER, width=80)
      my_game.column("Email", anchor=CENTER, width=160)
      my_game.column("Bookid", anchor=CENTER, width=20)
      my_game.column("BookTitle", anchor=CENTER, width=120)
      my_game.column("Author", anchor=CENTER, width=80)
      my_game.column("DateBorrowed", anchor=CENTER, width=80)
      my_game.column("datedue", anchor=CENTER, width=80)

      # Create Headings
      my_game.heading("#0", text="", anchor=CENTER)
      my_game.heading("sl_no", text="Sl no", anchor=CENTER)
      my_game.heading("SRN", text="SRN", anchor=CENTER)
      my_game.heading("FirstName", text="FirstName", anchor=CENTER)
      my_game.heading("LastName", text="LastName", anchor=CENTER)
      my_game.heading("Mobile", text="Mobile No", anchor=CENTER)
      my_game.heading("Email", text="Email Id", anchor=CENTER)
      my_game.heading("Bookid", text="BookId", anchor=CENTER)
      my_game.heading("BookTitle", text="BookTitle", anchor=CENTER)
      my_game.heading("Author", text="Author", anchor=CENTER)
      my_game.heading("DateBorrowed", text="DateBorrowed", anchor=CENTER)
      my_game.heading("datedue", text="DateDue", anchor=CENTER)
      # button command=searchfunc



      '''Label(root2, text="%-30s%-30s%-75s%-60s%-30s%-50s%-50s%-50s%-50s%-50s" % (
         'SRN','FirstName','LastName','Mobile','Email','Bookid','BookTitle','Author','DateBorrowed','datedue'), bg='black', fg='white').place(relx=0.07,
                                                                                                          rely=0.1)
      Label(root2, text="----------------------------------------------------------------------------", bg='black',
            fg='white').place(relx=0.05, rely=0.2)'''

      c = 1
      y = 0.3
      l=[]
      cur.execute("SELECT SRN,FirstName,LastName,Mobile,Email,Bookid,BookTitle,Author,DateBorrowed,datedue FROM borrowers WHERE SRN = "+str(input_userid))

      m = 0
      for k in cur:
         m += 1
         my_game.insert(parent='', index='end', iid=m, text='', values=(m,) + k)
      my_game.pack()
      '''for i in cur:
         l.append(i)
      l1=[]
      #print(l)
      for i in l:
         l1=[]
         l1=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
         break
      my_game.insert(parent='', index='end', text='', values=l1)'''
      '''Label(root2, text="%-30s%-30s%-60s%-60s%-30s%-50s%-50s%-50s%-50s%-50s" %(l1),
            bg='black', fg='white').place(relx=0.08, rely=y)'''
         #c += 1
         #y += 0.1

      quitBtn = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
      quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

      root2.mainloop()
      return

   #"Fetch" button to autofill first and last name after SRN : Suhas Include this Pls :
   # Borrow summary proper display of table : Formatting of strs thats all :--Suhas Do the formatting : This is the old window :
   #Search Optn
   #Also : TextBoxes look little off : correct em :
   #For autoEmails : A window List of all PPl who havent submitted the books on time; -Later


   #Stitch the fncs proeprly : quit Btns :(HOME) --Done
   #Update Search to search by FirstName : Last name, Email ID -Trying - done
   #Returned Successfully in return screen : + lil error handling : like no user while borrowing : -Imp
   #Add a dynamic alert/Notif in dashboard(eg : "This book" due date is on "this date")
   #GUI : of everything : align everything first : + Borrow window : make fonts the same.

