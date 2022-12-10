# Create a New window in 
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Create New Window ")
root.geometry("500x500+700+150")
root.resizable(width=False,height=False)

def create_new_window():
    new_win = Toplevel()
    new_win.title("New window")
    new_win.geometry("300x300")

    Label(new_win, text="Welcome Mahid").pack()

    Button(new_win, text="Close Window",command=new_win.destroy).pack()


btn=Button(root, text="Create a New Window", command=create_new_window)
btn.pack()


root.mainloop()