import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

# File system access library
import glob, os

import json

class Configure_Test_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                # Global directory navigation file
                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

                # AVA app controller (app_data access)
                self.controller = controller

                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Configure/Run Test Page', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,5), ipadx = 2, ipady = 2, fill = "x")

                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=5, side = "left", expand = "no", anchor = "n")

                frame1 = tk.LabelFrame(self, text="Pre-Test parameter entry", width=60, height=60, bd=1, borderwidth=3, relief=GROOVE)
                frame1.place(rely = 0.5, relx = 0.5,anchor= CENTER)

                Tests = ('Baseline', 'Diagnostic')
                self.TestType1 = ttk.Labelframe(frame1, text='Test Type')

                self.TestType = ttk.Combobox(self.TestType1, values= Tests, state='readonly')
                self.TestType.current(0)  # set selection
                self.TestType.pack(pady=5, padx=10)
                self.TestType1.pack(side="top", pady=10, padx=10)

                Duration = ('0', '1', '2', '5', '10', '20')
                self.TestDuration1 = ttk.Labelframe(frame1, text='Length of test (minutes)')
                self.TestDuration = ttk.Combobox(self.TestDuration1, values=Duration, state='readonly')
                self.TestDuration.current(0)  # set selection
                self.TestDuration.pack(pady=5, padx=10)
                self.TestDuration1.pack(side="top", pady=10, padx=10)

                Delay = ('0', '1', '2', '5', '10')
                self.DelayTime1 = ttk.Labelframe(frame1, text='Delay before test begins (minutes)')
                self.DelayTime = ttk.Combobox(self.DelayTime1, values=Delay, state='readonly')
                self.DelayTime.current(0)  # set selection
                self.DelayTime.pack(pady=5, padx=10)
                self.DelayTime1.pack(side="top", pady=10, padx=10)

                # Go to TestIsRunningPage
                goToTestIsRunningPage_button = ttk.Button(frame1, text="Begin Testing Sequence",
                                                        command=lambda: self.saveTestPreferences(controller))
                goToTestIsRunningPage_button.pack(pady=(15,10),padx=15, side = "top", expand = "no", anchor = "n")

        def saveTestPreferences (self,controller):

                # Global directory navigation file
                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

                data = {
                        'test_duration' : str(self.TestDuration.get()),
                        'delay_time' : str(self.DelayTime.get()),
                        'test_type' : str(self.TestType.get()),
                        }

                with open(directory['app_data'] + 'test_preferences.json','w') as f:
                        json.dump(data,f)
                        f.close

                controller.show_page("Test_Is_Running_Page")
