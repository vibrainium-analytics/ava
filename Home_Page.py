import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

# File system access library
import glob, os
import json

class Home_Page(tk.Frame):
        # Update page with new content every 1 second                
        def poll (self):

                # Read json file
                with open('/home/pi/ava/selected_vehicle.json','r') as f:
                        data = json.load(f)
                        f.close

                # Update labels with latest data
                self.label1['text'] = "Vehicle Name: {}".format(data['name'])
                self.label2['text'] = "Vehicle Make: {}".format(data['make'])
                self.label3['text'] = "Vehicle Model: {}".format(data['model'])
                self.label4['text'] = "Vehicle Year: {}".format(data['year'])
                
                # check for changes in data every 1 second
                self.after(1000, self.poll)

        def loadSavedVehicleProfile (self, event):
                # Read json file
                with open('/home/pi/ava/vehicle_profiles/' + self.Saved_Profiles_Dropdown.get() + '.json','r') as f:
                        data = json.load(f)
                        f.close
                # Write saved_vehicle status folder
                with open('selected_vehicle.json', 'w') as f:
                        json.dump(data,f)
                        f.close
                # Update labels with latest data
                self.label1['text'] = "Vehicle Name: {}".format(data['name'])
                self.label2['text'] = "Vehicle Make: {}".format(data['make'])
                self.label3['text'] = "Vehicle Model: {}".format(data['model'])
                self.label4['text'] = "Vehicle Year: {}".format(data['year'])
                
        def __init__(self,parent,controller):
                
                # AVA app controller (app_data access)
                self.controller = controller
                
                tk.Frame.__init__(self,parent)

                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Home Page', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,5), ipadx = 2, ipady = 2, fill = "x")

                # Load vehicles from vehicle directory
                from os import listdir
                vehicle_filenames = os.listdir("/home/pi/ava/vehicle_profiles")
                formatted_filenames = []

                # Format filenames to remove .json extension
                for filename in vehicle_filenames:
                        formatted_filenames.append(str(('.'.join(filename.split('.')[:-1]))))
                
                # Create saved vehicle profiles dropdown menu
                self.Saved_Profiles_Frame = ttk.Labelframe(self, text='Load Saved Vehicle', width=40, height=30, borderwidth=5, relief=GROOVE)
                self.Saved_Profiles_Dropdown = ttk.Combobox(self.Saved_Profiles_Frame, values = formatted_filenames, state='readonly')
                self.Saved_Profiles_Dropdown.bind('<<ComboboxSelected>>',self.loadSavedVehicleProfile)
                self.Saved_Profiles_Dropdown.pack(pady = 5, padx=5)
                self.Saved_Profiles_Frame.pack(side="top",pady=(4, 2), padx = 10, ipadx = 10, ipady = 15)
                
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

                        

                frame1 = tk.LabelFrame(self.Saved_Profiles_Frame, text="Active Vehicle Profile", width=30, height=25, bd=1, borderwidth=3, relief=GROOVE)
                frame1.pack(padx = 3, pady = 1, ipadx = 10, ipady = 1)

                frame2 = tk.LabelFrame(self, text="Control Center", width=25, height=35, bd=1, borderwidth=5, relief="groove")
                frame2.pack(side = "top", pady = (8,8), ipadx = 5, ipady = 5)

                frame3 = tk.LabelFrame(self, text="Extras", bd=1, borderwidth=4, relief=GROOVE)
                frame3.pack(side = "bottom", pady = (25,5), ipadx = 10, ipady = 5)



                self.label1 = ttk.Label(frame1, text="Vehicle Name: ")
                self.label1.pack(pady = (10,2), padx = 1, side = "top", anchor = "n")

                self.label2 = ttk.Label(frame1, text=str("Vehicle Make: "))
                self.label2.pack(pady=2,padx=1, side = "top", anchor = "n")

                self.label3 = ttk.Label(frame1, text=str("Vehicle Model: "))
                self.label3.pack(pady=2,padx=1, side = "top", anchor = "n")

                self.label4 = ttk.Label(frame1, text=str("Vehicle Year: " ))
                self.label4.pack(pady=2,padx=1, side = "top", anchor = "n")

                goToNewVehiclePage_button = ttk.Button(frame2, text="New Vehicle",
                                    command=lambda: controller.show_page("New_Vehicle_Page"))
                goToNewVehiclePage_button.pack(padx = 18, pady = 5, side = "left", expand = "yes", anchor = "n")

                goToRunTestPage_button = ttk.Button(frame2, text="Configure/Run Test",command=lambda: controller.show_page("Configure_Test_Page"))
                goToRunTestPage_button.pack(padx = 18, pady = 5, side = "left", expand = "no", anchor = "n")

                goToPlotPage_button = ttk.Button(frame2, text="Plot",command=lambda: controller.show_page("Plot_Page"))
                goToPlotPage_button.pack(padx = 18, pady = 5, side = "left", expand = "yes", anchor = "n")

                Tutorial_Button = ttk.Button(frame3, text="AVA tutorial",
                                    command=lambda: controller.show_page("Tutorial_Main_Page"))
                Tutorial_Button.pack(padx = 25, pady = 7, side = "left", expand = "yes", anchor = "nw")

                About_Button = ttk.Button(frame3, text="About Vibrainium Analytics...",
                                    command=lambda: controller.show_page("About_Page"))
                About_Button.pack(padx = 25, pady = 7, side = "right", expand = "yes", anchor = "ne")



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

