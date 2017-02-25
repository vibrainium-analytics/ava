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

LARGE_FONT= ("Verdana", 12)



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Start Page")
        label.pack(pady=1,padx=1, side = "top", anchor = "n")


        profilePageButton = ttk.Button(self,text="Profile",command=lambda: controller.show_page("ProfilePage"))

        profilePageButton.pack(pady=1, padx = 15, side = "left", expand = "no", anchor = "n")
        
        dataCollectButton = ttk.Button(self, text="Collect Samples",command=lambda: controller.show_page("DataCollectPage"))
        dataCollectButton.pack(side = "right", expand = "yes", anchor = "n")

        plotPageButton = ttk.Button(self,text="Archived Data Plot\n   (Historical)",command=lambda: controller.show_page("PlotPage"))
        plotPageButton.pack(side = "right", expand = "yes", anchor = "n")

        NewPlotPageButton = ttk.Button(self,text="Active Data Plot\n(Updates every second)",command=lambda: controller.show_page("NewPlotPage"))
        NewPlotPageButton.pack(side = "right", expand = "yes", anchor = "n")

        diagnosticsPageButton = ttk.Button(self, text="Diagnostics - calculations",
                            command=lambda: controller.show_page("DiagnosticsPage"))
        diagnosticsPageButton.pack(side = "right", expand = "yes", anchor = "n")


##        quitButton = ttk.Button(self, text="Click here to exit the program",
##                            command=lambda: 
##        quitButton.pack(side = CENTER, expand = NO, anchor = S)

       # might want to use alternate method as this window can't be placed - it lands wherever it lands - not sure the specifics
        messagebox.showinfo("Welcome", "Thank you for choosing the Automotive Vibration Analyzer (AVA).\n\nThis product was designed by Vibrainium Analytics.  The team consists of 4 Arizona State student majoring in Electrical Engineering.\n\nBrian Eleson\nSteven Frederick\nJoshua Geyer\nSpencer Harro\n\nA special thanks goes out to our mentor on this project - Dr. Steven Phillips ")
   
        
