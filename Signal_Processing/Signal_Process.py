import tkinter as tk
from tkinter import ttk
from scipy import signal
import os, json, shutil, math, numpy
import datetime

class Signal_Process(tk.Tk):

    with open('directory.json','r') as g:
            global directory
            directory = json.load(g)
            g.close

    # create a message box. This will only display if the signal processing has an error
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
        with open(directory['app_data'] + 'test_preferences.json','r') as f:
            test_data = json.load(f)
            f.close
        with open(directory['app_data'] + 'selected_vehicle.json','r') as f:
            data1 = json.load(f)
            f.close
        with open(directory['app_data'] + 'save_test.json','r') as f:
            data2 = json.load(f)
            f.close
        with open(directory['app_data'] + 'plot_preferences.json','r') as f:
            plot_preferences = json.load(f)
            f.close

        # set AC status and speed status dependancies
        if str(data2['idle_status']) == 'Yes':
            testnm = '-Idle'
            if str(data2['ac_status']) == 'AC On':
                testnm = testnm + '-AC'
        else:
            testnm = '-' + str(data2['speed']) + 'mph'

        # set directories using data from .json files
        now = '{:%Y-%b-%d %H:%M}'.format(datetime.datetime.now())
        veh_path = str(directory['veh_path'])

        path = veh_path + str(data1['name']) + '_' + str(data1['model']) + '_' + str(data1['year_Veh'])
        path1 = path + '/' + str(test_data['test_type']) + '/temp/'
        path2 = path + '/' + str(test_data['test_type']) + testnm + '/'
        path3 = veh_path + str(data1['name']) + '_' + str(data1['model'])+ '_' + str(data1['year_Veh']) + '/Baseline' + testnm

        # create folder name for trouble data that does not match historical data
        if str(test_data['test_type']) == "Diagnostic":
            path2 = path + '/unknown_trouble' + testnm + '-' + now + '/'

        path4 = path + '/' + testnm + '-Newest_Test/'
        if os.path.exists(path4):
            shutil.rmtree(path4) 

        if os.path.exists(path2):
            shutil.rmtree(path2)            # warning before baseline overwrite will be placed here.
        os.makedirs(path2)

        

        # read magnitude values into array and move raw data to new directory
        filename = path1 + 'Three Axes.txt'
        filename2 = path2 + 'Three Axes.txt'
        filename3 = path2 + 'Compare.txt'

        f=open(filename,'r')
        data=f.readlines()
        f.close()
        shutil.move(filename,filename2)
        shutil.rmtree(path + '/' + str(test_data['test_type']))
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
        out.close

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
        freq2=numpy.absolute(numpy.fft.rfft(smpl))
        freq2[0] = 0

        # until we have done 8 FFT's it is a simple average
        for j in range(1, runav):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq2 = ((freq2*j) + freq1)/(j+1)

        # weighted average until end of samples
        while (fnsh+n) < len(mag):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq2 = ((freq2*runav) + freq1)/(runav+1)

        # normalize fft
        s = numpy.sum(freq2)
        norm = s/(len(freq2))
        freq2 = freq2 / norm
        freq = numpy.append(freq,freq2)

        # write output to file with frequency scale
        filename2 = path2 + 'fft 125Hz.txt'
        for i in range(0, int(n/2)):
            j = i+1
            hz = float("{0:.1f}".format(j * 250/n))
            enrg = str(hz) + ' ' + str(float("{0:.2f}".format(freq2[i]))) + '\n'
            with open(filename2, 'a') as out:
                out.write(enrg)
        out.close

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
        freq3=numpy.absolute(numpy.fft.rfft(smpl))
        freq3[0] = 0

        # until we have done 4 FFT's it is a simple average
        for j in range(1, runav):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq3 = ((freq3*j) + freq1)/(j+1)

        # weighted average until end of samples
        while (fnsh+n) < len(mag):
            strt = fnsh+1
            fnsh = fnsh+n
            smpl = mag[strt:fnsh]
            freq1=numpy.absolute(numpy.fft.rfft(smpl))
            freq1[0] = 0
            freq3 = ((freq3*runav) + freq1)/(runav+1)

        # normalize fft
        s = numpy.sum(freq3)
        norm = s/(len(freq3))
        freq3 = freq3 / norm
        freq = numpy.append(freq,freq3)

        # write output to file with frequency scale
        filename2 = path2 + 'fft 62.5Hz.txt'
        for i in range(0, int(n/2)):
            j = i+1
            hz = float("{0:.1f}".format(j * 125/n))
            enrg = str(hz) + ' ' + str(float("{0:.2f}".format(freq3[i]))) + '\n'
            with open(filename2, 'a') as out:
                out.write(enrg)
        out.close

        # create file to use for comparison
        for i in range(0, 384):
            enrg = str(float("{0:.2f}".format(freq[i]))) + '\n'
            with open(filename3, 'a') as out:
                out.write(enrg)
            out.close

        # comparison code

        # if we are running a diagnostic load the compare files from baseline and compare them to current data.
        filename = path3 + '/Compare.txt'
        if str(test_data['test_type']) == "Diagnostic" and os.path.isfile(filename):
            
            f=open(filename,'r')
            base_line=f.readlines()
            f.close()
            difference = numpy.zeros(384)

            # signal has more noise when vehicle is in motion so the parameters are different.
            if testnm == "-Idle" or testnm == "-Idle-AC":
                b_peak = 1.25
                d_peak = 1.13
            else:
                b_peak = 1.6
                d_peak = 1.3

            # subtract baseline data from current test data
            for i in range (0 , 384):
                base_line[i] = float(base_line[i])
                difference[i] = abs(float("{0:.2f}".format(freq[i] - base_line[i])))

            # find number of peaks above baseline parameter
            base_peak = [x for x in base_line if x >= b_peak]

            # find number of peaks above difference parameter
            unmatch = [x for x in difference if x >= d_peak]

            # find the percent change in peaks from the baseline to the difference
            percent = float("{0:.2f}".format(100*(1-(len(unmatch)/len(base_peak)))))

            # if there are more peaks in the difference than in the baseline the match percentage is zero
            if percent < 0:
                percent = 0

            # if the match is above 90% timestamp and name as baseline
            if percent > 90:
                path5 = path3 + '-' + str(percent) + '%-' + now + '/'
                shutil.copytree(path2, path4)
                os.rename(path2, path5)
                

            # if the baseline was not a match check historical trouble cases for selected test type.
            else:
                match_file = ""
                pathm = path + '/'
                match = {}
                current = path2 + 'Compare.txt'
                for root, dirs, files in os.walk(path):
                    if 'Compare.txt' in files:
                        match_file = os.path.join(root,'Compare.txt')
                    if testnm in match_file and not match_file == current:
                        match_path = match_file.replace('/Compare.txt','')
                        f=open(match_file,'r')
                        comp=f.readlines()
                        f.close()
                        difference = numpy.zeros(384)
                        for i in range (0 , 384):
                            comp[i] = float(comp[i])
                            difference[i] = abs(float("{0:.2f}".format(freq[i] - comp[i])))
                        base_peak = [x for x in comp if x >= b_peak]
                        unmatch = [x for x in difference if x >= d_peak]
                        percent = float("{0:.2f}".format(100*(1-(len(unmatch)/len(base_peak)))))
                        match[str(match_path.replace(pathm,''))] = str(percent)

                        # if the match is above 75% we have a high confidence match.
                        if percent > 75:
                            trouble_match = 'High confidence match to: ' + match_path.replace(pathm,'')
                            print(trouble_match)

                with open(path2 + 'match.json','w') as f:
                        json.dump(match,f)
                        f.close
                shutil.copytree(path2, path4)

        self.destroy()
