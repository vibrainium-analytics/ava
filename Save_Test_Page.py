import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Save_Test_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text="Save Test Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToResultsPage_button = ttk.Button(self, text="Results",
                                    command=lambda: controller.show_page("Results_Page"))
                goToResultsPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
