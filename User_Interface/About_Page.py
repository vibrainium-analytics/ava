import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

# File system access library
import glob, os
import json

class About_Page(tk.Frame):

        def __init__(self,parent,controller):

                # AVA app controller (app_data access)
                self.controller = controller

                tk.Frame.__init__(self,parent)


                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='About', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,20), ipadx = 2, ipady = 2, fill = "x")

                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                Button_1 = ttk.Button(self, text="Click to see whatever #1",
                                    command=lambda: controller.show_page("To_Be_Determined_Page_1"))
                Button_1.pack(padx = 25, pady = 25, side = "left", expand = "yes", anchor = "n")

                Button_2 = ttk.Button(self, text="Click to see whatever #2",
                                    command=lambda: controller.show_page("To_Be_Determined_Page_2"))
                Button_2.pack(padx = 25, pady = 25, side = "right", expand = "yes", anchor = "n")
