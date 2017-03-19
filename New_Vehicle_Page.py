
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

class New_Vehicle_Page(tk.Frame):
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

                Name = ""
##                Make = ""
##                Model = ""
##                Year = ""
##                
##                
##                num_cylinders = 0
##                first_gear_ratio = 0.0
##                second_gear_ratio = 0.0
##                third_gear_ratio = 0.0
##                fourth_gear_ratio = 0.0
##                fifth_gear_ratio = 0.0
##                sixth_gear_ratio = 0.0
##                reverse_ratio = 0.0
##                converter_ratio = 0.0
##                final_drive_ratio = 0.0
##                wheel_circ_inches = 0.0
##                wheel_dist_per_cycle = 0.0

                tk.Frame.__init__(self, parent)

                self.controller = controller

<<<<<<< HEAD
                
                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='New/Edit Vehicle Profile Page', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,5), ipadx = 2, ipady = 2, fill = "x")


                goToHomePage_button = Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.pack(pady=1,padx=5, side = "left", expand = "no", anchor = "n")




                frame1 = LabelFrame(self, text="General Vehicle Info", width=500, height=300, bd=1, borderwidth=4, relief=GROOVE)
                frame1.place(relx=1,x = -5, rely=0.1, anchor=NE)

                frame2 = LabelFrame(self, text="Drivetrain Info", width=250, height=300, bd=1, borderwidth=4, relief=GROOVE)
                frame2.place(relx=0 ,x = 5, rely=0.2, anchor=NW)

                frame3 = LabelFrame(self, text="Advanced - engine accessories (need all belt-driven accessory pulley diameters)", width=700, height=100, bd=5, borderwidth=3, relief=GROOVE)
                frame3.place(relx=0,x = 5, rely=1, anchor=SW)


##                Name_Label = Label(frame1, text="Enter your vehicle name\n (ex: Steve-Toyota)")
##                Name_Label.pack(pady=5)
##                Name_Entry = Entry(frame1)
##                Name_Entry.pack(padx=5)
##
##                num_Cylinders_Label = Label(frame1, text="Enter number of cylinders")
##                num_Cylinders_Label.pack(pady=5)
##                num_Cylinders_Entry = Entry(self)
##                numCylinders_Entry.pack(padx=5)
##
##                wheel_Circumference_Label = Label(self, text="Enter tire diameter in inches\n (Leave blank if unknown)")
##                wheelCircumference.pack(padx=5)
##                wheel_Circumference_Entry = Entry(self)
##                wheel_Circumference_Entry.pack(padx=5) 
##
##                num_Cylinders_Label = Label(frame1, text="Enter number of cylinders")
##                num_Cylinders_Label.pack(pady=5)
##
##                num_Cylinders_Entry = Entry(frame1)
##                numCylinders_Entry.pack(padx=5)
####
##                
##                first_gear_ratio = 0.0
##                second_gear_ratio = 0.0
##                third_gear_ratio = 0.0
##                fourth_gear_ratio = 0.0
##                fifth_gear_ratio = 0.0
##                sixth_gear_ratio = 0.0
##                reverse_ratio = 0.0
##                converter_ratio = 0.0
##                final_drive_ratio = 0.0

               
class New_Vehicle_Page_Advanced(tk.Frame):
=======
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

                veh_path = str(directory['veh_path'])
                
                # Save vehicle profile in a new file
                with open(veh_path + name + '.json','w') as f:
                        json.dump(data,f)
                        f.close

                # Save vehicle profile to current selected_vehicle
                with open('selected_vehicle.json','w') as f:
                        json.dump(data,f)
                        f.close
                controller.show_page('Home_Page')
>>>>>>> Feature/Plot_From_Tests
        def __init__(self, parent, controller):

                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

                tk.Frame.__init__(self, parent)

                self.controller = controller
<<<<<<< HEAD
                # Advanced controls go here

                self.label = Label(self, text="New Vehicle Advanced Page")
                self.label.pack(pady=5, side = "top", anchor = "n")

                b1 = Button(self, text="I'm scared.  Get me out of here", command=lambda:controller.show_page("NewVehiclePage_Advanced"))
                b1.pack(pady=5)

                b2 = Button(self, text="Advanced is my thing", command=lambda:controller.show_page("HomePage") or print("Advanced window"))
                b2.pack(pady=5)
=======
                
                self.label = ttk.Label(self, text="New Vehicle Page")
                self.label.pack(pady=1,padx=1, side = "top", anchor = "n")

                self.label1 = ttk.Label(self,text = 'Name: ')
                self.label1.pack(side= "top")
                self.entry1 = ttk.Entry(self)
                self.entry1.pack(side = "top")

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

                self.goToHomePage_button = ttk.Button(self, text="Home",
                                    command=lambda: self.saveNewVehicleProfile(controller))
                self.goToHomePage_button.pack(side = "left", expand = "no", anchor = "n")
>>>>>>> Feature/Plot_From_Tests


