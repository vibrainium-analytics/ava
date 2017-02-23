# Steve changes this
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

# Math functions library
import numpy as np

# Import plotting libraries
import matplotlib.pyplot as pl
import matplotlib, sys
import matplotlib.animation as animation
from matplotlib import style

# Plotting library canvas tool
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
matplotlib.use('TkAgg')

from FFT_Library import FFT_Library
from tkinter import *

LARGE_FONT= ("Verdana", 12)



f1 = Figure(figsize=(5,5), dpi=100)
f2 = Figure(figsize=(5,5), dpi=100)
a1 = f1.add_subplot(111)
a2 = f2.add_subplot(111)

from sys import argv


class AVA(tk.Tk):    
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        container = tk.Frame(self)

        container.pack(side="top",expand=False)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        from StartPage import StartPage
        from DataCollectPage import DataCollectPage
        from ProfilePage import ProfilePage
        from DiagnosticsPage import DiagnosticsPage
        
        for F in (StartPage, DataCollectPage, PlotPage, NewPlotPage, ProfilePage, DiagnosticsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew") 
        self.show_page("StartPage")

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
    def show_page(self,page_name):
        '''Show a frame for the given page name'''
        for F in self.frames:
            if F == page_name:
                self.show_frame(F)
                return

class PlotPage(tk.Frame):
        def createDataPlot(self):
                filepath = "/home/pi/ava/profiles/"
                os.chdir(filepath)

                # Find the text files selected and create data arrays
                for file in glob.glob("*.txt"):
                    if file == self.listbox1.get(self.listbox1.curselection()):
                        data1 = np.loadtxt(self.listbox1.get(self.listbox1.curselection()))

                for file in glob.glob("*.txt"):
                    if file == self.listbox2.get(self.listbox2.curselection()):
                        data2 = np.loadtxt(self.listbox2.get(self.listbox2.curselection()))
                
                title1 = self.listbox1.get(self.listbox1.curselection())
                title2 = self.listbox2.get(self.listbox2.curselection())
                
                x1,y1 = FFT_Library.CalculateFFT (data1)
                x2,y2 = FFT_Library.CalculateFFT (data2)

                print("got here")
                print(y1)
                
                data1 = np.concatenate((np.array(x1),np.array(y1)),axis=1)
                data2 = np.concatenate((np.array(x2),np.array(y2)),axis=1)

                filepath = "/home/pi/ava"
                os.chdir(filepath)
                np.savetxt('DataPlotFile.txt', np.column_stack((x1,y1)),fmt='%i %i')

    
        ## Page Controller
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text="Historical Plot", font=LARGE_FONT)
                label.pack(pady=2,padx=2, side = "top", anchor = N)

                buttonHome = ttk.Button(self, text="Home",
                                    command=lambda: controller.show_page("StartPage"))
                buttonHome.pack(pady=1, padx = 15, side= LEFT, expand = NO, anchor = N, fill = NONE)

                self.buttonPlot = ttk.Button(self, text="Plot!",
                                    command=lambda: self.createDataPlot())
                self.buttonPlot.pack(pady=1, padx = 15, side= LEFT, expand = NO, anchor = N, fill = NONE)
                
                self.listbox1 = Listbox(self,exportselection=0)
                self.listbox1.pack(pady = 1, padx = 2, side = RIGHT, expand = NO, anchor = N)

                self.listbox2 = Listbox(self,exportselection=0)
                self.listbox2.pack(pady=1,padx=2, side = RIGHT, expand = NO, anchor = N)

                canvas = FigureCanvasTkAgg(f1, self)
                canvas.show()
                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                toolbar = NavigationToolbar2TkAgg(canvas, self)
                toolbar.update()
                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                filepath = "/home/pi/ava/profiles/"
                os.chdir(filepath)
                for file in glob.glob("*.txt"):
                    if file.endswith(".txt"):
                        self.listbox1.insert(END, file)
                        self.listbox2.insert(END, file)
                        full_filelocation = os.path.dirname(os.path.abspath(file))


##
##                self.intiatePlotButton = Button(self)
##                self.intiatePlotButton["text"]="Plot!"
##                self.intiatePlotButton["background"] = "yellow"
##                self.intiatePlotButton.pack(pady=1,padx=20, side = RIGHT, expand = NO, anchor = NE)
##                self.intiatePlotButton.bind("<Button-1>", self.clickInitiatePlotButton)

        ## Button 1 Click Event (Plot data)
        ## When Button #1 is clicked, find what was selected in listbox and load corresponding data
##        def clickInitiatePlotButton(self, event):
##                print(self.listbox1.get(self.listbox1.curselection()) + " is selected in listbox 1")
##                print(self.listbox2.get(self.listbox2.curselection()) + " is selected in listbox 2")
##
##                self.intiatePlotButton["background"] = "green"
##                filepath = "/home/pi/ava/profiles/"
##                os.chdir(filepath)
##                for file in glob.glob("*.txt"):
##                    if file == self.listbox1.get(self.listbox1.curselection()):
##                        data1 = np.loadtxt(self.listbox1.get(self.listbox1.curselection()))
##
##                for file in glob.glob("*.txt"):
##                    if file == self.listbox2.get(self.listbox2.curselection()):
##                        data2 = np.loadtxt(self.listbox2.get(self.listbox2.curselection()))
##
##                
##                print(data1)
##                title1 = self.listbox1.get(self.listbox1.curselection())
##                print(title1)
##                title2 = self.listbox2.get(self.listbox2.curselection())
##                x1,y1 = FFT_Library.CalculateFFT (data1)
##                x2,y2 = FFT_Library.CalculateFFT (data2)
##                data1 = np.concatenate((np.array(x1),np.array(y1)),axis=1)
##                data2 = np.concatenate((np.array(x2),np.array(y2)),axis=1)
##                plotDataNew(self,x1,y1,x2,y2, title1, title2)

class NewPlotPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        # Window title
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Plot")
        label.pack(pady=10,padx=10)

        self.button = tk.Button(self, text="Go Back",command=lambda: controller.show_page("StartPage"))
        self.button.pack()

        canvas = FigureCanvasTkAgg(f2, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

##def transferToPlotPage(self,controller,listbox_item,listbox_item1):
##
##        controller.app_data["listbox"].set(listbox_item)
##        controller.app_data["listbox1"].set(listbox_item1)
##        value = listbox_item
##        value1 = listbox_item1
##        print(str(value) + " AND " + str(value1))
##        print("Transfer function successful ")
##        controller.show_page("NewPlotPage")
##
##        filepath = "/home/pi/ava/profiles"
##        os.chdir(filepath)
##        
##        filename1 = controller.app_data["listbox"].get()
##        for file in glob.glob("*.txt"):
##            if file == filename1:
##                   data1 = np.loadtxt(filename1)
##        
##        x1,y1 = FFT_Library.CalculateFFT (data1)
##        print("x1 \n " + str(x1) + "\n Length + " + str(len(x1)))
##        print("y1 \n " + str(y1) + "\n Length + " + str(len(y1)))
##
##        filepath = "/home/pi/ava"
##        os.chdir(filepath)
##        np.savetxt('DataPlotFile.txt', np.column_stack((x1,y1)),fmt='%i %i')
##
#### Plot Data given two sets of data (in form x + " " + y).
##def plotDataNew(self,x1,y1,x2,y2, title1, title2):
##
##
##        #fig.clf('all')
##        # Setup figure to hold subplots
##
##        fig = Figure(figsize=(7.9,3.5), dpi=100) #******This will need to be properly sized after creating
##        #****** a new pop-up window
##
##        # Setup subplots
##        subplot1=fig.add_subplot(2,1,1)
##        subplot1.plot(x1,y1, "-o")
##        subplot1.set_title(title1)
##
##        subplot2=fig.add_subplot(2,1,2)
##        subplot2.plot(x2,y2, "-o")
##        subplot2.set_title(title2)
##
##        # Show plots
##        dataPlot = FigureCanvasTkAgg(fig, master=app)
##        dataPlot.show()
##        dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)
##
##    

# Run the app
app = AVA()
app.title("Automotive Vibration Analyzer")
fullscreen = FullScreenApp(app)
animate1 = animation.FuncAnimation(f1,animate,interval=5000)
animate2 = animation.FuncAnimation(f2,animate,interval=5000)
app.mainloop()
