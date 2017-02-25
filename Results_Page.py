import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Results_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                # AVA app controller (app_data access)
                self.controller = controller
                
                label = ttk.Label(self, text="Results Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToPlotPage_button = ttk.Button(self, text="Result Plots",
                                    command=lambda: controller.show_page("Plot_Page"))
                goToPlotPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
