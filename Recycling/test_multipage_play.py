from tkinter import *
from tkinter import ttk



class MyApp(Tk):
    # Controller class
    def __init__(self):
        Tk.__init__(self)

        # App data in controller
        self.app_data = {"listbox":    StringVar(),
                         "entry":       StringVar(),
                         }
        
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        self.frames = {}
        for F in (SelectPage, NextPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky = NSEW)
        self.show_frame(SelectPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self,classname):
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None

class SelectPage(ttk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Select Page').grid(padx=(20,20), pady=(20,20))
        
        self.listbox = Listbox(self,exportselection=0)
        self.listbox.grid()
        for item in [0,1,2,3,4,5]:
            self.listbox.insert(END, item)
            print (item)
        entry1 = ttk.Entry(self, textvariable=self.controller.app_data["entry"], width=8)
        entry1.grid()
##        button1 = ttk.Button(self, text='Next Page',
##                          command=lambda:self.doStuff(controller,self.listbox.get(self.listbox.curselection()))) # something like this lambda concept
        button1 = ttk.Button(self,text="Next Page",command=lambda: controller.show_frame(NextPage) or self.controller.app_data["listbox"].set(self.listbox.get(self.listbox.curselection())))
        button1.grid()

    def doStuff(self,controller,listbox_item):
        controller.show_frame(NextPage)
        controller.app_data["listbox"].set(listbox_item)
        value = listbox_item
        print(value)
        print("do Stuff successful")
        
class NextPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Next Page').grid(padx=(20,20), pady=(20,20))
        button1 = ttk.Button(self, text='Select Page',
                             command=lambda: controller.show_frame(SelectPage))
        button1.grid()
        button2 = ttk.Button(self, text='press to print', command=self.print_it)
        button2.grid()

    def print_it(self):
        
        value = self.controller.app_data["listbox"].get()
        print ('The value stored in StartPage some_entry = ' + str(value))
        value = self.controller.app_data["entry"].get()
        print ('The value stored in StartPage some_entry = ' + str(value))
app = MyApp()
app.title('Multi-Page Test App')
app.mainloop()
