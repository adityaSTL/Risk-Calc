import tkinter as tk
from tkinter import *
import socket
import lorem



master=tk.Tk()
#master.iconbitmap(r'C:\Users\Aditya.gupta\Downloads\me.ico')
master.geometry("320x210")
master.title("Riskometer")



text = tk.Text(master, height=40)
Label(master, text='Entry Price',font=("Courier", 12)).place(x=10,y=3)
Label(master, text='Stop Loss',font=("Courier", 12)).place(x=10,y=32)
Label(master, text='Quantity',font=("Arial", 12),fg='green').place(x=20,y=123)
Label(master, text='Risk',font=("Arial", 12),fg='red').place(x=20,y=63)
Label(master, text='',font=("Arial", 12),fg='red').grid(row=4)

#R1 = Radiobutton(master, text="Nifty 50", value=1,command=sel)

qq=0

def sel():
   
   try:
    e3.delete(0, END)
    tata = int(str(var.get()))
    qq=tata
    e3.insert(0,tata)
   except:
     print("1 pass")
   #label.config(text = selection)

def calc():
    t1=int(e1.get())
    t2=int(e2.get())
    t3=(e3.get())
    #t4=(display.get())
    display.delete(0,END)
    R2.deselect()
    R3.deselect()
    R4.deselect()
    R5.deselect()
    display.insert(0,round(int(t3)/(t2-t1),1))
        

    
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    display.delete(0,END)
    R2.deselect()
    R3.deselect()
    R4.deselect()
    R5.deselect()


var = IntVar()    
    
e1 = Entry(master,font=("Courier", 13), width=10)
e2 = Entry(master,font=("Courier", 13), width=10)
e3 = Entry(master,bg='pink',font=("Courier", 13), width=10)
display=Entry(master,bg='light green',font=("Courier", 13), width=10)


e1.place(x=130,y=3)
e2.place(x=130,y=32)
e3.place(x=130,y=63)

R2 = Radiobutton(master, text="10K", variable=var, value=10000,command=sel, font=("Arial", 10))
R3 = Radiobutton(master, text="15K", variable=var, value=15000,command=sel, font=("Arial", 10))
R4 = Radiobutton(master, text="20K", variable=var, value=20000,command=sel, font=("Arial", 10))
R5 = Radiobutton(master, text="25K", variable=var, value=25000,command=sel, font=("Arial", 10))
R2.place(x = 60, y = 103, anchor = CENTER)
R3.place(x = 125, y = 103, anchor = CENTER)
R4.place(x = 190, y = 103, anchor = CENTER)
R5.place(x = 255, y = 103, anchor = CENTER)


display.place(x=130,y=123)

bt1=Button(master,text='Submit',font=("Courier", 12),command=calc)
bt1.place(x=102,y=175,anchor=CENTER)

bt2=Button(master,text='Clear',font=("Courier", 12),command=clear)
bt2.place(x=212,y=175,anchor=CENTER)

master.wm_attributes("-topmost", 1)
#print(t1)
#print(type(t1))
mainloop()