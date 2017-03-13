import tkinter as tk
from tkinter import ttk
import glob, os
import json
import shutil
import math
import numpy


class Signal_Process(tk.Tk):

    def __init__(self,*args):
        tk.Tk.__init__(self,*args)
        self.message = tk.Text(self, height=2, width=30)
        self.message.pack()
        self.message.insert(tk.INSERT, "Processing Data Please Wait")
        self.title('Processing')
        self.process()

    def process(self):
            
        # set directories using data from .json files
        with open('data.json','r') as f:
            data = json.load(f)
            f.close

        with open('data1.json','r') as f:
            data1 = json.load(f)
            f.close

        with open('data2.json','r') as f:
            data2 = json.load(f)
            f.close 

        with open('directory.json','r') as f:
            data_dir = json.load(f)
            f.close

        if str(data2['idle_status']) == 'Yes':
            testnm = '-Idle'
            if str(data2['ac_status']) == 'AC On':
                testnm = testnm + '-AC'
        else:
            testnm = 'SteadySpeed-' + str(data2['speed'])
            
        path = str(data_dir['veh_path'])
        path = path + str(data1['name']) + '_' + str(data1['make']) + '/' + str(data['test_type'])
        path1 = path + '/temp/'
        path2 = path + testnm + '/'
        os.makedirs(path2)
        
        # read magnitude values from all files into array

        filename = path1 + 'Three Axes.txt'
        f=open(filename,'r')
        data=f.readlines()
        f.close()
        
        m = numpy.zeros(len(data)-1)
        for i in range(0, len(data)-1):
            row = data[i]        
            col = row.split()
            m[i] = col[3]
        mag = numpy.zeros(0)
        mag = numpy.append(mag,m)
            
        # calculate running average of fft

        n = 256
        strt = 1
        fnsh = n
        runav = 16
        smpl = mag[strt:fnsh]
        freq=numpy.absolute(numpy.fft.rfft(smpl))
        freq[0] = 0
        for j in range(1, runav):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq = ((freq*j) + freq1)/(j+1)
        while (fnsh+n) < len(mag):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq = ((freq*runav) + freq1)/(runav+1)
            
        # normalize fft
        s = numpy.sum(freq)
        norm = s/(len(freq))
        freq = freq / norm

        # write output to file
        filename2 = path2 + 'fft 250Hz.txt'
        for i in range(0, int(n/2)):
            hz = float("{0:.1f}".format(i * 500/n))
            enrg = str(hz) + ' ' + str(float("{0:.2f}".format(freq[i]))) + '\n'
            with open(filename2, 'a') as out:
                out.write(enrg)
        f.close
        self.destroy()

    
##    freq = freq/2
##    k=2
##    while k < 4:
##        b, a = signal.butter(20, .5)
##        mag1 = signal.filtfilt(b, a, mag)
##        stp = (int((len(mag)/k)-runav))
##        mag = numpy.zeros(0)
##        for i in range(1, stp):
##            mag = numpy.append(mag,mag1[(2*i)-1])
##        
##        # calculate running average of fft
##        strt = runav
##        fnsh = n + runav-1
##        smpl = mag[strt:fnsh]
##        fq=numpy.absolute(numpy.fft.rfft(smpl))
##        fq[0] = 0
##        for j in range(1, runav):
##            strt = fnsh+1
##            fnsh = fnsh+n
##            smpl = mag[strt:fnsh]
##            fq1=numpy.absolute(numpy.fft.rfft(smpl))
##            fq1[0] = 0
##            fq = ((fq*j) + fq1)/(j+1)
##        while (fnsh+n) < len(mag):
##            strt = fnsh+1
##            fnsh = fnsh+n
##            smpl = mag[strt:fnsh]
##            fq1=numpy.absolute(numpy.fft.rfft(smpl))
##            fq1[0] = 0
##            fq = ((fq*runav) + fq1)/(runav+1)
##
##        # normalize fft
##        s = numpy.sum(fq)
##        norm = s/(len(fq))
##        fq = fq / norm  
##
##        # write output to file
##        filename2 = datapath + 'fft' +str(freq/2) + 'Hz.txt'
##        for i in range(0, int(n/2)):
##            hz = float("{0:.1f}".format(i * freq/n))
##            enrg = str(hz) + ' ' + str(float("{0:.2f}".format(fq[i]))) + '\n'
##            with open(filename2, 'a') as out:
##                out.write(enrg)
##        f.close
##        freq = freq/(2)
##        k = k+1    
##


                

