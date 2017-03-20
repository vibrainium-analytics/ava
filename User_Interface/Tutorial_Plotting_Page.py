import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

# File system access library
import glob, os
import json

class Tutorial_Plotting_Page(tk.Frame):
        
        def __init__(self,parent,controller):
                
                # AVA app controller (app_data access)
                self.controller = controller
                
                tk.Frame.__init__(self,parent)


                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Tutorial - Plotting Page', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,20), ipadx = 2, ipady = 2, fill = "x")

                goBack_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Tutorial_Main_Page"))
                goBack_button.pack(pady=(5,5),padx=15, side = "top", expand = "no", anchor = "nw")

