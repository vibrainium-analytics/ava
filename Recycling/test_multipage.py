from tkinter import *
from tkinter import ttk

class MyApp(Tk):
    # Controller class
    def __init__(self):
        Tk.__init__(self)

        # OTHER METHOD
        self.app_data = {"name":    StringVar()
                         }
        
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        self.frames = {}
        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky = NSEW)
        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self,classname):
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='PageOne').grid(padx=(20,20), pady=(20,20))
        #self.make_widget(controller)

        # OR
        entry1 = ttk.Entry(self, textvariable=self.controller.app_data["name"], width=8)
        entry1.grid()
        button1 = ttk.Button(self, text='Next Page',
                          command=lambda: controller.show_frame(PageTwo))
        button1.grid()

    def make_widget(self, controller):
        self.some_input = StringVar
        self.some_entry = ttk.Entry(self, textvariable=self.some_input, width=8) 
        self.some_entry.grid()
        button1 = ttk.Button(self, text='Next Page',
                                  command=lambda: controller.show_frame(PageTwo))
        button1.grid()

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='PageTwo').grid(padx=(20,20), pady=(20,20))
        button1 = ttk.Button(self, text='Previous Page',
                             command=lambda: controller.show_frame(PageOne))
        button1.grid()
        button2 = ttk.Button(self, text='press to print', command=self.print_it)
        button2.grid()

    def print_it(self):
        #page_one = self.controller.get_page("PageOne")
        #value = page_one.some_entry.get()
        value = self.controller.app_data["name"].get()
        print ('The value stored in StartPage some_entry = ' + str(value))#What do I put here 
        #to print the value of some_input from PageOne

app = MyApp()
app.title('Multi-Page Test App')
app.mainloop()
