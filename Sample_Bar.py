import tkinter as tk
from tkinter import ttk
import urllib.request
import glob, os
import json
import shutil
import math

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
              
        fname = "Three Axes"
        xo = 2050                   # x-axis zero vibration value            
        yo = 1605                   # y-axis zero vibration value
        zo = 2060                   # z-axis zero vibration value 
              
        # get test data from .json file
        
        with open('data.json','r') as f:
            data = json.load(f)
            f.close
            
        samples = 6 * (int(data['test_duration']))
        testnm = str(data['test_type'])

        # set directories from .json file
        with open('directory.json','r') as f:
            data_dir = json.load(f)
            f.close

        with open('data1.json','r') as f:
            data1 = json.load(f)
            f.close
        
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
            rem = i/samples
            self.updating(rem)

        # for first loop i = 0 make directories only once. 
            if i == 0:
                os.makedirs(path1)
                os.makedirs(path2)

            if i < samples:
                name = fname + str(i+1)
                mkr = urllib.request.urlopen("http://192.168.1.1/A")
                accl = mkr.read().decode()
                mkr.close()
                filenam = path1 + name + '.txt'
                f = open(filenam,"w")
                f.write(accl)
                f.close
                self.after(2000, self.test, i+1)

            # when sampling is done the progress bar goes away

            elif i == samples:
                self.destroy()
                print('test is done')

                # Calculate magnitude of the 3-axis vibrations and reduce DC component

                for j in range(0, samples):
                    fname1 = path1 + fname + str(j+1) + '.txt'
                    f=open(fname1,'r')
                    data=f.readlines()
                    f.close
                    fname2 = path2 + fname + '.txt'
                    f=open(fname2,'a')
                    for i in range(0, len(data)-1):
                        row = data[i]
                        col = row.split()
                        x = float(col[0]) - xo
                        y = float(col[1]) - yo
                        z = float(col[2]) - zo
                        mag = int(math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2)))
                        data1 = str(col[0]) + ' ' + str(col[1]) + ' ' + str(col[2]) + ' ' + str(mag) + '\n'
                        f.write(data1)
                    f.close 
                shutil.rmtree(path1)


            
