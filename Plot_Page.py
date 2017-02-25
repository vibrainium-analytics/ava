import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Plot_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text="Plot Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToHomePage_button = ttk.Button(self, text="Home",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
