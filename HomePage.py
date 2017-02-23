import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class StartPage(tk.Frame):

        def __init__(self,parent,controller)
                tk.Frame.__init__(self,parent)

                label = ttk.Label(self, text="Home Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")


                goToRunTestPage_button = ttk.Button(self,text="Run Test",command=lambda: controller.show_page("RunTestPage"))
                goToRunTestPage_button.pack(pady=1, padx = 15, side = "left", expand = "no", anchor = "n")

                goToPlotPage_button = ttk.Button(self, text="Plot",command=lambda: controller.show_page("PlotPage"))
                dataCollectButton.pack(side = "right", expand = "yes", anchor = "n")

                goToNewVehiclePage_button = ttk.Button(self, text="New Car",
                                    command=lambda: controller.show_page("NewVehiclePage"))
                goToNewVehiclePage_button.pack(side = "right", expand = "yes", anchor = "n")

