import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os

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

        # App Data global variable holder
        self.app_data = {"var1":    tk.StringVar(),
                         "var2":    tk.StringVar(),
                         "var3":    tk.StringVar()
                         }
        
        # Container holding app pages
        container = tk.Frame(self)
        container.pack(side="top",expand=False)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        # Initial empty set of page frames
        self.frames = {}

        # Application pages to load in background
        from Home_Page import Home_Page
        from Configure_Test_Page import Configure_Test_Page
        from New_Vehicle_Page import New_Vehicle_Page
        from Test_Is_Running_Page import Test_Is_Running_Page
        from Save_Test_Page import Save_Test_Page
        from Results_Page import Results_Page
        from Plot_Page import Plot_Page

        # Create frames for each of the app pages
        for F in (Home_Page, Configure_Test_Page, Plot_Page, New_Vehicle_Page, Test_Is_Running_Page, Save_Test_Page, Results_Page):
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
#fullscreen = FullScreenApp(app)
import Plot_Page
import matplotlib.animation as animation
animate = Plot_Page.animation.FuncAnimation(Plot_Page.f,Plot_Page.animate,interval=1000)
app.mainloop()
