from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("700x840")
window.title("Speed calculation")
window.config(bg="red")
def over_speed():
    speed_limit = 90
    speed = int(e1.get())
    if speed <= speed_limit:
        messagebox.showinfo("status","No penalty")
    elif speed < speed_limit+20 :
        messagebox.showwarning("Warning","Warning speed is exceeding.Please slow down")
    else:
        messagebox.showwarning("Penalty","1000rs")
l1 = Label(window,text="speed")
l1.grid(row=0,column=0)
e1 = Entry(window)
e1.grid(row=0,column=1)
b1 = Button(window,text="submit",command=over_speed)
b1.grid(row=1,column=1)
window.mainloop()