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
                goToTestIsRunningPage_button = ttk.Button(self, text="Start test",
                                    command=lambda: self.saveTestPreferences(controller))
                goToTestIsRunningPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                # Go back to HomePage
                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                Tests = ('Baseline - Idle', 'Baseline - 20 MPH', 'Baseline 30 MPH', 'Diagnotic - Idle', 'Diagnostic - 20 MPH')
                TestType1 = ttk.Labelframe(self, text='Test Type')
                TestType = ttk.Combobox(TestType1, values= Tests, state='readonly')
                TestType.current(0)  # set selection
                TestType.pack(pady=5, padx=10)
                TestType1.pack(in_= self, side="top", pady=20, padx=10)

                Delay = ('0 Seconds', '30 seconds', '60 seconds', '90 seconds', '120 seconds')
                DelayTime1 = ttk.Labelframe(self, text='Delay before sampling begins')
                DelayTime = ttk.Combobox(DelayTime1, values=Delay, state='readonly')
                DelayTime.current(0)  # set selection
                DelayTime.pack(pady=5, padx=10)
                DelayTime1.pack(in_=self, side="top", pady=20, padx=10)

                Duration = ('1 minute', '2 minutes', '5 minutes', '10 minutes', '20 minutes')
                TestDuration1 = ttk.Labelframe(self, text='Sample size - time')
                TestDuration = ttk.Combobox(TestDuration1, values=Duration, state='readonly')
                TestDuration.current(0)  # set selection
                TestDuration.pack(pady=5, padx=10)
                TestDuration1.pack(in_=self, side="top", pady=20, padx=10)

        def saveTestPreferences (self,controller):

                os.chdir("/home/pi/ava/vehicle_profiles/")

                data = {
                        'make' : 'Honda',
                        'model' : 'Odyssey',
                        'year' : 2014,
                        }

                with open('data.json','w') as f:
                        json.dump(data,f)
                
                controller.show_page("Test_Is_Running_Page")

                
