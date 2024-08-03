from tkinter import *
from tkinter import messagebox

# Create the main application window
root = Tk()
root.title("Notepad")  # Set the title of the window
root.geometry("600x400+350+100")  # Set the size and position of the window

# Function to close the application
def closeApp(event=None):
    root.destroy()

# Function to create a new file
def createnewfile(event=None):
    if messagebox.askyesnocancel("Save File", "Do you want Save?"):
        textarea.delete("1.0", END)

# Create a text area widget
textarea = Text(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth())
textarea.pack(fill="both", expand=True, padx=10, pady=10)

# Create a menu bar
menulist = Menu(root)
root.config(bg="gray", menu=menulist)

# Create a File menu and add items to it
filemenu = Menu(menulist, tearoff=0)
menulist.add_cascade(label="File", menu=filemenu, underline=0)

filemenu.add_command(label="New", command=createnewfile, underline=0, accelerator="Ctrl + N")

# Create a submenu under the File menu
filentexsub = Menu(filemenu)
filemenu.add_cascade(label="New file", command=createnewfile, underline=1, accelerator="Ctrl + e", menu=filentexsub)

# Add commands to the New file submenu
filentexsub.add_command(label="new")
filentexsub.add_command(label="new window")
filentexsub.add_command(label="new text file")

filemenu.add_command(label="close", command=closeApp, underline=4, accelerator="Ctrl + Q")

# Add additional menu options
menulist.add_cascade(label="Edit")
menulist.add_cascade(label="View")
menulist.add_cascade(label="Help")

# Bind keyboard shortcuts to functions
root.bind("<Control-n>", createnewfile)
root.bind("<Control-q>", closeApp)

# Start the main event loop
root.mainloop()
