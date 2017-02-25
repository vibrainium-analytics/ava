import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

import json


class Test_Is_Running_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                # AVA app controller (app_data access)
                self.controller = controller

                os.chdir("/home/pi/ava/vehicle_profiles/")

                # Read json file
                with open('data.json','r') as f:
                        data = json.load(f)
                        
                label = ttk.Label(self, text="Test Is Running Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                label1 = ttk.Label(self, text=str("Test Type: " + data['test_type']))
                label1.pack(pady=1,padx=1, side = "top", anchor = "n")

                label2 = ttk.Label(self, text=str("Test Duration: " + data['test_duration']))
                label2.pack(pady=1,padx=1, side = "top", anchor = "n")

                label3 = ttk.Label(self, text=str("Delay Time: " + data['delay_time']))
                label3.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToSaveTestPage_button = ttk.Button(self, text="Save Test",
                                    command=lambda: controller.show_page("Save_Test_Page"))
                goToSaveTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                goToRunTestPage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Configure_Test_Page"))
                goToRunTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
