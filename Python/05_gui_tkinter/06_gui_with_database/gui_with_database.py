import os
from tkinter import *
import mysql.connector

app=Tk()

app.title("Student Mark Entry")
app.geometry("800x600+300+60")


def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="192.168.29.244",
    user="test01",
    password="test@123",
    database="a"
    )

    return dbcon
    # print("connected to database at ",dbcon)  

def check_creation_of_insert():
    value1get=E_value1.get()
    value2get=E_value2.get()
   
    statement="insert into record(value1, value2) values("+str(value1get)+","+str(value2get)+");"  
    print(statement)    
    # statement="insert into record(value1, value2) values(200,200);"      

def insertrecord():
    value1get=E_value1.get()
    value2get=E_value2.get()

    con=MyDBConnection()
    result=con.cursor()
    statement="insert into record(value1, value2) values("+str(value1get)+","+str(value2get)+");"  
    result.execute(statement)
    con.commit()
    con.close()
    print(statement)    
    msg = "value inserted successfully"
    lbl_resultshow.config(text=msg) 
    selectdatas()
    # statement="insert into record(value1, value2) values(200,200);"      


def updaterecord():
    value1get=E_value1.get()
    value2get=E_value2.get()

    con=MyDBConnection()
    result=con.cursor()
    passvalue=(value2get,value1get)
    statement="update record set value2=%s where value1=%s;"  
    result.execute(statement,passvalue)
    con.commit()
    con.close()
    print(statement)    
    msg = "value updated successfully"
    lbl_resultshow.config(text=msg) 
    selectdatas()
    # statement="insert into record(value1, value2) values(200,200);"      


def deleterecord():
    value1get=E_value1.get()
    # value2get=E_value2.get()

    con=MyDBConnection()
    result=con.cursor()
    passvalue=(value1get,)
    statement="delete from record where value1 =%s;"  
    result.execute(statement,passvalue)
    con.commit()
    con.close()
    print(statement)    
    msg = "record deleted successfully"
    lbl_resultshow.config(text=msg) 
    selectdatas()
    # statement="insert into record(value1, value2) values(200,200);"     
    # 

# try yourself how the data get retrived given with demo values
def select_working_logic():
    print("")
    result= ((22,22),(22,21),(20,34))
    print(result)
    print("")
    for record in result:
        print(record)
    print("")
    for record in result:
        for r in range(len(record)):
            print(record[r])


def selectdatas():

    con=MyDBConnection()
    result=con.cursor()
    result.execute("SELECT * FROM record")
    i=0 
    for record in result: 
        for j in range(len(record)):
            lbldisplay = Entry(displayframe, width=10, fg='blue') 
            lbldisplay.grid(row=i, column=j) 
            lbldisplay.insert(END, record[j])
        i=i+1 



dbcon1=MyDBConnection()
if dbcon1:
    x = "connected"
else:
    x = "not connected"
print("connected to database throug outside of def at  ",dbcon1) 



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



btn_add=Button(operatorframe, text="Insert", command=insertrecord)
btn_add.grid(row=3, column=0, ipadx=7, ipady=5)

btn_subtract=Button(operatorframe,text="update", command=updaterecord)
btn_subtract.grid(row=3, column=1,ipadx=7, ipady=5)

btn_multiply=Button(operatorframe, text="delete", command=deleterecord)
btn_multiply.grid(row=3, column=2,ipadx=7, ipady=5)

btn_division=Button(operatorframe, text="select", command=selectdatas)
btn_division.grid(row=3, column=3,ipadx=7, ipady=5)


lbl_resultshow=Label(mainframe, bg="gray", text=x)
lbl_resultshow.grid(row=4, columnspan=4, padx=10, pady=10)

displayframe=Frame(mainframe, bg="yellow")
displayframe.grid(row=5, columnspan=5, padx=10, pady=10)

selectdatas()

app.mainloop()