
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

# File system access library
import glob, os
import json

class New_Vehicle_Page(tk.Frame):
        def __init__(self, parent, controller):

                # Global directory navigation file
                with open('directory.json','r') as g:
                    global directory
                    directory = json.load(g)
                    g.close

                veh_path = str(directory['veh_path'])

                tk.Frame.__init__(self, parent)

                self.controller = controller

                self.pageLabelFrame=Frame(self, borderwidth=4, relief=GROOVE)
                Label(self.pageLabelFrame, text='New/Edit Profile', width=35).pack(side=TOP)
                self.pageLabelFrame.pack(pady = (5,5), ipadx = 2, ipady = 2, fill = "x")

                goToHomePage_button = Button(self, text="Go Back",
                                    command=lambda: controller.show_page("Home_Page"))
                goToHomePage_button.place(relx = 0, rely = .1, anchor = NW)

                frame1 = LabelFrame(self, text="General Vehicle Info", width=550, height=80, borderwidth=4, relief=GROOVE)
                frame1.place(relx=.18, rely=0.1, anchor=NW)

                frame2 = LabelFrame(self, text="Basic Drivetrain Info", width=275, height=310, borderwidth=4, relief=GROOVE)
                frame2.place(relx=.02, rely=0.30, anchor=NW)

                frame3 = LabelFrame(self, text="Advanced - Pulley Diameters (inches)", width=275, height=310, borderwidth=4, relief=GROOVE)
                frame3.place(relx=.60, rely=.30, anchor=NW)

                frame4 = Frame(self, width = 110, height = 50, borderwidth = 4, relief=GROOVE)
                frame4.place(relx = .40, x = 20, rely = .33, anchor=NW)

                #frame1 (general)
                name_Label = ttk.Label(frame1,text = 'Name: ')
                name_Label.place(relx = 0.03, x = 15, rely = 0.05, anchor=NW)
                name_Entry = ttk.Entry(frame1)
                name_Entry.place(relx = 0.15, rely = 0.05, anchor=NW)

                make_Label = ttk.Label(frame1,text = 'Make: ')
                make_Label.place(relx = .58, rely = 0.05, anchor=NE)
                make_Entry = ttk.Entry(frame1)
                make_Entry.place(relx = .9, x = -5, rely = 0.05, anchor=NE)

                model_Label = ttk.Label(frame1,text = 'Model: ')
                model_Label.place(relx = 0.03, x = 15, rely = 0.55, anchor=NW)
                model_Entry = ttk.Entry(frame1)
                model_Entry.place(relx = 0.15, rely = 0.55, anchor=NW)

                year_Veh_Label = ttk.Label(frame1,text = 'Year: ')
                year_Veh_Label.place(relx = .58, rely = 0.55, anchor=NE)
                year_Veh_Entry = ttk.Entry(frame1)
                year_Veh_Entry.place(relx = .9, x = -5, rely = 0.55, anchor=NE)

                #frame2 (Basic Drivetrain)
                tire_Label = ttk.Label(frame2, text="Tire radius  (inches):")
                tire_Label.place(relx = .02, rely = 0, anchor=NW)
                tire_Entry = ttk.Entry(frame2, width = 6)
                tire_Entry.place(relx = .75, rely = 0, anchor=NW)

                num_Cylinders_Label = ttk.Label(frame2, text="# of cylinders:")
                num_Cylinders_Label.place(relx = 0.02, rely = 0.1, anchor=NW)
                num_Cylinders_Entry = ttk.Entry(frame2, width = 6)
                num_Cylinders_Entry.place(relx = 0.75, rely = 0.1, anchor=NW)

                first_Gear_Label = ttk.Label(frame2, text = "1st gear ratio:")
                first_Gear_Label.place(relx = .02, rely = .2, anchor = NW)
                first_Gear_Entry = ttk.Entry(frame2, width = 6)
                first_Gear_Entry.place(relx = .75, rely = .2, anchor = NW)

                second_Gear_Label = ttk.Label(frame2, text = "2nd gear ratio:")
                second_Gear_Label.place(relx = .02, rely = .3, anchor = NW)
                second_Gear_Entry = ttk.Entry(frame2, width = 6)
                second_Gear_Entry.place(relx = .75, rely = .3, anchor = NW)

                third_Gear_Label = ttk.Label(frame2, text = "3rd gear ratio:")
                third_Gear_Label.place(relx = .02, rely = .4, anchor = NW)
                third_Gear_Entry = ttk.Entry(frame2, width = 6)
                third_Gear_Entry.place(relx = .75, rely = .4, anchor = NW)

                fourth_Gear_Label = ttk.Label(frame2, text = "4th gear ratio:")
                fourth_Gear_Label.place(relx = .02, rely = .5, anchor = NW)
                fourth_Gear_Entry = ttk.Entry(frame2, width = 6)
                fourth_Gear_Entry.place(relx = .75, rely = .5, anchor = NW)

                fifth_Gear_Label = ttk.Label(frame2, text = "5th gear ratio:")
                fifth_Gear_Label.place(relx = .02, rely = .6, anchor = NW)
                fifth_Gear_Entry = ttk.Entry(frame2, width = 6)
                fifth_Gear_Entry.place(relx = .75, rely = .6, anchor = NW)

                sixth_Gear_Label = ttk.Label(frame2, text = "6th gear ratio:")
                sixth_Gear_Label.place(relx = .02, rely = .7, anchor = NW)
                sixth_Gear_Entry = ttk.Entry(frame2, width = 6)
                sixth_Gear_Entry.place(relx = .75, rely = .7, anchor = NW)

                reverse_Gear_Label = ttk.Label(frame2, text = "Reverse gear ratio:")
                reverse_Gear_Label.place(relx = .02, rely = .8, anchor = NW)
                reverse_Gear_Entry = ttk.Entry(frame2, width = 6)
                reverse_Gear_Entry.place(relx = .75, rely = .8, anchor = NW)

                final_Drive_Label = ttk.Label(frame2, text = "Final Drive ratio:")
                final_Drive_Label.place(relx = .02, rely = .9, anchor = NW)
                final_Drive_Entry = ttk.Entry(frame2, width = 6)
                final_Drive_Entry.place(relx = .75, rely = .9, anchor = NW)



                tire_Entry.insert(0,0)
                num_Cylinders_Entry.insert(0,0)
                first_Gear_Entry.insert(0,0)
                second_Gear_Entry.insert(0,0)
                third_Gear_Entry.insert(0,0)
                fourth_Gear_Entry.insert(0,0)
                fifth_Gear_Entry.insert(0,0)
                sixth_Gear_Entry.insert(0,0)
                reverse_Gear_Entry.insert(0,0)
                final_Drive_Entry.insert(0,0)




                #frame3 (Advanced - Engine Accessories)
                main_Pulley_Label = ttk.Label(frame3, text="Crank Pulley Dia:", state = "disabled")
                main_Pulley_Label.place(relx = .02, rely = .05, anchor=NW)
                main_Pulley_Entry = ttk.Entry(frame3, width = 6, state = "disabled")
                main_Pulley_Entry.place(relx = .7, rely = .05, anchor=NW)

                alternator_Label = ttk.Label(frame3, text="Alternator Pulley Dia:", state = "disabled")
                alternator_Label.place(relx = 0.02, rely = 0.15, anchor=NW)
                alternator_Entry = ttk.Entry(frame3, width = 6, state = "disabled")
                alternator_Entry.place(relx = 0.7, rely = 0.15, anchor=NW)

                air_Conditioner_Label = ttk.Label(frame3, text = "Air Conditioner Pulley Dia:", state = "disabled")
                air_Conditioner_Label.place(relx = .02, rely = .25, anchor = NW)
                air_Conditioner_Entry = ttk.Entry(frame3, width = 6, state = "disabled")
                air_Conditioner_Entry.place(relx = .7, rely = .25, anchor = NW)

                waterpump_Label = ttk.Label(frame3, text = "Water Pump Pulley Dia:", state = "disabled")
                waterpump_Label.place(relx = .02, rely = .35, anchor = NW)
                waterpump_Entry = ttk.Entry(frame3, width = 6, state = "disabled")
                waterpump_Entry.place(relx = .7, rely = .35, anchor = NW)

                fan_Label = ttk.Label(frame3, text = "Fan Pulley Dia:", state = "disabled")
                fan_Label.place(relx = .02, rely = .45, anchor = NW)
                fan_Entry = ttk.Entry(frame3, width = 6, state = "disabled")
                fan_Entry.place(relx = .7, rely = .45, anchor = NW)

                powersteer_Label = ttk.Label(frame3, text = "Power Steering Pulley Dia:", state = "disabled")
                powersteer_Label.place(relx = .02, rely = .55, anchor = NW)
                powersteer_Entry = ttk.Entry(frame3, width = 6, state = "disabled")
                powersteer_Entry.place(relx = .7, rely = .55, anchor = NW)

                tension_Label = ttk.Label(frame3, text = "Tension pulley Dia:", state = "disabled")
                tension_Label.place(relx = .02, rely = .65, anchor = NW)
                tension_Entry = ttk.Entry(frame3, width = 6, state = "disabled")
                tension_Entry.place(relx = .7, rely = .65, anchor = NW)

                extra_Accessory_Label = ttk.Label(frame3, text = "Accessory Pulley Dia:\n(example: 2nd alternator \nfor large stereo systems", state = "disabled")
                extra_Accessory_Label.place(relx = .02, rely = .80, anchor = NW)
                extra_Accessory_Entry = ttk.Entry(frame3, width = 6, state = "disabled")
                extra_Accessory_Entry.place(relx = .7, rely = .80, anchor = NW)












                def Advanced_Entry():

                        main_Pulley_Label.configure(state="normal")
                        main_Pulley_Entry.configure(state="normal")
                        alternator_Label.configure(state="normal")
                        alternator_Entry.configure(state="normal")
                        air_Conditioner_Label.configure(state="normal")
                        air_Conditioner_Entry.configure(state="normal")
                        waterpump_Label.configure(state="normal")
                        waterpump_Entry.configure(state="normal")
                        fan_Label.configure(state="normal")
                        fan_Entry.configure(state="normal")
                        powersteer_Label.configure(state="normal")
                        powersteer_Entry.configure(state="normal")
                        tension_Label.configure(state="normal")
                        tension_Entry.configure(state="normal")
                        extra_Accessory_Label.configure(state="normal")
                        extra_Accessory_Entry.configure(state="normal")

                        main_Pulley_Entry.insert(0,0)
                        alternator_Entry.insert(0,0)
                        air_Conditioner_Entry.insert(0,0)
                        waterpump_Entry.insert(0,0)
                        fan_Entry.insert(0,0)
                        powersteer_Entry.insert(0,0)
                        tension_Entry.insert(0,0)
                        extra_Accessory_Entry.insert(0,0)




                        frame2.update()
                        frame3.update()


                def Basic_Entry():

                        main_Pulley_Label.configure(state="disabled")
                        main_Pulley_Entry.configure(state="disabled")
                        alternator_Label.configure(state="disabled")
                        alternator_Entry.configure(state="disabled")
                        air_Conditioner_Label.configure(state="disabled")
                        air_Conditioner_Entry.configure(state="disabled")
                        waterpump_Label.configure(state="disabled")
                        waterpump_Entry.configure(state="disabled")
                        fan_Label.configure(state="disabled")
                        fan_Entry.configure(state="disabled")
                        powersteer_Entry.configure(state="disabled")
                        powersteer_Label.configure(state="disabled")
                        tension_Entry.configure(state="disabled")                       
                        tension_Label.configure(state="disabled")
                        extra_Accessory_Label.configure(state="disabled")
                        extra_Accessory_Entry.configure(state="disabled")

                        main_Pulley_Entry.update()
                        alternator_Entry.update()
                        air_Conditioner_Entry.update()
                        waterpump_Entry.update()
                        fan_Entry.update()
                        powersteer_Entry.update()
                        tension_Entry.update()
                        extra_Accessory_Entry.update()

                        frame2.update()
                        frame3.update()

                def Read_Profile():
                        name = name_Entry.get()
                        make = make_Entry.get()
                        model = model_Entry.get()
                        year_Veh = year_Veh_Entry.get()

                        tirerad = tire_Entry.get()
                        tire = float(tirerad) * 2.0 * 3.1415
                        num_Cylinders = num_Cylinders_Entry.get()
                        first_Gear = first_Gear_Entry.get()
                        second_Gear = second_Gear_Entry.get()
                        third_Gear = third_Gear_Entry.get()
                        fourth_Gear = fourth_Gear_Entry.get()
                        fifth_Gear = fifth_Gear_Entry.get()
                        sixth_Gear = sixth_Gear_Entry.get()
                        reverse_Gear = reverse_Gear_Entry.get()
                        final_Drive = final_Drive_Entry.get()

                        main_Pulley = main_Pulley_Entry.get()
                        alternator = alternator_Entry.get()
                        air_Conditioner =air_Conditioner_Entry.get()
                        waterpump = waterpump_Entry.get()
                        fan = fan_Entry.get()
                        powersteer = powersteer_Entry.get()
                        tension = tension_Entry.get()
                        extra_Accessory = extra_Accessory_Entry.get()

                        profile_data = {
                                'name': name,
                                'make': make,
                                'model': model,
                                'year_Veh': year_Veh,
                                
                                'tire': tire,
                                'tirerad': tirerad, 
                                'num_Cylinders': num_Cylinders,
                                'first_Gear': first_Gear,
                                'second_Gear': second_Gear,
                                'third_Gear': third_Gear,
                                'fourth_Gear': fourth_Gear,
                                'fifth_Gear': fifth_Gear,
                                'sixth_Gear': sixth_Gear,
                                'reverse_Gear': reverse_Gear,
                                'final_Drive': final_Drive,

                                'main_Pulley': main_Pulley,
                                'alternator': alternator,
                                'air_Conditioner': air_Conditioner,
                                'waterpump': waterpump,
                                'fan': fan,
                                'powersteer': powersteer,
                                'tension': tension,
                                'extra_Accessory': extra_Accessory
                        }

                        return profile_data

                def Validate_Data(data):
                        # Loop through profile_data for data validation (No empty strings where values needed, etc.
                        # TODO: add more helpful data validation for integers vs. strings, etc.  Here is where it all should happen.  If invalid, break out of the loop
                        isValidProfile = 1  # initialize
                        for key, value in data.items():
                                if (value == ""):
                                        if key in ['tire','num_Cylinders','first_Gear','first_Gear','second_Gear','third_Gear','fourth_Gear','fifth_Gear', 'sixth_Gear','final_Drive']:
                                                isValidProfile = 1
                                        if key in ['main_Pulley','alternator','air_Conditioner','waterpump','fan','catalytic_Ratio','reverse_Gear', 'extra_Accessory']:
                                                isValidProfile = 1
                                        if key in ['name','make','model','year_Veh']:
                                                isValidProfile = 0
                                                break   # break out of the for loop if invalid profile
                        # DEBUG
                        if(isValidProfile ==0):
                                print('ERROR: Invalid Profile.  Check that all required fields are entered')
                        else:
                                print('Valid Profile.')

                        return isValidProfile

                def Save_To_Profile():

                        profile_data = Read_Profile()

                        isValid = Validate_Data(profile_data)

                        # If data is valid
                        if(isValid == 1):
                                # If profile already exists, edit
                                # Check if vehicle already exists
                                # If vehicle exists, simply update vehicle profile
                                # Load vehicles from vehicle directory
                                from os import listdir
                                vehicle_filenames = os.listdir(directory['veh_path'])
                                formatted_filenames = []

                                found_matching_profile = 0
                                # Format filenames to remove .json extension
                                for filename in vehicle_filenames:
                                        if filename.endswith(".json"):
                                                # If vehicle filename matches profile name
                                                if(profile_data['name'] in filename):
                                                        with open(directory['veh_path'] + str(profile_data['name']) + '.json', 'w') as f:
                                                                json.dump(profile_data,f)
                                                                f.close
                                                        print('Updated previous profile: ' + str(profile_data['name']) + '.json')
                                                        found_matching_profile = 1
                                                        break
                                # If vehicle does not exist, create a new json file profile
                                # Create a new profile
                                if found_matching_profile == 0:
                                        with open(directory['veh_path'] + str(profile_data['name']) + '.json', 'w') as f:
                                                json.dump(profile_data,f)
                                                f.close
                                        print('Created New profile: ' + str(profile_data['name']) + '.json')
                                #TODO: Save current vehicle stats as selected_vehicle json status
                                with open(directory['app_data'] + 'selected_vehicle.json', 'w') as f:
                                        json.dump(profile_data,f)
                                        f.close
                                        print('Selected Vehicle Updated')

                def Load_Saved_Profile ():

                        print ("Load")

                        with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
                                data = json.load(f)
                                f.close
        #DEBUG
                        print(data['name'])


                        name_Entry.delete(0, 'end')
                        make_Entry.delete(0, 'end')
                        model_Entry.delete(0, 'end')
                        year_Veh_Entry.delete(0, 'end')
                        tire_Entry.delete(0, 'end')
                        num_Cylinders_Entry.delete(0, 'end')
                        first_Gear_Entry.delete(0, 'end')
                        second_Gear_Entry.delete(0, 'end')
                        third_Gear_Entry.delete(0, 'end')
                        fourth_Gear_Entry.delete(0, 'end')
                        fifth_Gear_Entry.delete(0, 'end')
                        sixth_Gear_Entry.delete(0, 'end')
                        reverse_Gear_Entry.delete(0, 'end')
                        final_Drive_Entry.delete(0, 'end')

                        main_Pulley_Entry.delete(0, 'end')
                        alternator_Entry.delete(0, 'end')
                        air_Conditioner_Entry.delete(0, 'end')
                        waterpump_Entry.delete(0, 'end')
                        fan_Entry.delete(0, 'end')
                        powersteer_Entry.delete(0, 'end')
                        tension_Entry.delete(0, 'end')
                        extra_Accessory_Entry.delete(0, 'end')

                        name_Entry.insert(0, data['name'])
                        make_Entry.insert(0, data['make'])
                        model_Entry.insert(0, data['model'])
                        year_Veh_Entry.insert(0, data['year_Veh'])
                        tire_Entry.insert(0,data['tirerad'])
                        num_Cylinders_Entry.insert(0, data['num_Cylinders'])
                        first_Gear_Entry.insert(0, data['first_Gear'])
                        second_Gear_Entry.insert(0, data['second_Gear'])
                        third_Gear_Entry.insert(0, data['third_Gear'])
                        fourth_Gear_Entry.insert(0, data['fourth_Gear'])
                        fifth_Gear_Entry.insert(0, data['fifth_Gear'])
                        sixth_Gear_Entry.insert(0, data['sixth_Gear'])
                        reverse_Gear_Entry.insert(0,data['reverse_Gear'])
                        final_Drive_Entry.insert(0, data['final_Drive'])

                        main_Pulley_Entry.insert(0,data['main_Pulley'])
##                        if len(main_Pulley_Entry.get()) == 0:
##                                main_Pulley_Entry.insert(0,'0')
                        alternator_Entry.insert(0,data['alternator'])
                        air_Conditioner_Entry.insert(0,data['air_Conditioner'])
                        waterpump_Entry.insert(0,data['waterpump'])
                        fan_Entry.insert(0,data['fan'])
                        powersteer_Entry.insert(0,data['powersteer'])
                        tension_Entry.insert(0,data['tension'])
                        extra_Accessory_Entry.insert(0,data['extra_Accessory'])



                # Init function continued
                var = StringVar()
                var = 0
                advanced_Radio = Radiobutton(frame4, text='Advanced', variable=var, value="1", command=Advanced_Entry)
                basic_Radio = Radiobutton(frame4, text='Basic', variable=var, value="0", command=Basic_Entry)
                basic_Radio.place(relx =.05,rely=.05, anchor = NW)
                advanced_Radio.place(relx = .05, rely = .55, anchor = NW)

                load_Button = Button(self, text = "Prepopulate", command = Load_Saved_Profile)
                load_Button.place(relx = 0, rely = .2, anchor = NW)

                save_Button = Button(self, text = "Save", command = Save_To_Profile)
                save_Button.place(relx = .4, x = 20, rely = .85, anchor = NW)
