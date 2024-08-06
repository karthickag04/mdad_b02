from tkinter import *


def add():
    first_value=E_value1.get()
    second_vale=E_value2.get()
    result=int(first_value)+int(second_vale)
    lbl_resultshow.config(text=result)



app=Tk()
app.title("Operator Demo")
app.geometry("250x280+200+100")

mainframe=Frame(app, height=500, width=200, bg="red")
mainframe.pack(anchor="center", expand=True, ipadx=10, ipady=10)

lbl_name=Label(mainframe, text="welcome to frame with label", bg="gray")
lbl_name.grid(row=0, columnspan=4, padx=20, pady=20)

lbl_name=Label(mainframe, text="value1 :", bg="gray")
lbl_name.grid(row=1, column=0, padx=10, pady=10)

E_value1=Entry(mainframe)
E_value1.grid(row=1,column=1,padx=10, pady=10)

lbl_name=Label(mainframe, text="value2 :", bg="gray")
lbl_name.grid(row=2, column=0,padx=10, pady=10)

E_value2=Entry(mainframe)
E_value2.grid(row=2,column=1,padx=10, pady=10)


operatorframe=Frame(mainframe, bg="gray")
operatorframe.grid(row=3, columnspan=4, padx=10, pady=10)



btn_add=Button(operatorframe, text="+", command=add)
btn_add.grid(row=3, column=0, ipadx=7, ipady=5)

btn_subtract=Button(operatorframe,text="-")
btn_subtract.grid(row=3, column=1,ipadx=7, ipady=5)

btn_multiply=Button(operatorframe, text="*")
btn_multiply.grid(row=3, column=2,ipadx=7, ipady=5)

btn_division=Button(operatorframe, text="/")
btn_division.grid(row=3, column=3,ipadx=7, ipady=5)


lbl_resultshow=Label(mainframe, bg="gray", text="Output")
lbl_resultshow.grid(row=4, columnspan=4, padx=10, pady=10)


app.mainloop()
