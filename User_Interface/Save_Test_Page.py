import tkinter as tk
from tkinter import messagebox as tmb
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
                Label(self.pageLabelFrame, text='Save Test', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,5), ipadx = 2, ipady = 2, fill = "x")

                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Configure_Test_Page"))
                goToHomePage_button.pack(pady=1,padx=5, side = "left", expand = "no", anchor = "n")


                frame1 = tk.LabelFrame(self, text="Post-Test parameter entry", width=60, height=60, bd=1, borderwidth=3, relief=GROOVE)
                frame1.place(rely = 0.5, relx = 0.5,anchor= CENTER)

                Idle_Status = ('Yes', 'No')
                self.Idle_Status1 = ttk.Labelframe(frame1, text='Was this an Idle test?')
                self.Idle_Status = ttk.Combobox(self.Idle_Status1, values=Idle_Status, state='readonly')
                self.Idle_Status.current(0)  # set selection
                self.Idle_Status.pack(pady=5, padx=10)
                self.Idle_Status1.pack(side="top", pady=10, padx=10, ipady = 2, ipadx = 2)

                AC_Status = ('AC Off', 'AC On')
                self.AC_Status1 = ttk.Labelframe(frame1, text='AC Status')
                self.AC_Status = ttk.Combobox(self.AC_Status1, values= AC_Status, state='readonly')
                self.AC_Status.current(0)  # set selection
                self.AC_Status.pack(pady=5, padx=10)
                self.AC_Status1.pack(side="top", pady=8, padx=10, ipady = 2, ipadx = 2)

                Speeds = ('10', '20', '30', '40', '50', '60', '70', '80')
                self.Speeds1 = ttk.Labelframe(frame1, text='Speed')
                self.Speeds = ttk.Combobox(self.Speeds1, values=Speeds, state='readonly')
                self.Speeds.current(0)  # set selection
                self.Speeds.pack(pady=5, padx=10)
                self.Speeds1.pack(side="top", pady = 8, padx = 10, ipady = 2, ipadx = 2)

                Gears = ('1', '2', '3', '4', '5', '6')
                self.Gears1 = ttk.Labelframe(frame1, text='Gear')
                self.Gears = ttk.Combobox(self.Gears1, values=Gears, state='readonly')
                self.Gears.current(0)  # set selection
                self.Gears.pack(pady=5, padx=10)
                self.Gears1.pack(side="top", pady = 8, padx = 10, ipady = 2, ipadx = 2)

                goToResultsPage_button = ttk.Button(frame1, text="View Results",
                                    command=lambda: self.saveTestSettings(controller))
                goToResultsPage_button.pack(pady=8,padx=5, side = "top", expand = "no", anchor = "n")

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

                gear_int = int(self.Gears.get())
                gear_string = ""
                if gear_int == 1: gear_string = 'first_Gear'
                if gear_int == 2: gear_string = 'second_Gear'
                if gear_int == 3: gear_string = 'third_Gear'
                if gear_int == 4: gear_string = 'fourth_Gear'
                if gear_int == 5: gear_string = 'fifth_Gear'
                if gear_int == 6: gear_string = 'sixth_Gear'

                save_test_settings = {
                        'ac_status' : str(self.AC_Status.get()),
                        'idle_status' :str(self.Idle_Status.get()),
                        'speed' : str(speed),
                        'gear' : gear_string
                        }

                with open(directory['app_data'] + 'save_test.json','w') as f:
                        json.dump(save_test_settings,f)
                        f.close
                with open(directory['app_data'] + 'test_preferences.json','r') as f:
                    test_data = json.load(f)
                    f.close
                with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                    data1 = json.load(f)
                    f.close
                with open(directory['app_data'] + 'save_test.json','r') as f:
                    data2 = json.load(f)
                    f.close 

                # set AC status and speed status dependancies
                if str(data2['idle_status']) == 'Yes':
                    testnm = '-Idle'
                    if str(data2['ac_status']) == 'AC On':
                        testnm = testnm + '-AC'
                else:
                    testnm = '-' + str(data2['speed']+ 'mph')
                    
                path_base = str(directory['veh_path']) + str(data1['name']) + '_' + str(data1['model'])+ '_' + str(data1['year_Veh']) + '/Baseline' + testnm + '/'
                if os.path.exists(path_base) and str(test_data["test_type"]) == 'Baseline' :
                        base_warn=tmb.askquestion(title="Warning Baseline Overwrite", message = "Do you want overwrite baseline data?")
                        if base_warn == 'no' :
                                controller.show_page("Home_Page")
                                print('no overwrite')
                        elif base_warn == 'yes' :
                                controller.show_page("Results_Page")
                                Signal_Process()
                                print('overwrite')
                        else:
                                print('not right')
                else:
                        controller.show_page("Results_Page")
                        Signal_Process()
                        print('no baseline conflict')
