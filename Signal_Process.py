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

    # read magnitude values from all files into array

##    mag = numpy.zeros(0)
##    m = mag
##
##    
##
##    for j in range(0, count):
##        filename = datapath + fname + str(j+1) + '.txt'
##        f=open(filename,'r')
##        data=f.readlines()
##        f.close()
##        m = numpy.zeros(len(data)-1)
##        for i in range(0, len(data)-1):
##            row = data[i]        
##            col = row.split()
##            m[i] = col[2]
##        mag = numpy.append(mag,m)
##        
##    # calculate running average of fft
##    strt = 1
##    fnsh = n 
##    smpl = mag[strt:fnsh]
##    fq=numpy.absolute(numpy.fft.rfft(smpl))
##    fq[0] = 0
##    for j in range(1, runav):
##        strt = fnsh+1
##        fnsh = fnsh+n
##        smpl = mag[strt:fnsh]
##        fq1=numpy.absolute(numpy.fft.rfft(smpl))
##        fq1[0] = 0
##        fq = ((fq*j) + fq1)/(j+1)
##    while (fnsh+n) < len(mag):
##        strt = fnsh+1
##        fnsh = fnsh+n
##        smpl = mag[strt:fnsh]
##        fq1=numpy.absolute(numpy.fft.rfft(smpl))
##        fq1[0] = 0
##        fq = ((fq*runav) + fq1)/(runav+1)
##        
##    # normalize fft
##    s = numpy.sum(fq)
##    norm = s/(len(fq))
##    fq = fq / norm
##
##    # write output to file
##    filename2 = datapath + 'fft' + str(freq/2) + 'Hz.txt'
##    for i in range(0, int(n/2)):
##        hz = float("{0:.1f}".format(i * freq/n))
##        enrg = str(hz) + ' ' + str(float("{0:.2f}".format(fq[i]))) + '\n'
##        with open(filename2, 'a') as out:
##            out.write(enrg)
##    f.close
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
##            self.after(10000, self.destroy)
                

