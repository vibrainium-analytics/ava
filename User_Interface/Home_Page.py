import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import urllib.request

# File system access library
import glob, os
import json

class Home_Page(tk.Frame):
        # Update page with new content every 1 second
        def poll (self):
                with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close

                # Update labels with latest data
                self.label1['text'] = "Vehicle Name: {}".format(selected_vehicle['name'])
                self.label2['text'] = "Vehicle Make: {}".format(selected_vehicle['make'])
                self.label3['text'] = "Vehicle Model: {}".format(selected_vehicle['model'])
                self.label4['text'] = "Vehicle Year: {}".format(selected_vehicle['year_Veh'])

                try:
                        self = urllib.request.urlopen("http://192.168.1.1/S", timeout=1).read()
                        selftest = self.decode('ascii')
                        connect = True
                except (UnicodeDecodeError, urllib.error.URLError) or (OSError):
                        connect = False
                if connect == True:
                        self.label5['text'] = "Wi-Fi Connection: Connected"
                else:
                        self.label5['text'] = "Wi-Fi Connection: Disconnected"
                         

                # check for changes in data every 10 seconds
                self.after(1000, self.poll)

        def loadSavedVehicleProfile (self, event):
                # Save to json file (in vehicle profiles folder)
                with open(directory['veh_path'] + self.Saved_Profiles_Dropdown.get() + '.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close

                # Write saved_vehicle status folder
                with open(directory['app_data'] + 'selected_vehicle.json', 'w') as f:
                        json.dump(selected_vehicle,f)
                        f.close
                # Update labels with latest data
                self.label1['text'] = "Vehicle Name: {}".format(selected_vehicle['name'])
                self.label2['text'] = "Vehicle Make: {}".format(selected_vehicle['make'])
                self.label3['text'] = "Vehicle Model: {}".format(selected_vehicle['model'])
                self.label4['text'] = "Vehicle Year: {}".format(selected_vehicle['year_Veh'])

        def refresh(self):
                # Load vehicles from vehicle directory
                from os import listdir
                vehicle_filenames = os.listdir(directory["veh_path"])
                formatted_filenames = []

                # Format filenames to remove .json extension
                for filename in vehicle_filenames:
                        if filename.endswith(".json"):
                                formatted_filenames.append(str(('.'.join(filename.split('.')[:-1]))))

                self.Saved_Profiles_Dropdown['values'] = formatted_filenames

        def __init__(self,parent,controller):
                # Global directory navigation file
                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

                veh_path = str(directory['veh_path'])

                # AVA app controller (app_data access)
                self.controller = controller

                tk.Frame.__init__(self,parent)

                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Home', width=97).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,5), ipadx = 2, ipady = 2, fill = "both")

                # Load vehicles from vehicle directory
                from os import listdir
                vehicle_filenames = os.listdir(directory['veh_path'])
                formatted_filenames = []

                # Format filenames to remove .json extension
                for filename in vehicle_filenames:
                        if filename.endswith(".json"):
                                formatted_filenames.append(str(('.'.join(filename.split('.')[:-1]))))

                # Create saved vehicle profiles dropdown menu
                self.Saved_Profiles_Frame = ttk.Labelframe(self, text='Load Saved Vehicle', width=40, height=30, borderwidth=5, relief=GROOVE)
                self.Saved_Profiles_Dropdown = ttk.Combobox(self.Saved_Profiles_Frame, postcommand = self.refresh, state='readonly')
                self.Saved_Profiles_Dropdown.bind('<<ComboboxSelected>>',self.loadSavedVehicleProfile)
                self.Saved_Profiles_Dropdown.pack(pady = 5, padx=5)
                self.Saved_Profiles_Frame.pack(side="top",pady=(4, 2), padx = 10, ipadx = 10, ipady = 15)

                # Default settings for test_preferences.json
                test_preferences = {
                        'test_type' : 'Baseline-Idle',
                        'delay_time' : '0',
                        'test_duration' : '0',
                        'test_done' : 'No',
                        }

                with open(directory['app_data'] + 'test_preferences.json','w') as f:
                        json.dump(test_preferences,f)
                        f.close

                frame1 = tk.LabelFrame(self.Saved_Profiles_Frame, text="Active Vehicle Profile", width=30, height=25, bd=1, borderwidth=3, relief=GROOVE)
                frame1.pack(padx = 3, pady = 1, ipadx = 5, ipady = 1)

                frame2 = tk.LabelFrame(self, text="Control Center", width=25, height=35, bd=1, borderwidth=5, relief="groove")
                frame2.pack(side = "top", pady = (8,8), ipadx = 5, ipady = 2)

                frame3 = tk.LabelFrame(self, text="Extras", bd=1, borderwidth=4, relief=GROOVE)
                frame3.pack(side = "top", pady = (10,10), ipadx = 5, ipady = 2)

                frame4 = tk.LabelFrame(self, text="", width = 30, height = 10, bd=1, borderwidth=2, relief=GROOVE)
                frame4.pack(side = "top", pady = (12,12), ipadx = 5, ipady = 2)



                self.label1 = ttk.Label(frame1, text="Vehicle Name: ")
                self.label1.pack(pady = (10,2), padx = 1, side = "top", anchor = "n")

                self.label2 = ttk.Label(frame1, text=str("Vehicle Make: "))
                self.label2.pack(pady=2,padx=1, side = "top", anchor = "n")

                self.label3 = ttk.Label(frame1, text=str("Vehicle Model: "))
                self.label3.pack(pady=2,padx=1, side = "top", anchor = "n")

                self.label4 = ttk.Label(frame1, text=str("Vehicle Year: " ))
                self.label4.pack(pady=2,padx=1, side = "top", anchor = "n")

                self.label5 = ttk.Label(frame4, text=str("Wi-Fi Connection: " ))
                self.label5.pack(pady=2,padx=1, side = "top", anchor = "n")

                goToNewVehiclePage_button = ttk.Button(frame2, text="Profile",
                                    command=lambda: controller.show_page("New_Vehicle_Page"))
                goToNewVehiclePage_button.pack(padx = 18, pady = (8,2), side = "left", expand = "yes", anchor = "n")

                goToRunTestPage_button = ttk.Button(frame2, text="Test",command=lambda: controller.show_page("Configure_Test_Page"))
                goToRunTestPage_button.pack(padx = 18, pady = (8,2), side = "left", expand = "no", anchor = "n")

                goToPlotPage_button = ttk.Button(frame2, text="Plot",command=lambda: controller.show_page("Plot_Page"))
                goToPlotPage_button.pack(padx = 18, pady = (8,2), side = "left", expand = "yes", anchor = "n")

                Tutorial_Button = ttk.Button(frame3, text="Tutorial",
                                    command=lambda: controller.show_page("Tutorial_Main_Page"))
                Tutorial_Button.pack(padx = 25, pady = (8,2), side = "left", expand = "yes", anchor = "nw")

                About_Button = ttk.Button(frame3, text="About",
                                    command=lambda: controller.show_page("About_Page"))

                About_Button.pack(padx = 25, pady = (8,2), side = "right", expand = "yes", anchor = "ne")
                #About_Button.pack(padx = 25, pady = 7, side = "right", expand = "yes", anchor = "ne")

                self.poll()
