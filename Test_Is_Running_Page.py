import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Test_Is_Running_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                l
                # AVA app controller (app_data access)
                self.controller = controller
                
                abel = ttk.Label(self, text="Test Is Running Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToSaveTestPage_button = ttk.Button(self, text="Save Test",
                                    command=lambda: controller.show_page("Save_Test_Page"))
                goToSaveTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                goToRunTestPage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Run_Test_Page"))
                goToRunTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
