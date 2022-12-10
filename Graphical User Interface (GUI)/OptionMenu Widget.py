# OptionMenu Widget
from tkinter import *

root = Tk()
root.title("OptionMenu Widget")
root.geometry("600x600")
textVar = StringVar()
textVar.set("Mahidul")
print(textVar.get())

def show():
    selected = textVar.get()
    if selected == "Mahidul":
        label=Label(root, text="Hey Mahid")
        label.pack()
    else:
         label=Label(root, text=textVar.get())
         label.pack()


drop_menu = OptionMenu(root, textVar, "Mahidul", "Islam", "Mahid")
drop_menu.pack()

btn=Button(root,text="Show Result", command=show)
btn.pack()
root.mainloop()