from tkinter import *
from tkinter import messagebox

bank_window = Tk()
bank_window.geometry("700x840")
bank_window.config(bg="green")
def conditions():
    age = int(e1.get())
    salary = int(e2.get())
    credit_score = int(e3.get())
    if age >= 21 and age < 60 :
        if salary >= 20000:
            if credit_score >= 650:
                messagebox.showinfo("RESULT","APPROVED")
    else:
        messagebox.showinfo("RESULT","FAILED")

#line 1
l1 = Label(bank_window,text="age")
l1.grid(row=0,column=0)
e1 = Entry(bank_window)
e1.grid(row=0,column=1)
#line 2
l2 = Label(bank_window,text="salary")
l2.grid(row=1,column=0)
e2 = Entry(bank_window)
e2.grid(row=1,column=1)
#line 3
l3 = Label(bank_window,text="credit_score")
l3.grid(row=2,column=0)
e3 = Entry(bank_window)
e3.grid(row=2,column=1)
# button
b1 = Button(bank_window,text="submit",command=conditions)
b1.grid(row=3,column=1)

bank_window.mainloop()