import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class New_Vehicle_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text="New Vehicle Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToHomePage_button = ttk.Button(self, text="Home",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                D = ('0 Seconds', '30 seconds', '60 seconds', '90 seconds', '120 seconds')
                DT1 = ttk.Labelframe(self, text='Pre-defined - some will need this (cylinders) while other will need enterable fields')
                DT = ttk.Combobox(DT1, values=D, state='readonly')
                DT.current(0)  # set selection
                DT.pack(pady=5, padx=10)
                DT1.pack(in_=self, side="top", pady=20, padx=10)
