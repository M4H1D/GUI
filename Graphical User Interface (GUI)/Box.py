#GUI - textbox
from tkinter import *
root=Tk()
def hello():
    print("Hello, How are you?")
b1=Button(root,text="Hello",command=hello)
b1.pack()
def about():
    print("""I am Mahidul Islam. I don't know how to help you?
because I have nothing. Only ALLAH can help you. Never forget ALLAH.""")
b2=Button(root,text="About",command=about)
b2.pack()
b3=Entry(root,bd=10)
b3.pack()
b4=Button(root,text="Exit",command=root.destroy)
b4.pack()
l1=Label(root,text="Password")
e1=Entry(root,bd=5,fg="black",show="*")
l1.pack(side=LEFT)
e1.pack(side=RIGHT)
root.mainloop()