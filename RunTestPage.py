import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class RunTestPage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text="Run Test Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToTestIsRunningPage_button = ttk.Button(self, text="Start test",
                                    command=lambda: controller.show_page("TestIsRunningPage"))
                goToTestIsRunningPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
