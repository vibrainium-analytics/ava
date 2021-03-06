import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
# File system access library
import glob, os
import json

# Math functions library
import numpy as np

import matplotlib
# Plotting library canvas tool
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

# Import plotting libraries
import matplotlib.pyplot as pl
import matplotlib, sys
import matplotlib.animation as animation
from matplotlib import style

# Plotting library canvas tool
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
matplotlib.use('TkAgg')

fig = Figure(figsize=(6.7,3.5))
a = fig.add_subplot(111)
a.set_title("My Plot Title")
a.set_xlabel("Frequency Hz")
a.set_ylabel("Normalized Energy")
#fig.tight_layout()



from sys import argv

# Plot Page
def animate(i):
        data = []
        success = 1

        try:
                data = np.genfromtxt(directory['app_data'] + 'DataPlotFile.txt',delimiter=' ')
        except:
                print('ERROR: DataPlotFile.txt data load unsuccessful')
                success = success * 0
        if data != []:

                number_cols = len(data[0])

                # Clear subplot for new data
                a.clear()

                mag_max = 0     # maximum magnitude of magnitude lists


        # Create legend from plot label values
        a.legend()
##        a.set_title("My Plot Title")
        a.set_xlabel("Frequency Hz")
        a.set_ylabel("Normalized Energy")

                 

        try:
                if number_cols > 1:
                        freq_List = data[:,0]
                        mag1_List = data[:,1]
                        plot1 = a.plot(freq_List, mag1_List,'r',label='Test')
                if number_cols > 2:
                        mag2_List = data[:,2]
                        plot2 = a.plot(freq_List, mag2_List,'g',label='Comparison')
                if number_cols > 3:
                        mag3_List = data[:,3]
                        plot3 = a.plot(freq_List, mag3_List,'b',label='Baseline')

                # Create legend from plot label values
                a.legend()
        except:
                print('ERROR: Data did not load successfully')
                success = success * 0
        if success == 0:
                print('-------------------')
                print('ERROR: Animate function has error(s)')


class Plot_Page(tk.Frame):
        def poll(self):
                # Update plot page with new content every '__' seconds
                def poll (self):
                        # Global directory navigation file
                        with open('directory.json','r') as g:
                                global directory
                                directory = json.load(g)
                                g.close

                        # Read plot preferences json file
                        with open(directory['app_data'] + 'plot_preferences.json','r') as f:
                                plot_preferences = json.load(f)
                                f.close

                        # Update Plot #1 dropdown with most recent test (for default option)
                        self.Plot1_Dropdown['values'] = plot_preferences["selected_test"]
                        self.Plot1_Dropdown.current(0)

                        try:
                                selft = urllib.request.urlopen("http://192.168.1.1/S", timeout=1).read()
                                connect = True
                        except (UnicodeDecodeError, urllib.error.URLError) or (OSError):
                                connect = False

                        # check for changes in data every 10 seconds
                        self.after(10000, self.poll)

        def showTests(self):
                with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close
                current_vehicle_directory = directory['veh_path'] + selected_vehicle["name"] + "_" + selected_vehicle['model'] + '_' + selected_vehicle['year_Veh'] + '/'
                try:

                        all_filenames = os.listdir(current_vehicle_directory)
                        vehicle_tests = []
                        for item in all_filenames:
                                if (("Baseline" not in item) and (".DS_Store" not in item)):

                                        formatted_item = item
                                        vehicle_tests.append(formatted_item)

                        self.Plot1_Dropdown['values'] = vehicle_tests
                        self.Plot2_Dropdown['values'] = vehicle_tests

                except:
                        os.makedirs(current_vehicle_directory)
                        vehicle_filenames = os.listdir(current_vehicle_directory)

        def showComparisonTests(self):

                # Global directory file
                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

                # Selected vehicle file
                with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close

                # Plot test preferences
                with open(directory['app_data'] + 'plot_preferences.json','r') as f:
                        plot_preferences = json.load(f)
                        f.close

                # Find what test is currently selected
                #selected_test = plot_preferences["selected_test"]
                selected_test = str(self.Plot1_Dropdown.get())

                # Save current vehicle directory
                selected_test_directory = directory['veh_path'] + selected_vehicle['name'] + '_' + selected_vehicle['model'] + '_' + selected_vehicle['year_Veh'] + '/' + selected_test + "/"

                match_file = ""
                for root, dirs, files in os.walk(selected_test_directory):
                        if 'match.json' in files:
                                match_file = os.path.join(root,'match.json')
                if (match_file != ""):
                        print("match.json file found")

                        # Load the json match file
                        with open(match_file,'r') as f:
                                match = json.load(f)
                                f.close

                        # Reorder the match variable by closest percent match
                        sorted_by_percent_match = sorted(match, key=match.get, reverse = True)

                        # Populate the dropdown with ordered match values
                        sorted_testnames = []
                        formatted_sorted_testnames = []
                        for key in sorted_by_percent_match:
                                sorted_testnames.append(key)
                        if(sorted_testnames != []):
                                for item in sorted_testnames:
                                        print(item)
                                        # remove file identifiers from dropdown contents
                                        formatted_item = item
                                        condition = ["trouble", "Idle", "10", "20", "30", "40", "50", "60", "70", "80","-1-","-2-","--"," ","  ",]
                                        for cond in condition:
                                                if (cond in formatted_item): formatted_item = formatted_item.replace(cond,"")
                                        if (formatted_item != "") and ("Baseline" not in formatted_item):
                                                formatted_sorted_testnames.append(formatted_item)
                                                # print("Formatted: " + formatted_item)

                                if(formatted_sorted_testnames != []):

                                        self.Plot2_Dropdown['values'] = formatted_sorted_testnames
                                        print('Percent match sort successful:')
                                        print(formatted_sorted_testnames)
                                else:
                                        print('ERROR: Percent match sort unsuccessful')
                else:
                        print("ERROR: No match.json file found")


        def updatePlot(self, controller):
                success = 1 # Becomes 0 if updatePlot unsuccesful for error message
                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

                # Read currently selected vehicle file
                with open(directory['app_data'] + 'selected_vehicle.json','r') as file:
                        selected_vehicle = json.load(file)
                        file.close

                veh_path = str(directory['veh_path'])
                home = str(directory['home'])

                # Get selected resolution
                resolution = str(self.PlotResolution_Dropdown.get())

                # Format resolution to intended text file name based on user-selected input
                if resolution == "250 Hz":
                        resolution = "fft 250Hz.txt"
                elif resolution == "125 Hz":
                        resolution = "fft 125Hz.txt"
                elif resolution == "62.5 Hz":
                        resolution = "fft 62.5Hz.txt"

                # Find selected directories
                data1_name = str(self.Plot1_Dropdown.get())
                data2_name = str(self.Plot2_Dropdown.get())
                print('Selected: ' + data2_name)

                # Find data1 and data2 files
                current_directory = directory['veh_path'] + selected_vehicle["name"] + '_' + selected_vehicle['model'] + '_' + selected_vehicle['year_Veh'] + "/"

                all_filenames = os.listdir(current_directory)
                vehicle_tests = []
                for item1 in all_filenames:
                        if data1_name in item1:
                                data1_name = item1
                                break
                for item2 in all_filenames:
                        if data2_name in item2:
                                data2_name = item2
                                break

                with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close

                # Find directories for vehicles to compare
                data1_directory = current_directory + data1_name + "/"
                data2_directory = current_directory + data2_name + "/"

                print(data1_directory)
                print(data2_directory)
                # Find file with specified resolution
                for root, dirs, files in os.walk(data1_directory):
                        if resolution in files:
                                data1_file = os.path.join(root,resolution)
                for root, dirs, files in os.walk(data2_directory):
                        if resolution in files:
                                data2_file = os.path.join(root,resolution)
                x1 = []
                y1 = []
                x2 = []
                y2 = []
                x_baseline = []
                y_baseline = []

                # Extract file contents
                try:
                        print(data1_file)
                        print(data2_file)
                        data1 = np.loadtxt(data1_file)
                        data2 = np.loadtxt(data2_file)

                        # Save 1 x and 2 y terms in DataPlotFile
                        x1 = data1[:,0]
                        y1 = data1[:,1]
                        x2 = data2[:,0]
                        y2 = data2[:,1]

                        print('Array data loaded')
                except:
                        print('ERROR: Array data load failed')
                        success = success * 0
                # If baseline is desired
                if self.showBaselineChecked.get():
                        # Directory of currently selected vehicle profile
                        vehicle_directory = directory['veh_path'] + selected_vehicle['name'] + '_' + selected_vehicle['model'] + '_' + selected_vehicle['year_Veh'] + '/'

                        # To hold baseline to compare
                        baseline_foldername = ""

                        # Set diagnostic type
                        diagnostic_foldername = data1_name

                        # Loop through all of the subdirectories
                        for root, dirs, files in os.walk(vehicle_directory):
                                for direct in dirs:
                                        # Extract the directories that say "Baseline"
                                        if "Baseline" in direct:
                                                # Find the directory in the list of Baselines that has a matching test type
                                                # Assign the baseline_foldername that matching directory
                                                if ("Idle" in diagnostic_foldername) and ("Idle" in direct): baseline_foldername = direct
                                                elif ("10" in diagnostic_foldername) and ("10" in direct): baseline_foldername = direct
                                                elif ("20" in diagnostic_foldername) and ("20" in direct): baseline_foldername = direct
                                                elif ("30" in diagnostic_foldername) and ("30" in direct): baseline_foldername = direct
                                                elif ("40" in diagnostic_foldername) and ("40" in direct): baseline_foldername = direct
                                                elif ("50" in diagnostic_foldername) and ("50" in direct): baseline_foldername = direct
                                                elif ("60" in diagnostic_foldername) and ("60" in direct): baseline_foldername = direct
                                                elif ("70" in diagnostic_foldername) and ("70" in direct): baseline_foldername = direct

                        # Check if baseline exists
                        if baseline_foldername != "":
                                print('Baseline Exists: ' + baseline_foldername)
                                # Create directory path
                                baseline_directory = vehicle_directory + baseline_foldername
                                baseline_filePathToPlot = ""
                                # Get correct resolution
                                for root, dirs, files in os.walk(baseline_directory):
                                        if resolution in files:
                                                baseline_filePathToPlot = os.path.join(root,resolution)
                                                print('Found baseline: ' + baseline_filePathToPlot)
                                try:
                                    data_baseline = np.loadtxt(baseline_filePathToPlot)
                                    x_baseline = data_baseline[:,0]
                                    y_baseline = data_baseline[:,1]
                                    np.savetxt((directory['app_data'] + 'DataPlotFile.txt'), np.column_stack((x1,y1,y2,y_baseline)),fmt='%.4g %.4g %.4g %.4g')
                                    print('Baseline + Data plot save successful')
                                except:
                                    print('ERROR: Baseline + Data plot save unsuccessful')
                                    success = success * 0
                        else:
                                print('ERROR: No corresponding baseline exists')
                                base_plot=messagebox.showwarning(title="No baseline saved", message = "There is no baseline saved for this test. Uncheck the baseline box to plot data.")
                                success = success * 0
                else:   # If baseline is not selected in checkbox
                        # Save data to plot file to be plotted
                        try:
                            np.savetxt(directory['app_data'] + 'DataPlotFile.txt', np.column_stack((x1,y1,y2)),fmt='%.4g %.4g %.4g')
                            print('DataPlotFile save successful')
                        except:
                            print('ERROR: DataPlotFile save not successful')
                            success = success * 0
                if (success == 0):
                        print('--------------------------')
                        print ('ERROR: Plot update failed.')
                else:
                        print('--------------------------')
                        print ('SUCCESS: Plot update succeeded')

        def updateFreq(self, controller):
                with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close



                with open(directory['app_data'] + 'save_test.json','r') as f2:
                        saved_test = json.load(f2)
                        f2.close

                with open(directory['app_data'] + 'save_test.json','w') as f2:
                        json.dump(saved_test,f2)
                        f2.close


                # def Key_Freqs_Update ():
                        
                speed_str = saved_test['speed']
                speed = float(speed_str)

                gear_str = saved_test['gear']
                gear_ratio = float(selected_vehicle[gear_str])

                tire_str = selected_vehicle['tire']
                tire = float(tire_str)

                reverse_Gear_str = selected_vehicle['reverse_Gear']
                if reverse_Gear_str == "":
                        reverse_Gear = 0
                else:
                        reverse_Gear = float(reverse_Gear_str)
                        
                finaldrive_str = selected_vehicle['final_Drive']
                if finaldrive_str == "":
                        finaldrive = 0
                else:
                        finaldrive = float(finaldrive_str)

                cylinder_str = selected_vehicle['num_Cylinders']
                if cylinder_str == "":
                        cylinder = 0
                else:
                        cylinder = int(cylinder_str)

                main_Pulley_str = selected_vehicle['main_Pulley']
                if main_Pulley_str == "":
                        main_Pulley = 0
                else:
                        main_Pulley = float(main_Pulley_str)
                        
                alternator_str = selected_vehicle['alternator']
                if alternator_str == "":
                        alternator = 0
                else:
                        alternator = float(alternator_str)

                air_Conditioner_str = selected_vehicle['air_Conditioner']
                if air_Conditioner_str == "":
                        air_Conditioner = 0
                else:
                        air_Conditioner = float(air_Conditioner_str)

                waterpump_str = selected_vehicle['waterpump']
                if waterpump_str == "":
                        waterpump = 0
                else:
                        waterpump = float(waterpump_str)

                fan_str = selected_vehicle['fan']
                if fan_str == "":
                        fan = 0
                else:
                        fan = float(fan_str)

                powersteer_str = selected_vehicle['powersteer']
                if powersteer_str == "":
                        powersteer = 0
                else:        
                        powersteer = float(powersteer_str)

                tension_str = selected_vehicle['tension']
                if tension_str == "":
                        tension = 0
                else:
                        tension = float(tension_str)

                extra_Accessory_str = selected_vehicle['extra_Accessory']
                if extra_Accessory_str == "":
                        extra_Accessory = 0
                else:
                        extra_Accessory = float(extra_Accessory_str)
                        

                tire_rpm = speed * 5280.0 * 12.0 / tire / 60.0
                tire_freq = tire_rpm / 60.0

                driveshaft_rpm = tire_rpm * finaldrive
                driveshaft_freq = tire_freq * finaldrive

                crank_rpm = driveshaft_rpm * gear_ratio
                crank_freq = driveshaft_freq * gear_ratio

                cylinder_freq = crank_freq * cylinder / 2
                cylinder_fire_per_minute = cylinder_freq * 60

                alt_freq = 0 if alternator==0 else crank_freq * (main_Pulley / alternator)
                AC_freq = 0 if air_Conditioner==0 else crank_freq * (main_Pulley / air_Conditioner)
                waterpump_freq = 0 if waterpump==0 else crank_freq * (main_Pulley / waterpump)
                fan_freq = 0 if fan==0 else crank_freq * (main_Pulley / fan)
                powersteer_freq = 0 if powersteer==0 else crank_freq * (main_Pulley / powersteer)
                tension_freq = 0 if tension==0 else crank_freq * (main_Pulley / tension)
                extra_Accessory_freq = 0 if extra_Accessory==0 else crank_freq * (main_Pulley / extra_Accessory)



                cylinder_freq_round = round(cylinder_freq, 2)
                crank_freq_round = round(crank_freq, 2)
                driveshaft_freq_round = round(driveshaft_freq,2)
                tire_freq_round = round(tire_freq, 2)
                finaldrive_round = round(finaldrive, 2)
                alt_freq_round = round(alt_freq,2)
                AC_freq_round = round(AC_freq, 2)
                waterpump_freq_round = round(waterpump_freq, 2)
                fan_freq_round = round(fan_freq, 2)
                powersteer_freq_round = round(powersteer_freq, 2)
                tension_freq_round = round(tension_freq, 2)
                extra_Accessory_freq_round = round(extra_Accessory_freq, 2)

                frame3 = LabelFrame(self, text="Diagnostics - Relevant Frequencies", width=785, height=100, bd=5, borderwidth=3, relief=GROOVE)
                frame3.place(relx=0,x = 5, rely=.76, anchor="nw")
                        
                name_Label = ttk.Label(frame3,text = 'Name: {}'.format(selected_vehicle['name']))
                name_Label.place(relx = 0, x = 5, rely = 0, y = 5, anchor=NW)
                make_Label = ttk.Label(frame3,text = 'Make:  {}'.format(selected_vehicle['make']))
                make_Label.place(relx = 0, x=5, rely = 0.30, anchor=NW)
                model_Label = ttk.Label(frame3,text = 'Model: {}'.format(selected_vehicle['model']))
                model_Label.place(relx = 0, x = 5, rely = 0.55, anchor=NW)
                year_Veh_Label = ttk.Label(frame3,text = 'Year:   {}'.format(selected_vehicle['year_Veh']))
                year_Veh_Label.place(relx = 0, x= 5, rely = 0.80, anchor=NW)

                speed_Label = ttk.Label(frame3,text =           ' Test Speed:  ' + str(speed) + " Mph")
                speed_Label.place(relx = 0.18, rely = 0, y = 5, anchor=NW)
                tire_Label = ttk.Label(frame3,text =            ' Tires:           ' + str(tire_freq_round) + " Hz")
                tire_Label.place(relx = 0.18, rely = 0.3, anchor=NW)
                driveshaft_Label = ttk.Label(frame3,text =      ' Driveshaft:   ' + str(driveshaft_freq_round) + " Hz")
                driveshaft_Label.place(relx = 0.18, rely = 0.55, anchor=NW)
                crankcase_Label = ttk.Label(frame3,text =       'Crankcase:   ' + str(crank_freq_round) + ' Hz')
                crankcase_Label.place(relx = .18, x = 5, rely = 0.80, anchor=NW)

                cyl_Fire_Label = ttk.Label(frame3,text =        'Spark Plug:        ' + str(cylinder_freq_round) + ' Hz')
                cyl_Fire_Label.place(relx = .38, x= 5, rely = 0, y = 5, anchor=NW)
                alt_Label = ttk.Label(frame3,text =             ' Alternator:          ' + str(alt_freq_round) + " Hz")
                alt_Label.place(relx = 0.38, rely = 0.3, anchor=NW)
                AC_Label = ttk.Label(frame3,text =              ' Air Conditioner:   ' + str(AC_freq_round) + " Hz")
                AC_Label.place(relx = 0.38, rely = 0.55, anchor=NW)
                waterpump_Label = ttk.Label(frame3,text =       'Water Pump:      ' + str(waterpump_freq_round) + ' Hz')
                waterpump_Label.place(relx = .38, x = 5, rely = 0.80, anchor=NW)

                fan_Label = ttk.Label(frame3,text =             'Cooling Fan:      ' + str(fan_freq_round) + ' Hz')
                fan_Label.place(relx = .61, x= 5, rely = 0, y = 5, anchor=NW)
                powersteer_Label = ttk.Label(frame3,text =      ' Power Steering: ' + str(powersteer_freq_round) + " Hz")
                powersteer_Label.place(relx = 0.61, rely = 0.3, anchor=NW)
                AC_Label = ttk.Label(frame3,text =              ' Tension Pulley:   ' + str(tension_freq_round) + " Hz")
                AC_Label.place(relx = 0.61, rely = .55, anchor=NW)
                extra_Accessory_Label = ttk.Label(frame3,text = 'Accessory:         ' + str(extra_Accessory_freq_round) + ' Hz')
                extra_Accessory_Label.place(relx = .61, x = 5, rely = 0.80, anchor=NW)
                
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

                veh_path = str(directory['veh_path'])

                # AVA app controller (app_data access)
                self.controller = controller

                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='Plot', width=45).pack(side=LEFT)
                self.pageLabelFrame.place(relx = 0, rely = 0.005, anchor = "nw")

                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(padx=5, pady = 30, side = "left", expand = "no", anchor = "n")


                frame2 = LabelFrame(self, text="Plot controls", width=250, height=40, bd=1, borderwidth=4, relief=GROOVE)
                frame2.place(relx=0 ,x = 5, rely=0.15, anchor=NW)



                frame1 = LabelFrame(self, text="Interactive Plotting", width=480, height=10, bd=1, borderwidth=4, relief=GROOVE)
                frame1.place(relx=1,x = -5, rely=0.07, anchor=NE)

                frame4 = LabelFrame(self, text="", width=250, height=5, bd=1, borderwidth=4, relief=GROOVE)
                frame4.place(relx=0 ,x = 5, rely=0.65, anchor=NW)
                
                canvas = FigureCanvasTkAgg(fig, frame1)
                canvas.show()
                canvas.get_tk_widget().place(anchor = "nw")

                toolbar = NavigationToolbar2TkAgg(canvas, self)
                toolbar.update()
                toolbar.place(relx=0.50, rely=0.005, anchor = "nw")

                canvas._tkcanvas.pack(side=BOTTOM)

                # Read currently selected vehicle file
                with open(directory['app_data'] + 'selected_vehicle.json','r') as file:
                        selected_vehicle = json.load(file)
                        file.close

                # Load plots from test results directory
                from os import listdir
                current_vehicle_directory = directory['veh_path'] + selected_vehicle["name"] + "_" + selected_vehicle['model'] + '_' + selected_vehicle['year_Veh'] + '/'

                try:
                        all_filenames = os.listdir(current_vehicle_directory)
                        vehicles = []
                        for item in all_filenames:
                                if (("Baseline" not in item) and (".DS_Store" not in item)):
                                        vehicles.append(item)
                                        print(item)
                        vehicle_filenames = vehicles
                except:
                        os.makedirs(current_vehicle_directory)
                        vehicle_filenames = os.listdir(current_vehicle_directory)

                self.Plot1_Dropdown_Frame = ttk.Labelframe(frame2, text='Test')
                self.Plot1_Dropdown = ttk.Combobox(self.Plot1_Dropdown_Frame, values = vehicle_filenames, postcommand = self.showTests, state='readonly')
                self.Plot1_Dropdown.pack(pady=5,padx=5)
                self.Plot1_Dropdown_Frame.pack(side="top",pady=3,padx=5)

                self.Plot2_Dropdown_Frame = ttk.Labelframe(frame2, text='Comparison')
                self.Plot2_Dropdown = ttk.Combobox(self.Plot2_Dropdown_Frame, values = vehicle_filenames, postcommand = self.showComparisonTests, state='readonly')

                self.Plot2_Dropdown.pack(pady=5,padx=10)
                self.Plot2_Dropdown_Frame.pack(side="top",pady=3,padx=5)

                self.PlotResolution_Dropdown_Frame = ttk.Labelframe(frame2, text='Resolution')
                self.PlotResolution_Dropdown = ttk.Combobox(self.PlotResolution_Dropdown_Frame, values = ["250 Hz", "125 Hz", "62.5 Hz"], state='readonly')
                self.PlotResolution_Dropdown.pack(pady=(5,10),padx=5)
                self.PlotResolution_Dropdown_Frame.pack(side="top",pady=3,padx=5)

                self.showBaselineChecked = IntVar()
                self.ShowBaseline_Checkbox = ttk.Checkbutton(frame2, text = "Baseline",variable = self.showBaselineChecked)
                self.ShowBaseline_Checkbox.pack(side="left", padx = 10)

                self.plot_button = ttk.Button(frame2, text = "Plot!",command = lambda: self.updatePlot(controller))
                self.plot_button.pack(side = "right", padx = 10, pady = 3, expand = "no", anchor = "n")

                self.update_key_frequencies_button = ttk.Button(frame4, text="Update_Relevant_Frequencies",
                                    command=lambda: self.updateFreq(controller))
                self.update_key_frequencies_button.pack(padx=10, pady = 3, side = "left", expand = "no", anchor = "n") 



##
##                Key_Freqs_Update()
##
##
##                Update_button = ttk.Button(self, text="Refresh Page",
##                                    command = Key_Freqs_Update)
##                Update_button.pack(padx=20, pady = (305,10), side = "left", expand = "no", anchor = "n")
##
##                        
                self.poll()
