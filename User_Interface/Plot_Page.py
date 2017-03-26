import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
# File system access library
import glob, os

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

f = Figure(figsize=(5.65,2.6))
a = f.add_subplot(111)

from sys import argv
import json

# Plot Page
def animate(i):

        data = np.genfromtxt(directory['app_data'] + 'DataPlotFile.txt',delimiter=' ')
        number_cols = len(data[0])

        # Clear subplot for new data
        a.clear()

        mag_max = 0     # maximum magnitude of magnitude lists

        if number_cols > 1:
                freq_List = data[:,0]
                mag1_List = data[:,1]
                plot1 = a.plot(freq_List, mag1_List,'r',label='Plot #1')
        if number_cols > 2:
                mag2_List = data[:,2]
                plot2 = a.plot(freq_List, mag2_List,'g',label='Plot #2')
        if number_cols > 3:
                mag3_List = data[:,3]
                plot3 = a.plot(freq_List, mag3_List,'b',label='Plot #3')

        # Create legend from plot label values
        a.legend()

class Plot_Page(tk.Frame):
        def refresh(self):
                with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close
                current_vehicle_directory = directory['veh_path'] + selected_vehicle["name"] + "_" + selected_vehicle['model'] + '_' + selected_vehicle['year'] + '/'
                try:

                        all_filenames = os.listdir(current_vehicle_directory)
                        vehicles = []
                        for item in all_filenames:
                                if (("Baseline" not in item) and (".DS_Store" not in item)):
                                        vehicles.append(item)
                        self.Plot1_Dropdown['values'] = vehicles
                        self.Plot2_Dropdown['values'] = vehicles
                except:
                        os.makedirs(current_vehicle_directory)
                        vehicle_filenames = os.listdir(current_vehicle_directory)

        def updatePlot(self, controller):
                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

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

                # Tack on parent directory from current vehicle json file
                with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close

                # Find directories for vehicles to compare
                data1_directory = directory['veh_path'] + selected_vehicle["name"] + '_' + selected_vehicle['model'] + '_' + selected_vehicle['year'] + "/" + data1_name + "/"
                data2_directory = directory['veh_path'] + selected_vehicle["name"] + '_' + selected_vehicle['model'] + '_' + selected_vehicle['year'] + "/" + data2_name + "/"

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

                # If baseline is desired
                if self.showBaselineChecked.get():
                        # Directory of currently selected vehicle profile
                        vehicle_directory = directory['veh_path'] + selected_vehicle["name"] + '_' + selected_vehicle['model'] + '_' + selected_vehicle['year'] + "/"

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
                        else:
                                print('ERROR: No corresponding baseline exists')
                else:   # If baseline is not selected in checkbox
                        # Save data to plot file to be plotted
                        try:
                            np.savetxt(directory['app_data'] + 'DataPlotFile.txt', np.column_stack((x1,y1,y2)),fmt='%.4g %.4g %.4g')
                            print('DataPlotFile save successful')
                        except:
                            print('ERROR: DataPlotFile save not successful')

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
                Label(self.pageLabelFrame, text='Plot', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,5), ipadx = 2, ipady = 2, fill = "x")

                goToHomePage_button = ttk.Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=5, side = "left", expand = "no", anchor = "n")

                frame1 = LabelFrame(self, text="Interactive Plotting", width=500, height=300, bd=1, borderwidth=4, relief=GROOVE)
                frame1.place(relx=1,x = -5, rely=0.1, anchor=NE)

                frame2 = LabelFrame(self, text="Plot controls", width=250, height=300, bd=1, borderwidth=4, relief=GROOVE)
                frame2.place(relx=0 ,x = 5, rely=0.2, anchor=NW)

                frame3 = LabelFrame(self, text="Diagnostics - Relevant Frequencies", width=700, height=100, bd=5, borderwidth=3, relief=GROOVE)
                frame3.place(relx=0,x = 5, rely=1, anchor=SW)

                canvas = FigureCanvasTkAgg(f, frame1)
                canvas.show()
                canvas.get_tk_widget().pack(side="right", fill=BOTH, expand=True)

                toolbar = NavigationToolbar2TkAgg(canvas, frame1)
                toolbar.update()

                canvas._tkcanvas.pack(side=BOTTOM)##, fill=BOTH, expand=True)

                # Read currently selected vehicle file
                with open(directory['app_data'] + 'selected_vehicle.json','r') as file:
                        selected_vehicle = json.load(file)
                        file.close

                # Load plots from test results directory
                from os import listdir
                current_vehicle_directory = directory['veh_path'] + selected_vehicle["name"] + "_" + selected_vehicle['model'] + '_' + selected_vehicle['year'] + '/'

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

                self.Plot1_Dropdown_Frame = ttk.Labelframe(frame2, text='Plot 1')
                self.Plot1_Dropdown = ttk.Combobox(self.Plot1_Dropdown_Frame, values = vehicle_filenames, postcommand = self.refresh, state='readonly')
                self.Plot1_Dropdown.pack(pady=5,padx=5)
                self.Plot1_Dropdown_Frame.pack(side="top",pady=5,padx=5)

                self.Plot2_Dropdown_Frame = ttk.Labelframe(frame2, text='Plot 2')
                self.Plot2_Dropdown = ttk.Combobox(self.Plot2_Dropdown_Frame, values = vehicle_filenames, postcommand = self.refresh, state='readonly')
                self.Plot2_Dropdown.pack(pady=5,padx=10)
                self.Plot2_Dropdown_Frame.pack(side="top",pady=5,padx=5)

                self.PlotResolution_Dropdown_Frame = ttk.Labelframe(frame2, text='Plot Resolution')
                self.PlotResolution_Dropdown = ttk.Combobox(self.PlotResolution_Dropdown_Frame, values = ["250 Hz", "125 Hz", "62.5 Hz"], state='readonly')
                self.PlotResolution_Dropdown.pack(pady=5,padx=5)
                self.PlotResolution_Dropdown_Frame.pack(side="top",pady=5,padx=5)
                
                self.showBaselineChecked = IntVar()
                self.ShowBaseline_Checkbox = ttk.Checkbutton(frame2, text = "Show Baseline",variable = self.showBaselineChecked)
                self.ShowBaseline_Checkbox.pack(side="top")

                self.plot_button = ttk.Button(frame2, text = "Plot!",command = lambda: self.updatePlot(controller))
                self.plot_button.pack(side = "top", padx = 5, pady = 5, expand = "no", anchor = "n")
