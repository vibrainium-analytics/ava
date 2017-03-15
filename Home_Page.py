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
<<<<<<< HEAD

                                
=======
                
>>>>>>> 70eb98ffa6e6d81118ded3bf2cc7e3403f7ac338
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
                print('Pick: ' + self.Saved_Profiles_Dropdown.get())

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

                frame1 = tk.LabelFrame(self, text="frame1", width=10, height=10, bd=5, borderwidth=4, relief=GROOVE)
                frame2 = tk.LabelFrame(self, text="frame2", width=20, height= 20, bd=5, borderwidth=4, relief=GROOVE)
                frame3 = tk.LabelFrame(self, text="frame3", width=30, height=30, bd=5, borderwidth=4, relief=GROOVE)
                
                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Home Page', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,20), ipadx = 2, ipady = 2, fill = "x")



                # Load vehicles from vehicle directory
                from os import listdir
                vehicle_filenames = os.listdir("/home/pi/ava/vehicle_profiles")
                formatted_filenames = []

                # Format filenames to remove .json extension
                for filename in vehicle_filenames:
                        formatted_filenames.append(str(('.'.join(filename.split('.')[:-1]))))
                
                # Create saved vehicle profiles dropdown menu
                self.Saved_Profiles_Frame = ttk.Labelframe(self, text='Load Saved Vehicle')
                self.Saved_Profiles_Dropdown = ttk.Combobox(self.Saved_Profiles_Frame, values = formatted_filenames, state='readonly')
                self.Saved_Profiles_Dropdown.bind('<<ComboboxSelected>>',self.loadSavedVehicleProfile)
                self.Saved_Profiles_Dropdown.pack(pady = 10, padx=10)
                self.Saved_Profiles_Frame.pack(in_=self,side="top",pady=(10, 10), padx = 10)
                
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


                self.label1 = ttk.Label(self, text="Vehicle Name: ")
                self.label1.pack(pady = (20,2), padx = 1, side = "top", anchor = "n")

                self.label2 = ttk.Label(self, text=str("Vehicle Make: "))
                self.label2.pack(pady=2,padx=1, side = "top", anchor = "n")

                self.label3 = ttk.Label(self, text=str("Vehicle Model: "))
                self.label3.pack(pady=2,padx=1, side = "top", anchor = "n")

                self.label4 = ttk.Label(self, text=str("Vehicle Year: " ))
                self.label4.pack(pady=2,padx=1, side = "top", anchor = "n")

                goToNewVehiclePage_button = ttk.Button(self, text="New Vehicle",
                                    command=lambda: controller.show_page("New_Vehicle_Page"))
                goToNewVehiclePage_button.pack(padx = 25, pady = 25, side = "left", expand = "yes", anchor = "n")

                goToRunTestPage_button = ttk.Button(self, text="Run Test",command=lambda: controller.show_page("Run_Test_Page"))
                goToRunTestPage_button.pack(padx = 25, pady = 25, side = "left", expand = "no", anchor = "n")

                goToPlotPage_button = ttk.Button(self, text="Plot",command=lambda: controller.show_page("Plot_Page"))
                goToPlotPage_button.pack(padx = 25, pady = 25, side = "left", expand = "yes", anchor = "n")

                self.ExtrasFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.ExtrasFrame, text='Extras', width=35).pack(side=BOTTOM)
                self.ExtrasFrame.pack(pady = (5,20), ipadx = 2, ipady = 2, fill = "x")


                Tutorial_Button = ttk.Button(self, text="Click here to view\n          the\n     AVA tutorial",
                                    command=lambda: controller.show_page("Tutorial_Main_Page"))
                Tutorial_Button.pack(padx = 25, pady = (3), side = "left", expand = "yes", anchor = "nw")

                About_Button = ttk.Button(self, text="  Click here to view\n        info about\nVibrainium Analytics\n           and\n    the AVA system",
                                    command=lambda: controller.show_page("About_Page"))
                About_Button.pack(padx = 25, pady = (3), side = "right", expand = "yes", anchor = "ne")



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


        class Signal_Process(tk.Tk):

            def __init__(self,*args):
                tk.Tk.__init__(self,*args)
                self.message = tk.Text(self, height=2, width=30)
                self.message.pack()
                self.message.insert(tk.INSERT, "Tutorial will be built out here...")
                self.title('About..')
