import tkinter as tk

root=tk.Tk()
root.title("first GUI demo")
root.geometry("600x400+200+100")
# root.state('zoomed')
root.config(bg='red')


def closeapp():
    root.destroy()
# # textarea=tk.Text(root, height=200,width=300)
# # textarea.pack(expand=False)

# textarea=tk.Text(root, height=200,width=300)
# textarea.grid(row=2, column=2, padx=30, pady=30)


lbl_title=tk.Label(root, text="Student records")
lbl_title.grid(row=0, column=0, padx=10, pady=10)


lbl_username=tk.Label(root, text="username :")
lbl_username.grid(row=1, column=1, padx=10, pady=10)

lbl_username=tk.Label(root, text="age :")
lbl_username.grid(row=2, column=1, padx=30, pady=10)


entry_username=tk.Entry(root, width=40)
entry_username.grid(row=1, column=2, padx=10, pady=10)

entry_age=tk.Entry(root, width=40)
entry_age.grid(row=2, column=2, padx=10, pady=10)


btn_submit=tk.Button(text="Submit")
btn_submit.grid(row=3, column=3)


btn_submit=tk.Button(text="close app",command=closeapp)
btn_submit.grid(row=3, column=1)

root.mainloop()

