import tkinter as tk
from tkinter import ttk
import urllib.request
import glob, os
import json
from Sample_Bar import Sample_Bar

class Delay_Bar(tk.Tk):
                
    def __init__(self,*args):
        tk.Tk.__init__(self,*args)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=250, mode="determinate")
        self.progress.pack()
        self.title('Waiting for test to begin')
        val = 0
        maxval = 1
        self.progress["maximum"] = 1
        self.test()

    def updating(self,val):
        self.progress["value"] = val
        print(val)
        
    def test(self,i=0):


        with open('data.json','r') as f:
            data = json.load(f)
            f.close
        pause = int(data['delay_time'])
        wait = pause*5
        if pause == 0:
            wait = 1
            i = wait
        else:
            rem = i/wait
            self.updating(rem)
        if i < wait:
            delay = urllib.request.urlopen("http://192.168.1.1/D")
            count = delay.read()
            delay.close()
            self.after(2000, self.test, i+1)
        elif i == wait:
            self.destroy()
            print('sampling')
            Sample_Bar()
