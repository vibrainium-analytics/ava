import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class RunTestPage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text="Run Test Page")
                label.pack(pady=1,padx=1, side = "top", anchor = N)

                goToHomePage_button = ttk.Button(self, text="Home",
                                    command=lambda: controller.show_page("HomePage"))
                goToHomePage_button.pack(pady=1,padx=15, side = LEFT, expand = NO, anchor = N)
