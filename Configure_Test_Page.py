import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

import json

class Configure_Test_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                
                # AVA app controller (app_data access)
                self.controller = controller
                
                label = ttk.Label(self, text="Run Test Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")
                
                # Go to TestIsRunningPage 
                goToTestIsRunningPage_button = ttk.Button(self, text="Set test parameters",
                                    command=lambda: self.saveTestPreferences(controller))
                goToTestIsRunningPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                # Go back to HomePage
                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                Tests = ('Baseline - Idle', 'Baseline - 20 MPH', 'Baseline 30 MPH', 'Diagnotic - Idle', 'Diagnostic - 20 MPH')
                self.TestType1 = ttk.Labelframe(self, text='Test Type')
                self.TestType = ttk.Combobox(self.TestType1, values= Tests, state='readonly')
                self.TestType.current(0)  # set selection
                self.TestType.pack(pady=5, padx=10)
                self.TestType1.pack(in_= self, side="top", pady=20, padx=10)

                Delay = ('0', '1', '2', '5', '10')
                self.DelayTime1 = ttk.Labelframe(self, text='Delay before test begins (minutes)')
                self.DelayTime = ttk.Combobox(self.DelayTime1, values=Delay, state='readonly')
                self.DelayTime.current(0)  # set selection
                self.DelayTime.pack(pady=5, padx=10)
                self.DelayTime1.pack(in_=self, side="top", pady=20, padx=10)

                Duration = ('0', '1', '2', '5', '10', '20')
                self.TestDuration1 = ttk.Labelframe(self, text='Length of test (minutes)')
                self.TestDuration = ttk.Combobox(self.TestDuration1, values=Duration, state='readonly')
                self.TestDuration.current(0)  # set selection
                self.TestDuration.pack(pady=5, padx=10)
                self.TestDuration1.pack(in_=self, side="top", pady=20, padx=10)

        def saveTestPreferences (self,controller):
                
                data = {
                        'test_duration' : str(self.TestDuration.get()),
                        'delay_time' : str(self.DelayTime.get()),
                        'test_type' : str(self.TestType.get()),
                        }

                with open('data.json','w') as f:
                        json.dump(data,f)
                        f.close
                
                controller.show_page("Test_Is_Running_Page")

                

                
