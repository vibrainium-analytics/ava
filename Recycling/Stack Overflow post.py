from tkinter import *
from tkinter import ttk

class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        # App data in controller
        self.app_data = {"listbox":    StringVar()}
        
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        self.frames = {}
        
        for F in (Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky = NSEW)
        self.show_frame(Page1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Page1(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.listbox = Listbox(self,exportselection=0)
        self.listbox.grid()
        for item in [0,1,2,3,4,5]:
            self.listbox.insert(END, item)
            
        button1 = ttk.Button(self,text="Next Page"
                             ,command=lambda: controller.show_frame(Page2)
                             or self.controller.app_data["listbox"]
                             .set(self.listbox.get(self.listbox.curselection())))
        button1.grid()

class Page2(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        ttk.Label(self, text='Next Page').grid(padx=(20,20), pady=(20,20))
        button1 = ttk.Button(self, text='Select Page',
                             command=lambda: controller.show_frame(Page1))
        button1.grid()
        button2 = ttk.Button(self, text='print value', command=self.print_value)
        button2.grid()
    def print_value(self):
        value = self.controller.app_data["listbox"].get()
        print ('The value stored in StartPage some_entry = ' + str(value))
            
app = MyApp()
app.mainloop()
