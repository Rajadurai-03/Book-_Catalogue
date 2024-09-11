from tkinter import *
from tkinter import messagebox
import main
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raja"
)
cursor = connection.cursor()
cursor.execute("USE books")
cursor.execute('''CREATE TABLE IF NOT EXISTS 
                users(username varchar(30) primary key,
                password varchar(20),doj date)'''
                )

root = Tk()
root.title('login')
root.geometry('950x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)
global page
page=1

def signin():
    username = user.get()
    password = code.get()

    signinsuccess = main.dbsignin(cursor, username, password)
    if signinsuccess:
        root.withdraw()
                
        def add():
            watchlist.withdraw()
            screen = Toplevel(root)
            screen.title("Add Book")
            screen.geometry('950x500+300+200')
            screen.configure(bg='#fff')
            screen.resizable(False, False)
            # Label(screen,text="hello").pack()
            
            def addbook():
                book_name=book.get()
                rating = Rating.get()
                chapters=Chapters.get()
                maxchapters=Max_Chapters.get()
                main.dbaddbook(cursor,username,book_name,maxchapters,chapters,rating)
                connection.commit()
                screen.destroy()
                watchlist.deiconify()
                

            screen.img = PhotoImage(file='Login.png')
            Label(screen, image=screen.img, bg='#fff').place(x=50, y=140)
            frame1 = Frame(screen, width=350, height=350, bg="white")
            frame1.place(x=488, y=78)

            heading = Label(frame1, text='Add book', fg='#652d90', bg='#fff', font=('Microsoft Yahei UI Light', 23, 'bold'))
            heading.place(x=100, y=5)

            def on_enter(e):
                book.delete(0, 'end')

            def on_leave(e):
                name = book.get()
                if name == '':
                    book.insert(0, 'bookname')

            book = Entry(frame1, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
            book.place(x=30, y=70)
            book.insert(0, 'bookname')
            book.bind('<FocusIn>', on_enter)
            book.bind('<FocusOut>', on_leave)
            Frame(frame1, width=295, height=2, bg='black').place(x=25, y=97)

                    
            def on_enter(e):
                Max_Chapters.delete(0, 'end')

            def on_leave(e):
                name = Max_Chapters.get()
                if name == '':
                    Max_Chapters.insert(0, 'Max_Chapters')

            Max_Chapters = Entry(frame1, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
            Max_Chapters.place(x=30, y=130)
            Max_Chapters.insert(0, 'Max_Chapters')
            Max_Chapters.bind('<FocusIn>', on_enter)
            Max_Chapters.bind('<FocusOut>', on_leave)
            Frame(frame1, width=295, height=2, bg='black').place(x=25, y=157)

            def on_enter(e):
                Chapters.delete(0, 'end')

            def on_leave(e):
                name = Chapters.get()
                if name == '':
                    Chapters.insert(0, 'Chapters read')

            Chapters = Entry(frame1, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
            Chapters.place(x=30, y=190)
            Chapters.insert(0, 'Chapters read')
            Chapters.bind('<FocusIn>', on_enter)
            Chapters.bind('<FocusOut>', on_leave)
            Frame(frame1, width=295, height=2, bg='black').place(x=25, y=217)

            
            def on_enter(e):
                Rating.delete(0, 'end')

            def on_leave(e):
                name = Rating.get()
                if name == '':
                    Rating.insert(0, 'Rating')

            Rating = Entry(frame1, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
            Rating.place(x=30, y=250)
            Rating.insert(0, 'Rating')
            Rating.bind('<FocusIn>', on_enter)
            Rating.bind('<FocusOut>', on_leave)
            Frame(frame1, width=295, height=2, bg='black').place(x=25, y=277)

            Button(frame1, width=39, pady=7, text='Add book', bg='#652d90', border=0,command=addbook).place(x=35, y=300)

                    

            
 ########################           ##############################
        def forward():
            global page
            page+=1
            book_list=main.dbview(cursor,username)
            print(book_list,'\n')
            l=['','','','','']
            end=page*5
            start=end-4
            size=len(book_list)
            j=0
            if end<=size:
                for i in range(start-1,end):
                    l[j]=book_list[i][1].ljust(20," ")+str(book_list[i][2]).ljust(15," ")+str(book_list[i][3]).ljust(15," ")+str(book_list[i][4]).ljust(15," ")
                    print(l[j])
                    j=j+1
            else:
                for i in range(start-1,size):
                    l[j]=book_list[i][1].ljust(20," ")+str(book_list[i][2]).ljust(15," ")+str(book_list[i][3]).ljust(15," ")+str(book_list[i][4]).ljust(15," ")
                    print(l[j])
                    j=j+1

                    
            rect_frame1 = Frame(frame, bg="#F7F7F7")
            rect_frame1.place(x=20, y=95, width=670, height=60)
            Label(rect_frame1,text=l[0], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

            rect_frame2 = Frame(frame, bg="#F7F7F7")
            rect_frame2.place(x=20, y=155, width=670, height=60)
            Label(rect_frame2,text=l[1], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

            rect_frame3 = Frame(frame, bg="#F7F7F7")
            rect_frame3.place(x=20, y=220, width=670, height=60)
            Label(rect_frame3,text=l[2], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

            rect_frame4 = Frame(frame, bg="#F7F7F7")
            rect_frame4.place(x=20, y=290, width=670, height=60)
            Label(rect_frame4,text=l[3], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

            rect_frame5 = Frame(frame, bg="#F7F7F7")
            rect_frame5.place(x=20, y=365, width=670, height=60)
            Label(rect_frame5,text=l[4], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")
         ########################################   
        def backward():
            global page
            if page>1:
                page-=1
            book_list=main.dbview(cursor,username)
            print(book_list,'\n')
            l=['','','','','']
            end=page*5
            start=end-4
            size=len(book_list)
            j=0
            if end<=size:
                for i in range(start-1,end):
                    l[j]=book_list[i][1].ljust(20," ")+str(book_list[i][2]).ljust(15," ")+str(book_list[i][3]).ljust(15," ")+str(book_list[i][4]).ljust(15," ")
                    print(l[j])
                    j=j+1
            else:
                for i in range(start-1,size):
                    l[j]=book_list[i][1].ljust(20," ")+str(book_list[i][2]).ljust(15," ")+str(book_list[i][3]).ljust(15," ")+str(book_list[i][4]).ljust(15," ")
                    print(l[j])
                    j=j+1

                    
            rect_frame1 = Frame(frame, bg="#F7F7F7")
            rect_frame1.place(x=20, y=95, width=670, height=60)
            Label(rect_frame1,text=l[0], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

            rect_frame2 = Frame(frame, bg="#F7F7F7")
            rect_frame2.place(x=20, y=155, width=670, height=60)
            Label(rect_frame2,text=l[1], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

            rect_frame3 = Frame(frame, bg="#F7F7F7")
            rect_frame3.place(x=20, y=220, width=670, height=60)
            Label(rect_frame3,text=l[2], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

            rect_frame4 = Frame(frame, bg="#F7F7F7")
            rect_frame4.place(x=20, y=290, width=670, height=60)
            Label(rect_frame4,text=l[3], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

            rect_frame5 = Frame(frame, bg="#F7F7F7")
            rect_frame5.place(x=20, y=365, width=670, height=60)
            Label(rect_frame5,text=l[4], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")
            
##########################################################
        watchlist = Toplevel(root)
        watchlist.geometry("950x500")
        watchlist.configure(bg="#ffffff")

        frame = Frame(watchlist, bg="#ffffff")
        frame.place(x=0, y=0)

        background_img = PhotoImage(file="background1.png")
        background = Label(frame, image=background_img, bg="#ffffff")
        background.pack()
        count=main.dbgetrank(cursor,username)
        if count>=5 and count<10:
            rank_img = PhotoImage(file="silver.png")   
        elif count>=10:
            rank_img = PhotoImage(file="gold.png")
        else:
            rank_img = PhotoImage(file="bronze.png")
        rank = Label(frame, image=rank_img)
        rank.place(x=736,y=180)
        #frame.configure(height=500)
        img0 = PhotoImage(file="img0.png")
        b0 = Button(
            frame,
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=add,
            relief="flat"
        )
        b0.place(x=650, y=430, width=47, height=56)

        img1 = PhotoImage(file="img1.png")
        b1 = Button(
            frame,
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=forward,
            relief="flat"
        )
        b1.place(x=376, y=440, width=61, height=37)

        img2 = PhotoImage(file="img2.png")
        b2 = Button(
            frame,
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=backward,
            relief="flat"
        )
        b2.place(x=314, y=440, width=61, height=37)
        #value=['','','','']
        rect = Frame(frame, bg="#F7F7F7")
        rect.place(x=20, y=75, width=670, height=20)
        value="BookName".ljust(20)+"MaxChapter".ljust(15)+"Chapters".ljust(15)+"Rating".ljust(15)
        header=Label(rect, text=value, fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")
        book_list=main.dbview(cursor,username)
        print(book_list,'\n')
        l=['','','','','']
        end=page*5
        start=end-4
        size=len(book_list)
        j=0
        if end<=size:
            for i in range(start-1,end):
                l[j]=book_list[i][1].ljust(20," ")+str(book_list[i][2]).ljust(15," ")+str(book_list[i][3]).ljust(15," ")+str(book_list[i][4]).ljust(15," ")
                print(l[j])
                j=j+1
        else:
            for i in range(start-1,size):
                l[j]=book_list[i][1].ljust(20," ")+str(book_list[i][2]).ljust(15," ")+str(book_list[i][3]).ljust(15," ")+str(book_list[i][4]).ljust(15," ")
                print(l[j])
                j=j+1

                
        rect_frame1 = Frame(frame, bg="#F7F7F7")
        rect_frame1.place(x=20, y=95, width=670, height=60)
        Label(rect_frame1,text=l[0], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

        rect_frame2 = Frame(frame, bg="#F7F7F7")
        rect_frame2.place(x=20, y=155, width=670, height=60)
        Label(rect_frame2,text=l[1], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

        rect_frame3 = Frame(frame, bg="#F7F7F7")
        rect_frame3.place(x=20, y=220, width=670, height=60)
        Label(rect_frame3,text=l[2], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

        rect_frame4 = Frame(frame, bg="#F7F7F7")
        rect_frame4.place(x=20, y=290, width=670, height=60)
        Label(rect_frame4,text=l[3], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")

        rect_frame5 = Frame(frame, bg="#F7F7F7")
        rect_frame5.place(x=20, y=365, width=670, height=60)
        Label(rect_frame5,text=l[4], fg='#652d90', bg='#F7F7F7', font=('Courier New', 13, 'bold')).pack(side="left")
        
        profile = Label(frame, text=username, fg='black', bg='#3D708D', font=('JosefinSansRoman-Regular', 9, 'bold'))
        profile.place(x=859.5, y=20)
        # canvas.create_text(
        #     859.5, 30.0,
        #     text="USERNAME",
        #     fill="#ffffff",
        #     font=("JosefinSansRoman-Regular", int(20.0))
        # )

        watchlist.resizable(False, False)
        watchlist.mainloop()

    else:
        messagebox.showerror("Invalid", "Invalid username or password")

##########################################################
def signup():
    root.withdraw()
    screen = Toplevel(root)
    screen.title("signup")
    screen.geometry('950x500+300+200')
    screen.configure(bg='#fff')
    screen.resizable(False, False)

    def newdetails():
        try:
            name = user.get()
            key = code.get()
            ckey = confirm.get()
            if key == ckey:
                root.deiconify()
                screen.withdraw()
                main.dbsignup(cursor, name, key)
                print("success")
            elif key != ckey:
                messagebox.showerror("Invalid", "Give correct password")
            connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showerror("Invalid", "Username already exists")

    screen.img = PhotoImage(file='Login.png')
    Label(screen, image=screen.img, bg='#fff').place(x=50, y=140)

    frame1 = Frame(screen, width=350, height=350, bg="white")
    frame1.place(x=488, y=78)

    heading = Label(frame1, text='Sign up', fg='#652d90', bg='#fff', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame1, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(frame1, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame1, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(frame1, width=295, height=2, bg='black').place(x=25, y=177)

    def on_enter(e):
        confirm.delete(0, 'end')

    def on_leave(e):
        name = confirm.get()
        if name == '':
            confirm.insert(0, 'Confirm Password')

    confirm = Entry(frame1, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
    confirm.place(x=30, y=220)
    confirm.insert(0, 'Confirm Password')
    confirm.bind('<FocusIn>', on_enter)
    confirm.bind('<FocusOut>', on_leave)
    Frame(frame1, width=295, height=2, bg='black').place(x=25, y=247)

    Button(frame1, width=39, pady=7, text='Sign up', bg='#652d90', border=0, command=newdetails).place(x=35, y=274)

################################

img = PhotoImage(file='Login.png')
Label(root, image=img, bg='#fff').place(x=50, y=140)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=488, y=78)

heading = Label(frame, text='Sign in', fg='#652d90', bg='#fff', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

###############################
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

################################

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

################################

Button(frame, width=39, pady=7, text='Sign in', bg='#652d90', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white',
              font=('Microsoft Yahei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#652d90', command=signup)
sign_up.place(x=215, y=270)
################################

root.mainloop()

cursor.close()
connection.commit()
connection.close()
