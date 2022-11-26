#GUI - Radio Button

from tkinter import *
root=Tk()
v= IntVar()
rd1=Radiobutton(root,text="Man",variable=v,value=1)
rd1.pack(anchor=W)
rd2=Radiobutton(root,text="Dog",variable=v,value=2)
rd2.pack(anchor=W)
rd3=Radiobutton(root,text="Cat",variable=v,value=3)
rd3.pack(anchor=W)
rd4=Radiobutton(root,text="Rat",variable=v,value=4)
rd4.pack(anchor=W)
root.mainloop()