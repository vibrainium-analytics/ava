import tkinter as tk
from tkinter import messagebox, ttk, Frame
import glob, os

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        padx = 4
        pady = 32
        self._geom='792x477+0+0'
        master.geometry("{0}x{1}+0+0".format(
        master.winfo_screenwidth()-padx, master.winfo_screenheight()-pady))
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
        container.pack(side = "top", fill = "both")


        # Initial empty set of page frames
        self.frames = {}

        # Application pages to load in background
        # *** Add new to end of the imports below
        from User_Interface.Home_Page import Home_Page
        from User_Interface.Configure_Test_Page import Configure_Test_Page
        from User_Interface.Plot_Page import Plot_Page
        from User_Interface.New_Vehicle_Page import New_Vehicle_Page
        from User_Interface.Test_Is_Running_Page import Test_Is_Running_Page
        from User_Interface.Save_Test_Page import Save_Test_Page
        from User_Interface.Results_Page import Results_Page
        from User_Interface.Tutorial_Main_Page import Tutorial_Main_Page
        from User_Interface.About_Page import About_Page
        from User_Interface.Tutorial_Plotting_Page import Tutorial_Plotting_Page
        from User_Interface.Tutorial_Sample_Collection_Page import Tutorial_Sample_Collection_Page
        from User_Interface.Tutorial_Vehicle_Creation_Page import Tutorial_Vehicle_Creation_Page


        # Create frames for each of the app pages
        # This was reordered so that you can add to the bottom of the list about
        #    and the beginning of the list below - easier to keep track of
        # *** Add new to beginning of list
        for F in (Tutorial_Vehicle_Creation_Page,
                  Tutorial_Sample_Collection_Page,
                  Tutorial_Plotting_Page,
                  About_Page,
                  Tutorial_Main_Page,
                  Results_Page,
                  Save_Test_Page,
                  Test_Is_Running_Page,
                  New_Vehicle_Page,
                  Plot_Page,
                  Configure_Test_Page,
                  Home_Page
                 ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew") 

        # First page to load is Home_Page
        self.show_page("Home_Page")
        
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
import User_Interface.Plot_Page
import matplotlib.animation as animation
animate = User_Interface.Plot_Page.animation.FuncAnimation(User_Interface.Plot_Page.fig,User_Interface.Plot_Page.animate,interval=3000)
app.mainloop()
