from tkinter import *
root=Tk()
root.title("Checkbox")
root.geometry("500x500+700+150")
root.resizable(width=False,height=False)

var=StringVar()
def Checkbox():
    mylabel = Label(root, text= var.get())
    mylabel.pack()
check=Checkbutton(root, text="I Agree with Terms and Conditions.", variable=var ,onvalue="On",offvalue="Off")
check.deselect()
check.pack()


btn=Button(root, text="Show Result", command=Checkbox)
btn.pack()
root.mainloop()