import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File system access library
import glob, os
import json


class New_Vehicle_Page(tk.Frame):
        def saveNewVehicleProfile (self,controller):
                name = str(self.entry1.get())
                make = str(self.entry2.get())
                model = str(self.entry3.get())
                year = str(self.entry4.get())

                data = {
                        'name' : name,
                        'make' : make,
                        'model' : model,
                        'year' : year,
                        }

                with open('data1.json','w') as f:
                        json.dump(data,f)
                        f.close
                
                controller.show_page('Home_Page')
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                # AVA app controller (app_data access)
                self.controller = controller
                
                self.label = ttk.Label(self, text="New Vehicle Page")
                self.label.pack(pady=1,padx=1, side = "top", anchor = "n")
                
                self.goToHomePage_button = ttk.Button(self, text="Go Back",
                        command=lambda: self.saveNewVehicleProfile(controller))
                self.goToHomePage_button.pack(side = "left", expand = "no", anchor = "n")



                D = ('0 Seconds', '30 seconds', '60 seconds', '90 seconds', '120 seconds')
                DT1 = ttk.Labelframe(self, text='Pre-defined - some will need this (cylinders) while other will need enterable fields')
                DT = ttk.Combobox(DT1, values=D, state='readonly')
                DT.current(0)  # set selection
                DT.pack(pady=5, padx=10)
                DT1.pack(in_=self, side="top", pady=20, padx=10)

                self.label1 = ttk.Label(self,text = 'Name: ')
                self.label1.pack(side= "right")
                self.entry1 = ttk.Entry(self)
                self.entry1.pack(side = "right")

                self.label2 = ttk.Label(self,text = 'Make: ')
                self.label2.pack(side= "top")
                self.entry2 = ttk.Entry(self)
                self.entry2.pack(side = "top")

                self.label3 = ttk.Label(self,text = 'Model: ')
                self.label3.pack(side= "top")
                self.entry3 = ttk.Entry(self)
                self.entry3.pack(side = "top")

                self.label4 = ttk.Label(self,text = 'Year: ')
                self.label4.pack(side= "top")
                self.entry4 = ttk.Entry(self)
                self.entry4.pack(side = "top")



                
