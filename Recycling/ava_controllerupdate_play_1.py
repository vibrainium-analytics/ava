import tkinter as tk
from tkinter import ttk

# File system access library
import glob, os

# Math functions library
import numpy as np

# Import plotting libraries
import matplotlib.pyplot as pl
import matplotlib, sys

# Plotting library canvas tool
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
matplotlib.use('TkAgg')

from FFT_Library import FFT_Library
from tkinter import *

LARGE_FONT= ("Verdana", 12)

##def configurePlot(self, controller):
##    # Get data from listbox files
##    # TODO rework for app_data
##    for file in glob.glob("*.txt"):
##        if file == self.listbox1.get(self.controller.app_data["Listbox1_selection"].get()):
##               data1 = np.loadtxt(self.listbox1.get(self.controller.app_data["Listbox1_selection"].get()))
##    for file in glob.glob("*.txt"):
##        if file == self.listbox2.get(self.controller.app_data["Listbox2_selection"].get()):
##               data2 = np.loadtxt(self.listbox2.get(self.controller.app_data["Listbox2_selection"].get()))  
##
##    title1 = self.controller.app_data["Listbox1_selection"].get()
##    title2 = self.controller.app_data["Listbox2_selection"].get()
##    if(data1 != null and data2 != null):
##        x1,y1 = FFT_Library.CalculateFFT (data1)
##        x2,y2 = FFT_Library.CalculateFFT (data2)
##    else:
##        print("Houston, we have a problem")
##    return (title1, title2, x1, y1, x2, y2)
##


class AVA(Tk):

    # Controller Class
    def __init__(self, *args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)

        # Create array of app data available to all app pages
        self.app_data = {"Listbox1_selection":  StringVar(),
                         "Listbox2_selection":  StringVar(),
                         }
        container = ttk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (ListboxSelectPage,PlotPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column = 0, sticky = "nsew")

        self.show_frame(ListboxSelectPage)

        def show_frame(self, container):

            frame = self.frames[container]
            frame.tkraise()


class ListboxSelectPage(ttk.Frame):

    def __init__(self,parent,controller):
        self.controller = controller

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Listbox Select", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button3 = Button(self,text="Plot")
        button3.pack()
        button3.bind("<Button-1>",self.buttonClick)

        self.listbox1 = Listbox(self,exportselection=0)
        self.listbox1.pack(side=LEFT)

        self.listbox2 = Listbox(self,exportselection=0)
        self.listbox2.pack(side=LEFT)

        filepath = "/home/pi/git/ui/profiles/"

        os.chdir(filepath)

        for file in glob.glob("*.txt"):
            if file.endswith(".txt"):
                self.listbox1.insert(END, file)
                self.listbox2.insert(END, file)
                full_filelocation = os.path.dirname(os.path.abspath(file))
        
    def buttonClick(self,event):

        print(self.listbox1.get(self.listbox1.curselection()) + " is selected in listbox 1")
        print(self.listbox2.get(self.listbox2.curselection()) + " is selected in listbox 2")
        controller.show_frame(PlotPage)

class PlotPage(ttk.Frame):

    ## Page Controller
    def __init__(self, parent, controller):
        self.controller = controller

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Plot", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button0 = ttk.Button(self, text="ListboxSelect",command=lambda: controller.show_frame(StartPage))
        button0.pack()

        # Configure plot parameters
        #(title1, title2, x1,y1, x2, y2) = configurePlot(self,controller)

        # Setup figure to hold subplots
        f = Figure(figsize=(10,8), dpi=100)

        # Setup subplots
        subplot1=f.add_subplot(2,1,1)
        #subplot1.plot(x1,y1, "-o")
        subplot1.plot([1,2],[1,2], "-o")
        #subplot1.set_title(title1)

        subplot2=f.add_subplot(2,1,2)
        #subplot2.plot(x2,y2, "-o")
        subplot2.plot([1,2],[1,2], "-o")
        #subplot2.set_title(title2)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)



app = AVA()
app.title("AVA")
app.mainloop()



