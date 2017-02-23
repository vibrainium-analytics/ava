import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TestIsRunningPage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text="Test Is Running Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToSaveTestPage_button = ttk.Button(self, text="Save Test",
                                    command=lambda: controller.show_page("SaveTestPage"))
                goToSaveTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                goToRunTestPage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("RunTestPage"))
                goToRunTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
