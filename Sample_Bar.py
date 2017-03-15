import tkinter as tk
from tkinter import ttk
import os, json, shutil, math, urllib.request

class Sample_Bar(tk.Tk):

    # create progress bar
    def __init__(self,*args):
        tk.Tk.__init__(self,*args)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=250, mode="determinate")
        self.progress.pack()
        self.title('Test progress')
        val = 0
        maxval = 1
        self.progress["maximum"] = 1
        self.test()
        
    # update the progress
    def updating(self,val):
        self.progress["value"] = val

    # sample vibration data 
    def test(self,i=0):   

        # a function will be made here that uses the following values to determine the orientation of the sensor
        # and remove the at rest values from the measured vibrations. This is done prior to the calculation of the
        # vibration magnitude to remove noise from the frequency spectrum.
        
        xo = 2065                   # x-axis zero vibration no load
        xup = 2475                  # x-axis zero vibration positive g
        xdwn = 1650                 # x-axis zero vibration negative g
        yo = 2020                   # y-axis zero vibration no load
        yup = 2440                  # y-axis zero vibration positive g
        ydwn = 1605                 # y-axis zero vibration negative g
        zo = 2090                   # z-axis zero vibration no load
        zup = 2510                  # z-axis zero vibration positive g
        zdwn = 1675                 # z-axis zero vibration negative g
              
        # get test data from .json file
        with open('data.json','r') as f:
            data = json.load(f)
            f.close    

        # The test duration is in minutes. The sample loop on the sensor module is 8 seconds plus 2 seconds for the progress bar to update
        samples = 6 * (int(data['test_duration']))    
        testnm = str(data['test_type'])

        # get directories info from .json files
        with open('directory.json','r') as f:
            data_dir = json.load(f)
            f.close
        with open('data1.json','r') as f:
            data1 = json.load(f)
            f.close

        # set directories
        path = str(data_dir['veh_path'])
        path = path + str(data1['name']) + '_' + str(data1['make']) + '/' + testnm + '/'
        path1 = path + 'temp1/'
        path2 = path + 'temp/'

        # samples = 0 is a debug feature that bypasses sampling
        if samples == 0:
            self.destroy()
            print ('ok')

        # if samples is anything other than zero the progress bar is updated       
        else:

            # for first loop i = 0 make directories only once remove them if they exist.
            if i == 0:
                if os.path.exists(path1):
                    shutil.rmtree(path1)
                os.makedirs(path1)
                if os.path.exists(path2):
                    shutil.rmtree(path2)
                os.makedirs(path2)

            # calculate amount of progress bar remaining    
            rem = i/samples
            self.updating(rem)

            # if the progress bar is not filled sample vibration data from sensor module
            if i < samples:
                name = 'Three Axes' + str(i+1)                                               
                mkr = urllib.request.urlopen("http://192.168.1.1/A")
                accl = mkr.read().decode()
                mkr.close()
                filenam = path1 + name + '.txt'
                f = open(filenam,"w")
                f.write(accl)
                f.close 
                self.after(2000, self.test, i+1)        # 2 second delay to update progress bar
                
            # when sampling is done the magnitude of the vibrations is calculated and the 8 sample files are placed into one file
            # the individual files are removed along with one of the temp folders
            elif i == samples:
                accl = ''
                for j in range (1, samples+1):
                    name = 'Three Axes' + str(j)
                    filenam = path1 + name + '.txt'
                    f = open(filenam, 'r')
                    data=f.readlines()
                    f.close
                    for i in range(0, 4096):
                        row = data[i]
                        col = row.split()
                        x = float(col[0]) - xo
                        y = float(col[1]) - ydwn
                        z = float(col[2]) - zo
                        mag = int(math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2)))
                        a = str(col[0]) + ' ' + str(col[1]) + ' ' + str(col[2]) + ' ' + str(mag) + '\n'
                        accl = accl + a
                
                fname2 = path2 + 'Three Axes' + '.txt'
                f=open(fname2,'w')
                f.write(accl)
                f.close 
                shutil.rmtree(path1)
                self.destroy()
                print('test is done')
