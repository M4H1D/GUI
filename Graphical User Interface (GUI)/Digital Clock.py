# Digital Clock
from tkinter import *
import time

root=Tk()
root.title("Digital Clock")


def Times():
    timeVar = time.strftime("%I: %M: %S %p")
    label.config(text=timeVar)
    label.after(200, Times)


label = Label(root, text="Clock", font=("Arial", 100), bg="black", fg="green")
label.pack()     

Times()

root.mainloop()