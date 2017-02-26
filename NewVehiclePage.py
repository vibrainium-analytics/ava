import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class NewVehiclePage(tk.Frame):
        def entry(self,controller):
                veh = self.name.get()
                cylinders = self.cylnd.get()
                tiresize = self.tire.get()
                advanced = self.advnc.get()
                print ("name " + str(veh))
                print ("cylinders " + str(cylinders))
                print ("tire " + str(tiresize))
                print ("extra " + str(advanced))
                if advanced == 'Y' or advanced == 'y':
                        #open sub window for advanced 
                        controller.show_page("NewVehiclePage_Advanced")
                elif advanced == 'N' or advanced == 'n':
                        controller.show_page("HomePage")
   
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                self.controller = controller
                
                self.label = ttk.Label(self, text="New Vehicle Page")
                self.label.pack(pady=5, side = "top", anchor = "n")

                self.label = ttk.Label(self, text="Enter your vehicle name\n (ex: Steve-Toyota)")
                self.label.pack(pady=5)

                self.name = ttk.Entry(self)
                self.name.pack(padx=5)

                self.label = ttk.Label(self, text="Enter number of cylinders")
                self.label.pack(pady=5)

                self.cylnd = ttk.Entry(self)
                self.cylnd.pack(padx=5)

                label = ttk.Label(self, text="Enter tire diameter in inches\n (Leave blank if unknown)").pack()

                self.tire = ttk.Entry(self)
                self.tire.pack(padx=5) 

                label = ttk.Label(self, text=(
                    ("Do you want to enter additional vehicle data?\n"
                     "(Gear Ratios, Pully Ratios, etc) Y or N")
                    )).pack()

                self.advnc = ttk.Entry(self)
                self.advnc.pack(padx=5)
                
                b = ttk.Button(self, text="Enter", command=lambda:self.entry(controller))
                b.pack(pady=5)
                
               
class NewVehiclePage_Advanced(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                self.controller = controller
                # Advanced controls go here

                self.label = ttk.Label(self, text="New Vehicle Advanced Page")
                self.label.pack(pady=5, side = "top", anchor = "n")

                b1 = ttk.Button(self, text="I'm scared.  Get me out of here", command=lambda:controller.show_page("NewVehiclePage_Advanced"))
                b1.pack(pady=5)

                b2 = ttk.Button(self, text="Advanced is my thing", command=lambda:controller.show_page("HomePage") or print("Advanced window"))
                b2.pack(pady=5)
