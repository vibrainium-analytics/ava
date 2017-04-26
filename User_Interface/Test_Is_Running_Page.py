import tkinter as tk
from tkinter import messagebox as tmb
from tkinter import *
from tkinter import ttk
from Signal_Processing.Delay_Bar import Delay_Bar
import urllib.request

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
                        
                if data['test_duration'] == '0':
                        batlife = 'NA'
                else:
                        try:
                                battime = urllib.request.urlopen("http://192.168.1.1/B", timeout=5).read()
                                batl = int(battime.decode())
                                batlife = str(batl)
                        except (UnicodeDecodeError, urllib.error.URLError) or (OSError):
                                wifi_warning=tmb.showwarning(title="WiFi not connected", message = "Reset Wi-Fi connection and try again")
                
                # Update labels with latest data
                self.label1['text'] = "Test Type: {}".format(data['test_type'])
                self.label2['text'] = "Test Duration: {}".format(data['test_duration'] + " minutes")
                self.label3['text'] = "Delay Time: {}".format(data['delay_time'] + " minutes")
                self.label4['text'] = "Sensor Battery: {}".format(batlife + "%")
                
                if data['test_done'] == 'Yes':

                        data_t = {
                                 'test_duration' : data['test_duration'],
                                 'delay_time' : data['delay_time'],
                                 'test_type' : data['test_type'],
                                 'test_done' : 'No',
                                 'bat_life' : batlife,
                                 }

                        with open(directory['app_data'] + 'test_preferences.json','w') as f:
                            json.dump(data_t,f)
                            f.close

                        self.goToSaveTestPage_button.configure(state="normal")                            

                # check for changes in data every 1 seconds
                self.after(1000, self.poll)

        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                # AVA app controller (app_data access)
                self.controller = controller

                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Test in Progress', width=35).pack(side=TOP)
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

                self.label4 = ttk.Label(self, text=str("Sensor Battery: " ))
                self.label4.pack(pady=2,padx=2, side = "top", anchor = "n")

                startTest_button = ttk.Button(self, text="Start Test", command = lambda:self.delay(controller))
                startTest_button.pack(pady=1,padx=15,side="left",expand="no",anchor="n")

                self.goToSaveTestPage_button = ttk.Button(self, text="Save Test", state = 'disabled',
                                    command=lambda: self.save(controller))
                self.goToSaveTestPage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                

                self.poll()


        def delay (self,controller):

                with open(directory['app_data'] + 'test_preferences.json','r') as f:
                        data = json.load(f)
                        f.close

                if int(data['delay_time']) == 0 and int(data['test_duration']) == 0:
                        Delay_Bar()

                else:
                        try:
                                self = urllib.request.urlopen("http://192.168.1.1/S", timeout=5).read()
                                selftest = self.decode('ascii')
                                connect = True
                        except (UnicodeDecodeError, urllib.error.URLError) or (OSError):
                                wifi_warning=tmb.showwarning(title="WiFi not connected", message = "Reset Wi-Fi connection and try again")
                                connect = False
                        if connect == True:
                                if 'fail' in selftest:
                                    self_test_warning=tmb.showwarning(title="Self-Test Failed", message = "Check sensor for damage and restart")
                                    controller.show_page('Home_Page')
                                elif 'pass' in selftest:
                                    Delay_Bar()

        def save (self, controller):

                controller.show_page('Save_Test_Page')
                self.goToSaveTestPage_button.configure(state="disabled") 


