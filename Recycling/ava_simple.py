from tkinter import *
import numpy as np
import matplotlib.pyplot as pl
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib,sys
matplotlib.use('TkAgg')

def transferToPlotPage(self,controller,listbox_item,listbox_item1):
        
        controller.app_data["listbox"].set(listbox_item)
        controller.app_data["listbox1"].set(listbox_item1)
        value = listbox_item
        value1 = listbox_item1
        print(str(value) + " AND " + str(value1))
        print("Function successful successful")
        controller.show_frame(PlotPage)
def plotData(self, x1, y1):
        f = Figure(figsize=(10,8),dpi=100)

        subplot1=f.add_subplot(2,1,1)
        subplot1.plot(x1,y1)

        # Show plots
        dataPlot = FigureCanvasTkAgg(f,master=app)
        dataPlot.show()
        dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

class Application(tk.Tk):
    
    def __init__(self, *args,**kwargs):
        
        # Build container for app
        tk.Tk.__init__(self,*args,**kwargs)

        # App data in controller
        self.app_data = {"listbox":    StringVar(),
                         "listbox1":    StringVar(),
                         "entry":       StringVar(),
                         }
        
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        # Set available page frames
        for F in (StartPage, PlotPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column = 0, sticky = "nsew")

        # Show start page
        self.show_frame(StartPage)

    # Load desired page frame
    def show_frame(self, container):

        frame = self.frames[container]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
            self.controller = controller
            
            # initialize frame
            tk.Frame.__init__(self,parent)

            # Window title
            self.label = tk.Label(self, text="Start Page")
            self.label.pack(pady=10,padx=10)

            self.listbox = Listbox(self,exportselection=0)
            self.listbox.pack()

            self.listbox1 = Listbox(self,exportselection=0)
            self.listbox1.pack()
        
            for item in [0,1,2,3,4,5]:
                self.listbox.insert(END, item)
                self.listbox1.insert(END,item)

            # Button to plot data
            #self.button = tk.Button(self, text="Plot Page",command=lambda: controller.show_frame(PlotPage))
            self.button = tk.Button(self, text="Plot Page",command=lambda: transferToPlotPage(self,
                                                                                              controller,
                                                                                              self.listbox.get(self.listbox.curselection()),
                                                                                              self.listbox1.get(self.listbox1.curselection())))
            self.button.pack()

    
class PlotPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        # Window title
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Plot")
        label.pack(pady=10,padx=10)
        
        f = Figure(figsize=(5,8),dpi=100)

        listbox = self.controller.app_data["listbox"].get()
        listbox1 = self.controller.app_data["listbox1"].get()
                                    
        subplot1=f.add_subplot(2,1,1)
        subplot1.plot([3,4],[1,2])

        # Show plots
        dataPlot = FigureCanvasTkAgg(f,self)
        dataPlot.show()
        dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)
        

# Run App
app = Application()
app.title('Automotive Vibration Analyzer')
app.mainloop()
