from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("950x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "E:\\dbms lab\\kamal\\background.png")
background = canvas.create_image(
    475.0, 213.0,
    image=background_img)

img0 = PhotoImage(file = "E:\\dbms lab\\kamal\\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 876, y = 433,
    width = 47,
    height = 56)

img1 = PhotoImage(file = "E:\\dbms lab\\kamal\\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 376, y = 404,
    width = 61,
    height = 37)

img2 = PhotoImage(file = "E:\\dbms lab\\kamal\\img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 314, y = 404,
    width = 61,
    height = 37)

canvas.create_text(
    859.5, 30.0,
    text = "USERNAME",
    fill = "#ffffff",
    font = ("JosefinSansRoman-Regular", int(20.0)))

window.resizable(False, False)
window.mainloop()
