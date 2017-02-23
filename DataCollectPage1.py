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

from tkinter import *

LARGE_FONT= ("Verdana", 12)
class DataCollectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Data Collect", font=LARGE_FONT)
        label.pack(pady=1,padx=1, side = TOP, anchor = N)

        homeButton= ttk.Button(self, text="Home",
                            command=lambda: controller.show_page("StartPage"))
        homeButton.pack(pady=1, padx=15, side = LEFT, expand = NO, anchor = N)

        initiateSampleCollectionButton = ttk.Button(self, text="Click to start collecting samples from the wireless sensor unit")
        initiateSampleCollectionButton.pack(pady=1,  padx=55, side = LEFT, expand = NO, anchor = N)

        
