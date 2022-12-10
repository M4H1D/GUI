#MessageBox

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("MessageBox")
root.geometry("500x500+700+150")
root.resizable(width=False,height=False)

def show():
    result=messagebox.askquestion("Title", "Hello Mahid")
   
    if result == "yes":
        Label(root, text="You are a Mahid").pack()
    else:
        Label(root, text="You are a Kutta").pack()
btn=Button(root, text="Cilck Me!", command=show)
btn.pack()


root.mainloop()