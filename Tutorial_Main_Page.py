import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

# File system access library
import glob, os
import json

class Tutorial_Main_Page(tk.Frame):
        
        def __init__(self,parent,controller):
                
                # AVA app controller (app_data access)
                self.controller = controller
                
                tk.Frame.__init__(self,parent)


                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Main Tutorial Page', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,20), ipadx = 2, ipady = 2, fill = "x")


                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=(5,5),padx=15, side = "top", expand = "no", anchor = "nw")


 
                Plot_Tutorial_Button = ttk.Button(self, text="Plotting Tutorial",
                                    command=lambda: controller.show_page("Tutorial_Plotting_Page"))
                Plot_Tutorial_Button.pack(padx = 25, pady = 25, side = "left", expand = "yes", anchor = "n")

                Plot_Tutorial_Button = ttk.Button(self,text="Sample Collection Tutorial",command=lambda: controller.show_page("Tutorial_Sample_Collection_Page"))
                Plot_Tutorial_Button.pack(padx = 25, pady = 25, side = "left", expand = "no", anchor = "n")

                Plot_Tutorial_Button = ttk.Button(self, text="Vehicle Profile Creation Tutorial",command=lambda: controller.show_page("Tutorial_Vehicle_Creation_Page"))
                Plot_Tutorial_Button.pack(padx = 25, pady = 25, side = "right", expand = "yes", anchor = "n")


