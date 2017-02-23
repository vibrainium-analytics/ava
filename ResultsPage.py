import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ResultsPage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text="Results Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToPlotPage_button = ttk.Button(self, text="Result Plots",
                                    command=lambda: controller.show_page("PlotPage"))
                goToPlotPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
