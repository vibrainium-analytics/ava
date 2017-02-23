

from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print (e.get())
def makeentry(parent, caption, width=None, **options):
    print("Got here")
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry


b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()


user = makeentry(master, "User name:", 10)
password = makeentry(master, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
