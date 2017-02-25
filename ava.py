import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

# Math functions library
import numpy as np

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='792x477+0+0'
        master.geometry("{0}x{1}+0+0".format(
        master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
       
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

# Startup routine
class AVA(tk.Tk):    
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        # Container holding app pages
        container = tk.Frame(self)
        container.pack(side="top",expand=False)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        # Initial empty set of page frames
        self.frames = {}

        # Application pages to load in background
        from HomePage import HomePage
        from ConfigureTestPage import ConfigureTestPage
        from PlotPage import PlotPage
        from NewVehiclePage import NewVehiclePage
        from TestIsRunningPage import TestIsRunningPage
        from SaveTestPage import SaveTestPage
        from ResultsPage import ResultsPage

        # Create frames for each of the app pages
        for F in (HomePage, ConfigureTestPage, PlotPage, NewVehiclePage, TestIsRunningPage, SaveTestPage, ResultsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew") 

        # First page to load is HomePage
        self.show_page("HomePage")
        
    # Define how frames will be promoted to current Tkinter frame
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
    # Search through possible pages to find
    # desired page to promote to current Tkinter frame
    def show_page(self,page_name):
        '''Show a frame for the given page name'''
        for F in self.frames:
            if F == page_name:
                self.show_frame(F)
                return

# -------------------------------------------------------------#
# --------------------- Run the app ---------------------------#
# -------------------------------------------------------------#
app = AVA()
app.title("Automotive Vibration Analyzer")
fullscreen = FullScreenApp(app)
app.mainloop()
