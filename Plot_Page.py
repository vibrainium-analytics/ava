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

# Plot Page
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
