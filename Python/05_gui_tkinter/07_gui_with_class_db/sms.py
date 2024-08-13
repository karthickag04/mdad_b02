import tkinter as tk
from db.dbfile import *


con=dbconnection()
print("connection established at :",con.dbconn())


def insert_student_record():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    dob_= dob_entry.get()
    mobile_no=mobile_number_entry.get()


    connection=con.dbconn()
    result_cursor=connection.cursor()
    query="INSERT INTO student(first_name,last_name,dob,mobile_no) VALUES (%s,%s,%s,%s);"
    values=(first_name,last_name,dob_,mobile_no)
    result_cursor.execute(query,values)
    connection.commit()
    result_cursor.close()
    connection.close()
    rmsg="Record inserted successfully"
    lbl_resultshow.config(text=rmsg)





# Create the main window
root = tk.Tk()
root.title("User Information Form")

# Set up the root window to use grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a frame and center it using grid
framemain = tk.Frame(root, bg="gray")
framemain.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

# Configure the frame's row and column to be responsive
framemain.grid_rowconfigure(5, weight=1)
framemain.grid_columnconfigure(1, weight=1)

# Create and place labels and entry fields within the frame
tk.Label(framemain, text="First Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
first_name_entry = tk.Entry(framemain)
first_name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(framemain, text="Last Name:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
last_name_entry = tk.Entry(framemain)
last_name_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(framemain, text="Date of Birth:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
dob_entry = tk.Entry(framemain)
dob_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(framemain, text="Mobile Number:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
mobile_number_entry = tk.Entry(framemain)
mobile_number_entry.grid(row=3, column=1, padx=10, pady=10)

# Add a submit button
submit_button = tk.Button(framemain, text="Submit", command=insert_student_record)
submit_button.grid(row=4, columnspan=2, pady=20)

lbl_resultshow = tk.Label(framemain, text="", bg="gray")
lbl_resultshow.grid(row=5, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
