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

f = Figure(figsize=(7,7), dpi=100)
a = f.add_subplot(111)

from sys import argv

# Plot Page
def animate(i):
        
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
        a.title.set_text("Data Plot")
        a.plot(xList,yList)
        a.set_xlabel('Frequency (Hz)')
        a.set_ylabel('Magnitude')
        
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
