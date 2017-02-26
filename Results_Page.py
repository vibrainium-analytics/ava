import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

import json
class Results_Page(tk.Frame):
        # Update page with new content every 1 second                
        def poll (self):

                os.chdir("/home/pi/ava/vehicle_profiles/")
                
                # Read json file
                with open('data2.json','r') as f:
                        data = json.load(f)

                # Update labels with latest data
                self.label1['text'] = "AC Status: {}".format(data['ac_status'])
                self.label2['text'] = "Idle Status: {}".format(data['idle_status'])
                self.label3['text'] = "Speed: {}".format(data['speed'])
                
                # check for changes in data every 1 second
                self.after(1000, self.poll)

        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                # AVA app controller (app_data access)
                self.controller = controller
                
                label = ttk.Label(self, text="Results Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label1 = ttk.Label(self, text="AC Status: ")
                self.label1.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label2 = ttk.Label(self, text=str("Idle Status: "))
                self.label2.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label3 = ttk.Label(self, text=str("Speed: "))
                self.label3.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToPlotPage_button = ttk.Button(self, text="Result Plots",
                                    command=lambda: controller.show_page("Plot_Page"))
                goToPlotPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                self.poll()
