from tkinter import *


class MenuCreation():

    def mainmenulist(self,app):
        menulist=Menu(app)
        app.config(menu=menulist)

        menulist.add_cascade(label="File")


        menulist.add_cascade(label="Edit")
        menulist.add_cascade(label="View")
        menulist.add_cascade(label="Help")



