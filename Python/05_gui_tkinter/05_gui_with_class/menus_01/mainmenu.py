from tkinter import *

def mainmenulist(app):
    menulist=Menu(app)
    app.config(menu=menulist)

    menulist.add_cascade(label="File")


    menulist.add_cascade(label="Edit")
    menulist.add_cascade(label="View")
    menulist.add_cascade(label="Help")

