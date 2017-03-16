import tkinter as tk
from tkinter import ttk
from Sample_Bar import Sample_Bar
import os, json, urllib.request

class Delay_Bar(tk.Tk):

    # set up progress bar frame                
    def __init__(self,*args):
        tk.Tk.__init__(self,*args)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=250, mode="determinate")
        self.progress.pack()
        self.title('Waiting for test to begin')
        val = 0
        maxval = 1
        self.progress["maximum"] = 1
        self.test()

    # function for updating the progress bar
    def updating(self,val):
        self.progress["value"] = val

    # function to communicate with sensor module and countdown delay timer    
    def test(self,i=0):

        # get delay time from .json file
        with open('data.json','r') as f:
            data = json.load(f)
            f.close
        pause = int(data['delay_time'])             # pause is the delay time in minutes

        # 50 seconds of the delay comes from the sensor module. sensor module has built in 10 second timer
        wait = pause*5                              # wait is the delay time in seconds - time to update progress bar

        # if pause is 0 there will be no delay
        if pause == 0:
            self.destroy()
            print('sampling')
            Sample_Bar()
            # call the function to begin sampling vibration data

        else:
            rem = i/wait                            # rem is the amount of progress bar which is filled
            self.updating(rem)

            # if the wait period is not over read the 10 second delay function from the sensor module
            if i < wait:
                delay = urllib.request.urlopen("http://192.168.1.1/D")
                count = delay.read()
                delay.close()
                self.after(2000, self.test, i+1)    # we give the progress bar 2 seconds to update (5*2 = 10, the remaining delay time)
            elif i == wait:
                self.destroy()
                print('sampling')
                Sample_Bar()                        # call the function to begin sampling vibration data

