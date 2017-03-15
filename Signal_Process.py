import tkinter as tk
from tkinter import ttk
from scipy import signal
import os, json, shutil, math, numpy

class Signal_Process(tk.Tk):

    # create a message box. This will only display if the signal processing takes more than one second
    def __init__(self,*args):
        tk.Tk.__init__(self,*args)
        self.message = tk.Text(self, height=2, width=30)
        self.message.pack()
        self.message.insert(tk.INSERT, "Processing Data Please Wait")
        self.title('Processing')
        self.process()

    # signal processing function
    def process(self):
            
        # get data from .json files
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

        # set AC status and speed status dependancies
        if str(data2['idle_status']) == 'Yes':
            testnm = '-Idle'
            if str(data2['ac_status']) == 'AC On':
                testnm = testnm + '-AC'
        else:
            testnm = 'SteadySpeed-' + str(data2['speed'])

        # set directories using data from .json files    
        path = str(data_dir['veh_path'])
        path = path + str(data1['name']) + '_' + str(data1['make']) + '/' + str(data['test_type'])
        path1 = path + '/temp/'
        path2 = path + testnm + '/'
        if os.path.exists(path2):
           shutil.rmtree(path2)     
        os.makedirs(path2)
        
        # read magnitude values into array and move raw data to new directory
        filename = path1 + 'Three Axes.txt'
        filename2 = path2 + 'Three Axes.txt'
        f=open(filename,'r')
        data=f.readlines()
        f.close()
        shutil.move(filename,filename2)
        shutil.rmtree(path)       
        mag = numpy.zeros(len(data))
        for i in range(0, len(data)-1):
            row = data[i]        
            col = row.split()
            mag[i] = col[3]
            
        # calculate weighted average of fft
        n = 256                                             # number of points in the FFT
        strt = 1
        fnsh = n
        runav = 16                                          # number of FFT's in 8 second weighted average 
        smpl = mag[strt:fnsh]

        # first FFT is outside the average loop so we aren't dividing by zero
        freq=numpy.absolute(numpy.fft.rfft(smpl))
        freq[0] = 0

        # until we have done 16 FFT's it is a simple average
        for j in range(1, runav):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq = ((freq*j) + freq1)/(j+1)

        # weighted average until end of samples
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

        # write output to file with frequency scale
        filename2 = path2 + 'fft 250Hz.txt'
        for i in range(0, int(n/2)):
            j = i+1
            hz = float("{0:.1f}".format(j * 500/n))
            enrg = str(hz) + ' ' + str(float("{0:.2f}".format(freq[i]))) + '\n'
            with open(filename2, 'a') as out:
                out.write(enrg)
        f.close

        # create filter coefficients for zooming in by 2
        b, a = signal.butter(20, .5)

        # filter magnitude values that were read earlier
        mag1 = signal.filtfilt(b, a, mag)

        # downsample by 2 to avoid aliasing
        stp = int(len(mag)/2)
        mag = numpy.zeros(0)
        for i in range(1, stp):
            mag = numpy.append(mag,mag1[(2*i)-1])

        # calculate weighted average of fft
        n = 256                                                 # number of points in the FFT
        strt = 1
        fnsh = n
        runav = 8                                               # number of FFT's in 8 second weighted average
        smpl = mag[strt:fnsh]

        # first FFT is outside the average loop so we aren't dividing by zero
        freq=numpy.absolute(numpy.fft.rfft(smpl))
        freq[0] = 0

        # until we have done 8 FFT's it is a simple average
        for j in range(1, runav):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq = ((freq*j) + freq1)/(j+1)

        # weighted average until end of samples
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

        # write output to file with frequency scale
        filename2 = path2 + 'fft 125Hz.txt'
        for i in range(0, int(n/2)):
            j = i+1
            hz = float("{0:.1f}".format(j * 250/n))
            enrg = str(hz) + ' ' + str(float("{0:.2f}".format(freq[i]))) + '\n'
            with open(filename2, 'a') as out:
                out.write(enrg)
        f.close

        # create filter coefficients for zooming in by 2
        b, a = signal.butter(20, .5)

        # filter magnitude values from the previously filtered data
        mag1 = signal.filtfilt(b, a, mag)

        # downsample by 2 to avoid aliasing
        stp = int(len(mag)/2)
        mag = numpy.zeros(0)
        for i in range(1, stp):
            mag = numpy.append(mag,mag1[(2*i)-1])

        # calculate weighted average of fft
        n = 256                                                 # number of points in the FFT 
        strt = 1
        fnsh = n
        runav = 4                                               # number of FFT's in 8 second weighted average
        smpl = mag[strt:fnsh]

        # first FFT is outside the average loop so we aren't dividing by zero
        freq=numpy.absolute(numpy.fft.rfft(smpl))
        freq[0] = 0

        # until we have done 4 FFT's it is a simple average
        for j in range(1, runav):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq = ((freq*j) + freq1)/(j+1)

        # weighted average until end of samples
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

        # write output to file with frequency scale
        filename2 = path2 + 'fft 62.5Hz.txt'
        for i in range(0, int(n/2)):
            j = i+1
            hz = float("{0:.1f}".format(j * 125/n))
            enrg = str(hz) + ' ' + str(float("{0:.2f}".format(freq[i]))) + '\n'
            with open(filename2, 'a') as out:
                out.write(enrg)
        f.close
        self.destroy()



                

