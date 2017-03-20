import tkinter as tk
from tkinter import ttk
import os, json, shutil, math, urllib.request

class Sample_Bar(tk.Tk):

    # create progress bar
    def __init__(self,*args):

        with open('directory.json','r') as g:
            global directory
            directory = json.load(g)
            g.close
            
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
        # get test data from .json file
        with open(directory['app_data'] + 'test_preferences.json','r') as f:
            data = json.load(f)
            f.close

        with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
            data1 = json.load(f)
            f.close

        # The test duration is in minutes. The sample loop on the sensor module is 8 seconds
        # plus 2 seconds for the progress bar to update, ten seconds total

        samples = 6 * (int(data['test_duration']))    
        testnm = str(data['test_type'])

        # set directories
        veh_path = str(directory['veh_path'])
        home = str(directory['home'])
        path = directory['veh_path'] + str(data1['name']) + '_' + str(data1['make']) + '/' + testnm + '/'
        path1 = path + 'temp1/'
        path2 = path + 'temp/'

        # for first loop i = 0 make directories only once remove them if they exist.
        if i == 0:
            if os.path.exists(path1):
                shutil.rmtree(path1)
            os.makedirs(path1)
            if os.path.exists(path2):
                shutil.rmtree(path2)
            os.makedirs(path2)

        # samples = 0 is a simulated test that bypasses sampling
        if samples == 0:
            accl = ''
            sim_file = directory['home'] + 'A_0.txt'
            f = open(sim_file, 'r')
            data=f.readlines()
            f.close
            end = (int((len(data))/4096))*4096
            
            for i in range(0, end-1):
                row = data[i]
                col = row.split()
                x = float(col[0]) 
                y = float(col[1]) 
                z = float(col[2]) 
                mag = int(math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2)))
                a = str(col[0]) + ' ' + str(col[1]) + ' ' + str(col[2]) + ' ' + str(mag) + '\n'
                accl = accl + a
            fname2 = path2 + 'Three Axes' + '.txt'
            f=open(fname2,'w')
            f.write(accl)
            f.close
            self.destroy()
            print ('simulated sampling complete')
      
        else:
            # if samples is anything other than zero the progress bar is updated   
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
                        x = float(col[0]) 
                        y = float(col[1]) 
                        z = float(col[2])  
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
