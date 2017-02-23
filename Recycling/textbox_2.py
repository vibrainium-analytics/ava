import tkinter
from tkinter import *

root = Tk()
root.title('Form')
Label(text="User: ").pack(side=TOP, padx=10, pady=10)

entry = Entry(root,width=10)
entry.pack(side=TOP,padx=10,pady=10)

Label(text="Password: ").pack(side=TOP, padx=10, pady=10)
entry1 = Entry(root,width=10)
entry1.pack(side=TOP,padx=10,pady=10)

def doMath(int1,int2):
    return int1+int2

def onButtonClick():
    user = entry.get()
    pw = entry1.get()
    print(user + pw)
    print(doMath(user,pw))
    print("do stuff")
    entry.delete(0,END)
    entry1.delete(0,END)

Button(root, text="OK",command=onButtonClick).pack(side=LEFT)
Button(root, text="Close").pack(side=RIGHT)

root.mainloop()

