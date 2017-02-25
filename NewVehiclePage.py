import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class NewVehiclePage(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                def entry():
                        veh = self.name.get()
                        cylinders = self.cylnd.get()
                        tiresize = self.tire.get()
                        advanced = self.advnc.get()
                        print ("name " + str(veh))
                        print ("cylinders " + str(cylinders))
                        print ("tire " + str(tiresize))
                        print ("extra " + str(advanced))
                        if advanced == 'N' or advanced == 'n':
                                controller.show_page("HomePage")
                        ##elif advanced == 'Y' or advanced == 'y':
                                #open sub window for advanced 
                                

                                
                label = ttk.Label(self, text="New Vehicle Page")
                label.pack(pady=5, side = "top", anchor = "n")

                label = ttk.Label(self, text="Enter your vehicle name\n (ex: Steve-Toyota)")
                label.pack(pady=5)

                self.name = ttk.Entry(self)
                self.name.pack(padx=5)

                label = ttk.Label(self, text="Enter number of cylinders")
                label.pack(pady=5)

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
                
                b = ttk.Button(self, text="Enter", command=entry)
                b.pack(pady=5)

 