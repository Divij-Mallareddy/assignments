from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Discount based on price")
window.geometry("700x840")
window.config(background="blue")
def discount():
    bill = int(entry1.get())
    if bill >= 300 :
        discount = (bill*15)/100
        bill = bill - discount
        print("total amount to be paid",bill)
        messagebox.showinfo("invoice",f"total amount to be paid {bill}$",)
    elif bill < 300 and bill >= 200 :
        discount = (bill*10)/100
        bill = bill - discount
        print("total amount to be paid", bill)
        messagebox.showinfo("invoice", f"total amount to be paid {bill}$", )
    else:
        print("total amount to be paid", bill)
        messagebox.showinfo("invoice", f"total amount to be paid {bill}$"
                                       f"\nNo discount", )
label1 = Label(window,text="Total bill: ",justify="center")
label1.grid(row=0,column=0)
entry1 = Entry(window,justify="center")
entry1.grid(row=0,column=1)
button1 = Button(window,text="submit",command=discount)
button1.grid(row=1,column=1)
window.mainloop()
