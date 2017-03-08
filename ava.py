import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

# Math functions library
import numpy as np
#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
# Plot Page Code
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

from sys import argv

# Plot Page
def animate(i):
        filepath = "/home/pi/ava/"
        os.chdir(filepath)
        
        pullData = open('DataPlotFile.txt','r').read()
        dataList = pullData.split('\n')
        xList = []
        yList = []

        for eachLine in dataList:
                if len(eachLine) > 1:
                        x, y = eachLine.split(' ')
                        xList.append(int(x))
                        yList.append(int(y))

        a.clear()
        a.title.set_text("Length " + str(len(xList)))
        a.plot(xList,yList)
        
class Plot_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                # AVA app controller (app_data access)
                self.controller = controller
                
                label = ttk.Label(self, text="Plot Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToHomePage_button = ttk.Button(self, text="Home",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                canvas = FigureCanvasTkAgg(f, self)
                canvas.show()
                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                toolbar = NavigationToolbar2TkAgg(canvas, self)
                toolbar.update()
                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#------------------------------------------------------------------#
#------------------------------------------------------------------#                
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='792x477+0+0'
        master.geometry("{0}x{1}+0+0".format(
        master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
       
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

# Startup routine
class AVA(tk.Tk):    
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        # App Data global variable holder
        self.app_data = {"var1":    tk.StringVar(),
                         "var2":    tk.StringVar(),
                         "var3":    tk.StringVar()
                         }
        
        # Container holding app pages
        container = tk.Frame(self)
        container.pack(side="top",expand=False)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        # Initial empty set of page frames
        self.frames = {}

        # Application pages to load in background
        from Home_Page import Home_Page
        from Configure_Test_Page import Configure_Test_Page
        from New_Vehicle_Page import New_Vehicle_Page
        from Test_Is_Running_Page import Test_Is_Running_Page
        from Save_Test_Page import Save_Test_Page
        from Results_Page import Results_Page

        # Create frames for each of the app pages
        for F in (Home_Page, Configure_Test_Page, Plot_Page, New_Vehicle_Page, Test_Is_Running_Page, Save_Test_Page, Results_Page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew") 

        # First page to load is Home_Page
        self.show_page("Home_Page")
        
    # Define how frames will be promoted to current Tkinter frame
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
    # Search through possible pages to find
    # desired page to promote to current Tkinter frame
    def show_page(self,page_name):
        '''Show a frame for the given page name'''
        for F in self.frames:
            if F == page_name:
                self.show_frame(F)
                return

# -------------------------------------------------------------#
# --------------------- Run the app ---------------------------#
# -------------------------------------------------------------#
app = AVA()
app.title("Automotive Vibration Analyzer")
#fullscreen = FullScreenApp(app)
animate = animation.FuncAnimation(f,animate,interval=1000)
app.mainloop()
