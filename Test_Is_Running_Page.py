import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Delay_Bar import Delay_Bar


# File system access library
import glob, os

import json

class Test_Is_Running_Page(tk.Frame):

        # Update page with new content every 1 second                
        def poll (self):

                
                # Read json file
                with open('data.json','r') as f:
                        data = json.load(f)
                        f.close

                # Update labels with latest data
                self.label1['text'] = "Test Type: {}".format(data['test_type'])
                self.label2['text'] = "Test Duration: {}".format(data['test_duration'] + " minutes")
                self.label3['text'] = "Delay Time: {}".format(data['delay_time'] + " minutes")

                # check for changes in data every 1 second
                self.after(1000, self.poll)
                

        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                # AVA app controller (app_data access)
                self.controller = controller
                         
                label = ttk.Label(self, text="Test Is Running Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label1 = ttk.Label(self, text=str("Test Type: "))
                self.label1.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label2 = ttk.Label(self, text=str("Test Duration: "))
                self.label2.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label3 = ttk.Label(self, text=str("Delay Time: " ))
                self.label3.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToSaveTestPage_button = ttk.Button(self, text="Save Test",
                                    command=lambda: controller.show_page("Save_Test_Page"))
                goToSaveTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                goToRunTestPage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Configure_Test_Page"))
                goToRunTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                startTest_button = ttk.Button(self, text="Start test",
                                    command=lambda: self.delay(controller))
                startTest_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
                self.poll()


        def delay (self,controller):

                Delay_Bar()

