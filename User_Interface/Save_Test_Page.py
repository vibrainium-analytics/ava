import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from Signal_Processing.Signal_Process import Signal_Process

# File system access library
import glob, os

import json

class Save_Test_Page(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                # AVA app controller (app_data access)
                self.controller = controller

                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Configure/Run Test Page', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,5), ipadx = 2, ipady = 2, fill = "x")

                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Configure_Test_Page"))
                goToHomePage_button.pack(pady=1,padx=5, side = "left", expand = "no", anchor = "n")


                frame1 = tk.LabelFrame(self, text="Post-Test parameter entry", width=60, height=60, bd=1, borderwidth=3, relief=GROOVE)
                frame1.place(rely = 0.5, relx = 0.5,anchor= CENTER)

                AC_Status = ('AC Off', 'AC On')
                self.AC_Status1 = ttk.Labelframe(frame1, text='AC Status')
                self.AC_Status = ttk.Combobox(self.AC_Status1, values= AC_Status, state='readonly')
                self.AC_Status.current(0)  # set selection
                self.AC_Status.pack(pady=5, padx=10)
                self.AC_Status1.pack(side="top", pady=20, padx=10, ipady = 2, ipadx = 2)

                Idle_Status = ('Yes', 'No')
                self.Idle_Status1 = ttk.Labelframe(self, text='Under Idle?')
                self.Idle_Status = ttk.Combobox(self.Idle_Status1, values=Idle_Status, state='readonly')
                self.Idle_Status.current(0)  # set selection
                self.Idle_Status.pack(pady=5, padx=10)
                self.Idle_Status1.pack(side="top", pady=20, padx=10, ipady = 2, ipadx = 2)

                Speeds = ('10', '10', '30', '40', '50', '60', '70', '80')
                self.Speeds1 = ttk.Labelframe(frame1, text='Speed')
                self.Speeds = ttk.Combobox(self.Speeds1, values=Speeds, state='readonly')
                self.Speeds.current(0)  # set selection
                self.Speeds.pack(pady=5, padx=10)
                self.Speeds1.pack(side="top", pady = 20, padx = 10, ipady = 2, ipadx = 2)

                goToResultsPage_button = ttk.Button(frame1, text="View Results",
                                    command=lambda: self.saveTestSettings(controller))
                goToResultsPage_button.pack(pady=15,padx=5, side = "top", expand = "no", anchor = "n")

        def saveTestSettings (self,controller):
                 # Global directory navigation file
                with open('directory.json','r') as g:
                        global directory
                        directory = json.load(g)
                        g.close
                        
                # if you are at idle the speed is 0. this makes it so that the speed cannot be above 0 at idle
                
                if str(self.Idle_Status.get()) == 'Yes':
                        speed = 0
                else:
                        speed = self.Speeds.get()

                # if you are at idle the speed is 0. this makes it so that the speed cannot be above 0 at idle
                
                if str(self.Idle_Status.get()) == 'Yes':
                        speed = 0
                else:
                        speed = self.Speeds.get()


                data = {
                        'ac_status' : str(self.AC_Status.get()),
                        'idle_status' :str(self.Idle_Status.get()),
                        'speed' : str(speed),
                        }

                with open(directory['app_data'] + 'save_test.json','w') as f:
                        json.dump(data,f)
                        f.close
                
                controller.show_page("Results_Page")
                Signal_Process()

                
