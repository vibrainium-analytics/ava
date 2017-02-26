import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

import json

class Save_Test_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                # AVA app controller (app_data access)
                self.controller = controller
                
                label = ttk.Label(self, text="Save Test Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToResultsPage_button = ttk.Button(self, text="Results",
                                    command=lambda: self.saveTestSettings(controller))
                goToResultsPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                AC_Status = ('AC Off', 'AC On')
                self.AC_Status1 = ttk.Labelframe(self, text='AC Status')
                self.AC_Status = ttk.Combobox(self.AC_Status1, values= AC_Status, state='readonly')
                self.AC_Status.current(0)  # set selection
                self.AC_Status.pack(pady=5, padx=10)
                self.AC_Status1.pack(in_= self, side="top", pady=20, padx=10)

                Idle_Status = ('Yes', 'No', '60 seconds', '90 seconds', '120 seconds')
                self.Idle_Status1 = ttk.Labelframe(self, text='Under Idle?')
                self.Idle_Status = ttk.Combobox(self.Idle_Status1, values=Idle_Status, state='readonly')
                self.Idle_Status.current(0)  # set selection
                self.Idle_Status.pack(pady=5, padx=10)
                self.Idle_Status1.pack(in_=self, side="top", pady=20, padx=10)

                Speeds = ('10', '10', '30', '40', '50', '60', '70', '80')
                self.Speeds1 = ttk.Labelframe(self, text='Speed')
                self.Speeds = ttk.Combobox(self.Speeds1, values=Speeds, state='readonly')
                self.Speeds.current(0)  # set selection
                self.Speeds.pack(pady=5, padx=10)
                self.Speeds1.pack(in_=self, side="top", pady=20, padx=10)

        def saveTestSettings (self,controller):

                os.chdir("/home/pi/ava/vehicle_profiles/")

                data = {
                        'ac_status' : str(self.AC_Status.get()),
                        'idle_status' : str(self.Idle_Status.get()),
                        'speed' : str(self.Speeds.get()),
                        }

                with open('data2.json','w') as f:
                        json.dump(data,f)
                
                controller.show_page("Results_Page")

                
