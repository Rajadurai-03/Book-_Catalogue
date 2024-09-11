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

def signin():
    username = user.get()
    password = code.get()

    signinsuccess = main.dbsignin(cursor, username, password)
    if signinsuccess:
        root.withdraw()
                
        def btn_clicked():
            print("Button Clicked")

        watchlist = Toplevel(root)
        watchlist.geometry("950x500")
        watchlist.configure(bg="#ffffff")

        frame = Frame(watchlist, bg="#ffffff")
        frame.place(x=0, y=0)

        background_img = PhotoImage(file="background1.png")
        background = Label(frame, image=background_img, bg="#ffffff")
        background.pack()
        #frame.configure(height=500)
        img0 = PhotoImage(file="img0.png")
        b0 = Button(
            frame,
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat"
        )
        b0.place(x=650, y=430, width=47, height=56)

        img1 = PhotoImage(file="img1.png")
        b1 = Button(
            frame,
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat"
        )
        b1.place(x=376, y=440, width=61, height=37)

        img2 = PhotoImage(file="img2.png")
        b2 = Button(
            frame,
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat"
        )
        b2.place(x=314, y=440, width=61, height=37)

        
        rect_frame1 = Frame(frame, bg="red")
        rect_frame1.place(x=20, y=80, width=670, height=60)

        rect_frame2 = Frame(frame, bg="green")
        rect_frame2.place(x=20, y=150, width=670, height=60)

        rect_frame3 = Frame(frame, bg="blue")
        rect_frame3.place(x=20, y=220, width=670, height=60)

        rect_frame4 = Frame(frame, bg="yellow")
        rect_frame4.place(x=20, y=290, width=670, height=60)

        rect_frame5 = Frame(frame, bg="orange")
        rect_frame5.place(x=20, y=360, width=670, height=60)
        
        profile = Label(frame, text='USERNAME', fg='black', bg='#3D708D', font=('JosefinSansRoman-Regular', 9, 'bold'))
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

    img = PhotoImage(file='Login.png')
    Label(screen, image=img, bg='#fff').place(x=50, y=140)

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
