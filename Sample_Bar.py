import tkinter as tk
from tkinter import ttk
import urllib.request
import glob, os
import json

class Sample_Bar(tk.Tk):
                
    def __init__(self,*args):
        tk.Tk.__init__(self,*args)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=250, mode="determinate")
        self.progress.pack()
        self.title('Test is progress')
        val = 0
        maxval = 1
        self.progress["maximum"] = 1
        self.test()

    def updating(self,val):
        self.progress["value"] = val

    def test(self,i=0):

        path ="/home/pi/ava/vehicle_profiles/" 
        os.chdir(path)
        with open('data.json','r') as f:
            data = json.load(f)
        samples = int(data['test_duration'])
        wait = samples
        if samples == 0:
            wait = 1
            i = wait
        else:
            rem = i/wait
            self.updating(rem)
        if i < wait:
            self.after(10000, self.test, i+1)
            delay = urllib.request.urlopen("http://192.168.1.1/S")
            count = delay.read()
            delay.close()
        elif i == wait:
            self.destroy()
            print('test is done')
