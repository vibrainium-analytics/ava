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

from tkinter import *

LARGE_FONT= ("Verdana", 12)

class DiagnosticsPage(tk.Frame):
    ## Page Controller
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Diagnostics", font=LARGE_FONT)
        label.pack(pady=1,padx=2, side = TOP, anchor = N)



        
        buttonHome = ttk.Button(self, text="Home",
                            command=lambda: controller.show_page("StartPage"))
        buttonHome.pack(pady=1, padx = 15, side= LEFT, expand = NO, anchor = N, fill = NONE)
        
        
        self.crankPrint = Button(self)
        self.crankPrint["text"]="Crankcase Frequency"
        self.crankPrint["background"] = "steel blue"
        self.crankPrint.pack(pady=1,padx=25, side = LEFT, expand = NO, anchor = NE, fill = NONE)
        self.crankPrint.bind("<Button-1>", self.crankPrintClick)

        self.driveshaft = Button(self)
        self.driveshaft["text"]="Driveshaft Frequency"
        self.driveshaft["background"] = "steel blue"
        self.driveshaft.pack(pady=1,padx=25, side = LEFT, expand = NO, anchor = NE, fill = NONE)
        self.driveshaft.bind("<Button-1>", self.driveshaftClick)

        self.wheelFreq = Button(self)
        self.wheelFreq["text"]="Wheel Frequency"
        self.wheelFreq["background"] = "steel blue"
        self.wheelFreq.pack(pady=1,padx=25, side = LEFT, expand = NO, anchor = NE, fill = NONE)
        self.wheelFreq.bind("<Button-1>", self.wheelFreqClick)

    ## crankPrint (Diagnostics) Click Event
    def crankPrintClick(self, event):
        
                #ratios - intitializing, they will be set by user input or calculated based on user input

        pi = 3.14159                                                    ## should probably be constant


        num_cylinders = 0
        first_gear_ratio = 0.0
        second_gear_ratio = 0.0
        third_gear_ratio = 0.0
        fourth_gear_ratio = 0.0
        fifth_gear_ratio = 0.0
        sixth_gear_ratio = 0.0
        reverse_ratio = 0.0
        converter_ratio = 0.0
        final_drive_ratio = 0.0
        wheel_circ_inches = 0.0
        wheel_dist_per_cycle = 0.0
        fourwheel = False

        ground_speed = 0.0                                           ## MPH
        gear = third_gear_ratio

        wheel_rpm = 0.0
        wheel_freq = 0.0
        driveshaft_rpm = 0.0
        driveshaft_freq = 0.0
        crank_rpm = 0.0
        crank_freq = 0.0
        cylinder_fire_freq = 0.0
        

        # My pickup data -- this will be entered by user and store into a vehicle profile

        num_cylinders = 8
        first_gear_ratio = 2.71
        second_gear_ratio = 1.54
        third_gear_ratio = 1
        fourth_gear_ratio = 0.71
        fifth_gear_ratio = 0.0  ##four speed transmission
        sixth_gear_ratio = 0.0  ##four speed transmission
        reverse_ratio = 2.18
        converter_ratio = 2.20
        final_drive_ratio = 3.55
        wheel_circ_inches = 98.33
        fourwheel = True

        test_ground_speed = 45.0                                             ## MPH -- pre/post determined test speed (post is probably better)
        gear = third_gear_ratio                                                        

        wheel_rpm = test_ground_speed * 5280.0 * 12.0 / wheel_circ_inches / 60.0
        wheel_freq = wheel_rpm / 60.0
        driveshaft_rpm = wheel_rpm * final_drive_ratio
        driveshaft_freq = wheel_freq * final_drive_ratio
        crank_rpm = driveshaft_rpm * gear
        crank_freq = driveshaft_freq * gear
        cylinder_fire_freq = crank_freq / 8.0

        messagebox.showinfo("Crankcase Info", "Please see the Python Shell for print statements\n\nThis information will all displayed within the plot page also once we get the window plot-kill situation under control")

        print("During the test the crankcase frequency was", crank_freq, "Hertz.")
        print("That translates to", crank_rpm, "revolutions per minute (RPM)\n")
        print("Cylinder fire frequency ", cylinder_fire_freq, "Hertz")
        

    ## driveshaft (Diagnostics) Click Event
    def driveshaftClick(self, event):
               
        #ratios - intitializing, they will be set by user input or calculated based on user input

        pi = 3.14159                                                    ## should probably be constant


        num_cylinders = 0
        first_gear_ratio = 0.0
        second_gear_ratio = 0.0
        third_gear_ratio = 0.0
        fourth_gear_ratio = 0.0
        fifth_gear_ratio = 0.0
        sixth_gear_ratio = 0.0
        reverse_ratio = 0.0
        converter_ratio = 0.0
        final_drive_ratio = 0.0
        wheel_circ_inches = 0.0
        wheel_dist_per_cycle = 0.0
        fourwheel = False

        ground_speed = 0.0                                           ## MPH
        gear = third_gear_ratio

        wheel_rpm = 0.0
        wheel_freq = 0.0
        driveshaft_rpm = 0.0
        driveshaft_freq = 0.0
        crank_rpm = 0.0
        crank_freq = 0.0
        cylinder_fire_freq = 0.0
        

        # My pickup data -- this will be entered by user and store into a vehicle profile

        num_cylinders = 8
        first_gear_ratio = 2.71
        second_gear_ratio = 1.54
        third_gear_ratio = 1
        fourth_gear_ratio = 0.71
        fifth_gear_ratio = 0.0  ##four speed transmission
        sixth_gear_ratio = 0.0  ##four speed transmission
        reverse_ratio = 2.18
        converter_ratio = 2.20
        final_drive_ratio = 3.55
        wheel_circ_inches = 98.33
        fourwheel = True

        test_ground_speed = 45.0                                             ## MPH -- pre/post determined test speed (post is probably better)
        gear = third_gear_ratio                                                        

        
        wheel_rpm = test_ground_speed * 5280.0 * 12.0 / wheel_circ_inches / 60.0
        wheel_freq = wheel_rpm / 60.0
        driveshaft_rpm = wheel_rpm * final_drive_ratio
        driveshaft_freq = wheel_freq * final_drive_ratio
        crank_rpm = driveshaft_rpm * gear
        crank_freq = driveshaft_freq * gear
        cylinder_fire_freq = crank_freq / 8.0

        print("During this the the  driveshaft frequency was" , driveshaft_freq, "Hertz.")
        print("That translates to ", driveshaft_rpm, "revolutions per minute (RPM)\n")


 ## crankPrint (Diagnostics) Click Event
    def wheelFreqClick(self, event):
        
                #ratios - intitializing, they will be set by user input or calculated based on user input

        pi = 3.14159                                                    ## should probably be constant


        num_cylinders = 0
        first_gear_ratio = 0.0
        second_gear_ratio = 0.0
        third_gear_ratio = 0.0
        fourth_gear_ratio = 0.0
        fifth_gear_ratio = 0.0
        sixth_gear_ratio = 0.0
        reverse_ratio = 0.0
        converter_ratio = 0.0
        final_drive_ratio = 0.0
        wheel_circ_inches = 0.0
        wheel_dist_per_cycle = 0.0
        fourwheel = False

        ground_speed = 0.0                                           ## MPH
        gear = third_gear_ratio

        wheel_rpm = 0.0
        wheel_freq = 0.0
        driveshaft_rpm = 0.0
        driveshaft_freq = 0.0
        crank_rpm = 0.0
        crank_freq = 0.0
        cylinder_fire_freq = 0.0
        

        # My pickup data -- this will be entered by user and store into a vehicle profile

        num_cylinders = 8
        first_gear_ratio = 2.71
        second_gear_ratio = 1.54
        third_gear_ratio = 1
        fourth_gear_ratio = 0.71
        fifth_gear_ratio = 0.0  ##four speed transmission
        sixth_gear_ratio = 0.0  ##four speed transmission
        reverse_ratio = 2.18
        converter_ratio = 2.20
        final_drive_ratio = 3.55
        wheel_circ_inches = 98.33
        fourwheel = True

        test_ground_speed = 45.0                                             ## MPH -- pre/post determined test speed (post is probably better)
        gear = third_gear_ratio                                                        

        wheel_rpm = test_ground_speed * 5280.0 * 12.0 / wheel_circ_inches / 60.0
        wheel_freq = wheel_rpm / 60.0
        driveshaft_rpm = wheel_rpm * final_drive_ratio
        driveshaft_freq = wheel_freq * final_drive_ratio
        crank_rpm = driveshaft_rpm * gear
        crank_freq = driveshaft_freq * gear
        cylinder_fire_freq = crank_freq / 8.0

        print("During the test the wheel frequency was", wheel_freq, "Hertz.")
        print("That translates to ", wheel_rpm, "revolutions per minute (RPM)\n")
        





