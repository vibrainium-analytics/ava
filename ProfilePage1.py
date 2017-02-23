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

class ProfilePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Profile Page", font=LARGE_FONT)
        label.pack(pady=1,padx=1, side = "top", anchor = N)

        homeButton= ttk.Button(self, text="Home",
                            command=lambda: controller.show_page("StartPage"))
        homeButton.pack(pady=1,padx=15, side = LEFT, expand = NO, anchor = N)

        newProfilePageButton = ttk.Button(self, text="Create a new vehicle profile")
        newProfilePageButton.pack(pady=1,padx=50, side = RIGHT, expand = NO, anchor = N)

        existingProfilePageButton = ttk.Button(self, text="Open/edit an existing vehicle profile")
        existingProfilePageButton.pack(pady=1,padx=50, side = RIGHT, expand = NO, anchor = N)

