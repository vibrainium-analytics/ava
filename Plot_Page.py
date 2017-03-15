import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

# Math functions library
import numpy as np

# Import plotting libraries
import matplotlib.pyplot as pl
import matplotlib, sys
import matplotlib.animation as animation
from matplotlib import style

# Plotting library canvas tool
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
matplotlib.use('TkAgg')

f = Figure(figsize=(5,5))
a = f.add_subplot(111)

from sys import argv
import json

# Plot Page
def animate(i):
        
        data = np.genfromtxt('DataPlotFile.txt',delimiter=' ')
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

        def updatePlot(self, controller):
                # Get selected resolution
                resolution = str(self.PlotResolution_Dropdown.get())

                # Format resolution to intended text file name based on user-selected input
                if resolution == "250 Hz":
                        resolution = "250.txt"
                elif resolution == "125 Hz":
                        resolution = "125.txt"
                elif resolution == "62.5 Hz":
                        resolution = "62.5.txt"
                        
                # Find selected directories
                data1_name = str(self.Plot1_Dropdown.get())
                data2_name = str(self.Plot2_Dropdown.get())

                # Tack on parent directory from current vehicle json file
                with open('/home/pi/ava/selected_vehicle.json','r') as f:
                        selected_vehicle = json.load(f)
                        f.close

                # Find directories for vehicles to compare
                data1_directory = "/home/pi/ava/vehicle_profiles/" + selected_vehicle["name"] + "/" + data1_name + "/"
                data2_directory = "/home/pi/ava/vehicle_profiles/" + selected_vehicle["name"] + "/" + data1_name + "/"
                
                # Find file with specified resolution
                for root, dirs, files in os.walk(data1_directory):
                        if resolution in files:
                                data1_file = os.path.join(root,resolution)
                for root, dirs, files in os.walk(data2_directory):
                        if resolution in files:
                                data2_file = os.path.join(root,resolution)
                
                # Extract file contents
                data1 = np.loadtxt(data1_file)
                data2 = np.loadtxt(data2_file)

                # Save 1 x and 2 y terms in DataPlotFile
                x1 = data1[:,0]
                y1 = data1[:,1]

                x2 = data2[:,0]
                y2 = data2[:,1]

                os.chdir("/home/pi/ava")
                np.savetxt('DataPlotFile.txt', np.column_stack((x1,y1,y2)),fmt='%i %i %i')

                # Debug
                print("Resolution: " + resolution)
                print("Data 1: " + data1_directory)
                print("Data 2: " + data2_directory)
                print(data1_file)
                print(data2_file)
                print(data1)
                print(data2)
                print(x1)
                print(y1)
                
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                # AVA app controller (app_data access)
                self.controller = controller
                
                label = ttk.Label(self, text="Plot Page")
                label.pack(pady=1,padx=1, side = "top", anchor = "n")

                goToHomePage_button = ttk.Button(self, text="Home",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=15, side = "left", expand = "no", anchor = "n")

                canvas = FigureCanvasTkAgg(f, self)
                canvas.show()
                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                toolbar = NavigationToolbar2TkAgg(canvas, self)
                toolbar.update()
                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                # Load plots from test results directory
                from os import listdir
                vehicle_filenames = os.listdir("/home/pi/ava/vehicle_profiles/Spencer's Car/")
                
                self.Plot1_Dropdown_Frame = ttk.Labelframe(self, text='Plot 1')
                self.Plot1_Dropdown = ttk.Combobox(self.Plot1_Dropdown_Frame, values = vehicle_filenames, state='readonly')
                #self.Plot1_Dropdown.bind('<<ComboboxSelected>>',self.loadSavedVehicleProfile)
                self.Plot1_Dropdown.pack(pady=5,padx=10)
                self.Plot1_Dropdown_Frame.pack(in_=self,side="top",pady=20,padx=10)

                self.Plot2_Dropdown_Frame = ttk.Labelframe(self, text='Plot 2')
                self.Plot2_Dropdown = ttk.Combobox(self.Plot2_Dropdown_Frame, values = vehicle_filenames, state='readonly')
                #self.Plot1_Dropdown.bind('<<ComboboxSelected>>',self.loadSavedVehicleProfile)
                self.Plot2_Dropdown.pack(pady=5,padx=10)
                self.Plot2_Dropdown_Frame.pack(in_=self,side="top",pady=20,padx=10)

                self.PlotResolution_Dropdown_Frame = ttk.Labelframe(self, text='Plot Resolution')
                self.PlotResolution_Dropdown = ttk.Combobox(self.PlotResolution_Dropdown_Frame, values = ["250 Hz", "125 Hz", "62.5 Hz"], state='readonly')
                #self.Plot1_Dropdown.bind('<<ComboboxSelected>>',self.loadSavedVehicleProfile)
                self.PlotResolution_Dropdown.pack(pady=5,padx=10)
                self.PlotResolution_Dropdown_Frame.pack(in_=self,side="top",pady=20,padx=10)

                self.plot_button = ttk.Button(self, text = "Plot!",command = lambda: self.updatePlot(controller))
                self.plot_button.pack(side = "left", expand = "no", anchor = "n")
