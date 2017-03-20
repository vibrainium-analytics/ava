import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from Signal_Processing.Delay_Bar import Delay_Bar


# File system access library
import glob, os

import json

class Test_Is_Running_Page(tk.Frame):

        # Update page with new content every 1 second                
        def poll (self):
                # Global directory navigation file
                with open('directory.json','r') as g:
                        global directory
                        directory = json.load(g)
                        g.close

                # Read json file
                with open(directory['app_data'] + 'test_preferences.json','r') as f:
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
                         
                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Test Is Running Page', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,20), ipadx = 2, ipady = 2, fill = "x")

                goToRunTestPage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Configure_Test_Page"))
                goToRunTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                self.label1 = ttk.Label(self, text=str("Test Type: "))
                self.label1.pack(pady = 1, padx = 2, side = "top", anchor = "n")

                self.label2 = ttk.Label(self, text=str("Test Duration: "))
                self.label2.pack(pady=2,padx=2, side = "top", anchor = "n")

                self.label3 = ttk.Label(self, text=str("Delay Time: " ))
                self.label3.pack(pady=2,padx=2, side = "top", anchor = "n")

                startTest_button = ttk.Button(self, text="Start Test", command = lambda:self.delay(controller))
                startTest_button.pack(pady=1,padx=15,side="left",expand="no",anchor="n")

                self.poll()

        # the following two functions make it so that the save button only appears after the test has begun
        # and then the save button dissapears after you press it.
        
        def delay (self,controller):

                Delay_Bar()
                
                self.goToSaveTestPage_button = ttk.Button(self, text="Save Test",
                                    command=lambda: self.save(controller))
                self.goToSaveTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")
        def save (self, controller):

                controller.show_page('Save_Test_Page')
                self.goToSaveTestPage_button.pack_forget()

