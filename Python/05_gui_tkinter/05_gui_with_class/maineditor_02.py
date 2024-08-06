from tkinter import *
from menus_02.mainmenu import *

# Create the main application window
app = Tk()
app.title("Tabbed Interface Demo")
app.geometry("600x400+200+100")


mc=MenuCreation()
mc.mainmenulist(app)

app.mainloop()
