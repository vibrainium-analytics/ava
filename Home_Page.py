import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os
import json

class Home_Page(tk.Frame):
        # Update page with new content every 1 second                
        def poll (self):
                
                # Read json file
                with open('data1.json','r') as f:
                        data = json.load(f)
                        f.close

                # Update labels with latest data
                self.label1['text'] = "Vehicle Name: {}".format(data['name'])
                self.label2['text'] = "Vehicle Make: {}".format(data['make'])
                self.label3['text'] = "Vehicle Model: {}".format(data['model'])
                self.label4['text'] = "Vehicle Year: {}".format(data['year'])

                # check for changes in data every 1 second
                self.after(1000, self.poll)

        def __init__(self,parent,controller):
                
                # AVA app controller (app_data access)
                self.controller = controller
                
                tk.Frame.__init__(self,parent)

                label = ttk.Label(self, text="Home Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label1 = ttk.Label(self, text="Vehicle Name: ")
                self.label1.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label2 = ttk.Label(self, text=str("Vehicle Make: "))
                self.label2.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label3 = ttk.Label(self, text=str("Vehicle Model: "))
                self.label3.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label4 = ttk.Label(self, text=str("Vehicle Year: " ))
                self.label4.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToRunTestPage_button = ttk.Button(self,text="Run Test",command=lambda: controller.show_page("Configure_Test_Page"))
                goToRunTestPage_button.pack(pady=1, padx = 15, side = "left", expand = "no", anchor = "n")

                goToPlotPage_button = ttk.Button(self, text="Plot",command=lambda: controller.show_page("Plot_Page"))
                goToPlotPage_button.pack(side = "right", expand = "yes", anchor = "n")

                goToNewVehiclePage_button = ttk.Button(self, text="New Vehicle",
                                    command=lambda: controller.show_page("New_Vehicle_Page"))
                goToNewVehiclePage_button.pack(side = "right", expand = "yes", anchor = "n")

                # defaule settings for directories
                
                path = "/home/pi/ava/"
                veh_prof_path = path + "vehicle_profiles/"
                os.chdir(path)

                data = {
                        'path' : str(path),
                        'veh_path' : str(veh_prof_path),
                        }
                with open('directory.json', 'w') as f:
                        json.dump(data,f)
                        f.close

                # default settings for data.json

                data = {
                        'test_type' : 'Baseline-Idle',
                        'delay_time' : '0',
                        'test_duration' : '0',
                        }
                
                with open('data.json','w') as f:
                        json.dump(data,f)
                        f.close
                
                self.poll()
