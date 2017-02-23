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

## Plot Data given two sets of data (in form x + " " + y).
def plotDataNew(self,x1,y1,x2,y2, title1, title2):

        # Setup figure to hold subplots
        f = Figure(figsize=(10,8), dpi=100)
        # Setup subplots
        subplot1=f.add_subplot(2,1,1)
        subplot1.plot(x1,y1, "-o")
        subplot1.set_title(title1)


        subplot2=f.add_subplot(2,1,2)
        subplot2.plot(x2,y2, "-o")
        subplot2.set_title(title2)

        # Show plots
        dataPlot = FigureCanvasTkAgg(f, master=app)
        dataPlot.show()
        dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)
            
class AVA(tk.Tk):
    

    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (StartPage, DataCollectPage, PlotPage, ProfilePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, container):

        frame = self.frames[container]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Start Page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Data Collect",command=lambda: controller.show_frame(DataCollectPage))
        button.pack()

        button2 = ttk.Button(self,text="Profile",command=lambda: controller.show_frame(ProfilePage))
        button2.pack()

        button3 = ttk.Button(self,text="Plot",command=lambda: controller.show_frame(PlotPage))
        button3.pack()

class ProfilePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Profile", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Data Collect",
                            command=lambda: controller.show_frame(DataCollectPage))
        button2.pack()

        button3 = ttk.Button(self, text="Plot",
                            command=lambda: controller.show_frame(PlotPage))
        button3.pack()


class DataCollectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Data Collect", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Profile",
                            command=lambda: controller.show_frame(ProfilePage))
        button2.pack()

        button3 = ttk.Button(self, text="Plot",
                            command=lambda: controller.show_frame(PlotPage))
        button3.pack()


class PlotPage(tk.Frame):
    
    


    ## Page Controller
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Plot", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button0 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button0.pack()

        button2 = ttk.Button(self, text="Profile",
                            command=lambda: controller.show_frame(ProfilePage))
        button2.pack()

        button3 = ttk.Button(self, text="Data Collect",
                            command=lambda: controller.show_frame(DataCollectPage))
        button3.pack()

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
        
        self.button1 = Button(self)
        self.button1["text"]="Plot!"
        self.button1["background"] = "yellow"
        self.button1.pack()
        self.button1.bind("<Button-1>", self.button1Click)

    ## Button 1 Click Event (Plot data)
    ## When Button #1 is clicked, find what was selected in listbox and load corresponding data
    def button1Click(self, event):
        print(self.listbox1.get(self.listbox1.curselection()) + " is selected in listbox 1")
        print(self.listbox2.get(self.listbox2.curselection()) + " is selected in listbox 2")

        for file in glob.glob("*.txt"):
            if file == self.listbox1.get(self.listbox1.curselection()):
                   data1 = np.loadtxt(file)
        for file in glob.glob("*.txt"):
            if file == self.listbox2.get(self.listbox2.curselection()):
                   data2 = np.loadtxt(file)     

        title1 = self.listbox1.get(self.listbox1.curselection())
        title2 = self.listbox2.get(self.listbox2.curselection())
        x1,y1 = FFT_Library.CalculateFFT (data1)
        x2,y2 = FFT_Library.CalculateFFT (data2)
        data1 = np.concatenate((np.array(x1),np.array(y1)),axis=1)
        data2 = np.concatenate((np.array(x2),np.array(y2)),axis=1)
        plotDataNew(self,x1,y1,x2,y2, title1, title2)

    

app = AVA()
app.mainloop()



