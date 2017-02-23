import glob, os
import numpy as np
import matplotlib.pyplot as pl
import matplotlib, sys

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
matplotlib.use('TkAgg')

from FFT_Library1 import FFT_Library
from tkinter import *

## Plot Data given two sets of data (in form x + " " + y).
def plotDataOld(self,data1, data2, title1, title2):

        # Setup figure to hold subplots
        f = Figure(figsize=(10,8), dpi=100)
        
        # Setup subplots
        subplot1=f.add_subplot(2,1,1)
        subplot1.plot(data1[:,0], data1[:,1], "r*")
        subplot1.set_xlim([0,10])
        subplot1.set_ylim([0,10])

        subplot2=f.add_subplot(2,1,2)
        subplot2.plot(data2[:,0], data2[:,1], "r*")
        subplot2.set_xlim([0,10])
        subplot2.set_ylim([0,10])

        # Show plots
        dataPlot = FigureCanvasTkAgg(f, master=root)
        dataPlot.show()
        dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

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
        dataPlot = FigureCanvasTkAgg(f, master=root)
        dataPlot.show()
        dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

        
## Main application
class MyApp:
    def __init__ (self, myParent):

        self.myContainer = Frame(myParent)
        self.myContainer.pack()
        
        self.listbox1 = Listbox(self.myContainer,exportselection=0)
        self.listbox1.pack(side=LEFT)

        self.listbox2 = Listbox(self.myContainer,exportselection=0)
        self.listbox2.pack(side=LEFT)
        
        filepath = "/home/pi/git/ui/profiles/"

        os.chdir(filepath)

        for file in glob.glob("*.txt"):
            if file.endswith(".txt"):
                self.listbox1.insert(END, file)
                self.listbox2.insert(END, file)
                full_filelocation = os.path.dirname(os.path.abspath(file))
        
        self.button1 = Button(self.myContainer)
        self.button1["text"]="Plot!"
        self.button1["background"] = "yellow"
        self.button1.pack()
        self.button1.bind("<Button-1>", self.button1Click)

## When Button #1 is clicked, find what was selected in listbox and load corresponding data
    def button1Click(self, event):
        print(self.listbox1.get(self.listbox1.curselection()) + " is selected in listbox 1")
        print(self.listbox2.get(self.listbox2.curselection()) + " is selected in listbox 2")

        for file in glob.glob("*.txt"):
            if file == self.listbox1.get(self.listbox1.curselection()):
                   data1 = np.loadtxt(self.listbox1.get(self.listbox1.curselection()))
        for file in glob.glob("*.txt"):
            if file == self.listbox2.get(self.listbox2.curselection()):
                   data2 = np.loadtxt(self.listbox2.get(self.listbox2.curselection()))     

        title1 = self.listbox1.get(self.listbox1.curselection())
        title2 = self.listbox2.get(self.listbox2.curselection())
        x1,y1 = FFT_Library.CalculateOptimizedFFT (data1, 256, 10)
        x2,y2 = FFT_Library.CalculateOptimizedFFT (data2, 256, 10)
        data1 = np.concatenate((np.array(x1),np.array(y1)),axis=1)
        data2 = np.concatenate((np.array(x2),np.array(y2)),axis=1)
        plotDataNew(self,x1,y1,x2,y2, title1, title2)
        
    
root = Tk()
myapp = MyApp(root)
root.mainloop()

