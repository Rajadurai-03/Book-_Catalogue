from tkinter import *
from tkinter import messagebox
import main
import mysql.connector
connection= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raja"
)
cursor=connection.cursor()
cursor.execute("USE books")
cursor.execute('''CREATE TABLE IF NOT EXISTS 
                users(username varchar(30) primary key,
                password varchar(20),doj date)'''
                )

root=Tk()
root.title('login')
root.geometry('950x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
    signinsuccess=main.dbsignin(cursor,username,password)
    if signinsuccess:
        screen=Toplevel(root)
        screen.title("home page" )
        screen.geometry('950x500+300+200')
        screen.configure(bg='#fff')
        Label(screen,text='hello everyone!',bg='#fff').pack(expand=True)
        screen.mainloop()
    else:
        messagebox.showerror("Invalid","invalid username or password")
    
def signup():
    screen=Toplevel(root)
    screen.title("signup")
    screen.geometry('950x500+300+200')
    screen.configure(bg='#fff')
    screen.resizable(False,False)
    
    img = PhotoImage(file='Login.png')
    screen.image = img 
    
    Label(screen, image=img, bg='#fff').place(x=50, y=140)



################################
img = PhotoImage(file='Login.png')
Label(root,image=img,bg='#fff').place(x=50,y=140)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=488,y=78)

heading=Label(frame,text='Sign in',fg='#652d90',bg='#fff',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)
###############################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        

user = Entry(frame,width=25,fg='black' ,border=0,bg='#fff',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
################################
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
        
code = Entry(frame,width=25,fg='black' ,border=0,bg='#fff',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
################################

Button(frame,width=39,pady=7 ,text='Sign in',bg='#652d90',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don 't have an account?",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#652d90',command=signup)
sign_up.place(x=215,y=270)
################################
root.mainloop()


cursor.close()
connection.commit()
connection.close()
