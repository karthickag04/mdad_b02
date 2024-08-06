from tkinter import *



class MenuCreation():

    def __init__(self,app):
        self.app=app
        self.mainmenulist()
    
    def mainmenulist(self):
        menulist=Menu(self.app)
        self.app.config(menu=menulist)

        self.filemenu(menulist)

        menulist.add_cascade(label="Edit")
        menulist.add_cascade(label="View")
        menulist.add_cascade(label="Help")

    def filemenu(self,menulist):

        filemenu=Menu(menulist)
        menulist.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New")
        filemenu.add_separator()
        filemenu.add_command(label="New file")
        filemenu.add_command(label="New Window")







