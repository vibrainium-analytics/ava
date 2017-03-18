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
                home = str(directory['home'])
                with open(home + 'selected_vehicle.json','r') as f:
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

                veh_path = str(directory['veh_path'])

                # Save to json file (in vehicle profiles folder)
                with open(veh_path + self.Saved_Profiles_Dropdown.get() + '.json','r') as f:
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

                with open('directory.json','r') as f:
                    global directory
                    directory = json.load(f)
                    f.close
                veh_path = str(directory['veh_path']) 
                
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

                        
                # Load vehicles from vehicle directory
                from os import listdir
                vehicle_filenames = os.listdir(veh_path)
                formatted_filenames = []

                # Format filenames to remove .json extension
                for filename in vehicle_filenames:
                        formatted_filenames.append(str(('.'.join(filename.split('.')[:-1]))))
                
                # Create saved vehicle profiles dropdown menu
                self.Saved_Profiles_Frame = ttk.Labelframe(self, text='Load Saved Vehicle')
                self.Saved_Profiles_Dropdown = ttk.Combobox(self.Saved_Profiles_Frame, values = formatted_filenames, state='readonly')
                self.Saved_Profiles_Dropdown.bind('<<ComboboxSelected>>',self.loadSavedVehicleProfile)
                self.Saved_Profiles_Dropdown.pack(pady=5,padx=10)
                self.Saved_Profiles_Frame.pack(in_=self,side="top",pady=20,padx=10)
                
                
                
                self.poll()
