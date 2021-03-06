import tkinter as tk
from tkinter import ttk
from scipy import signal
import os, json, shutil, math, numpy
import datetime
from tkinter import messagebox as tmb

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

        # set Idle status and speed status dependancies
        if str(data2['idle_status']) == 'Yes':
            testnm = 'Idle'
        else:
            testnm = str(data2['speed']) + 'mph'

        # set directories using data from .json files
        now = '{:%Y-%b-%d %H:%M}'.format(datetime.datetime.now())
        veh_path = str(directory['veh_path'])

        path = veh_path + str(data1['name']) + '_' + str(data1['model']) + '_' + str(data1['year_Veh'])
        path1 = path + '/' + str(test_data['test_type']) + '/temp/'
        path2 = path + '/' + str(test_data['test_type']) + '-' + testnm + '/'
        path3 = path + '/Baseline-' + testnm
        path4 = path + '/' + testnm + '-Newest_Test/'

        # create folder name for trouble data that does not match historical data

        if str(test_data['test_type']) == "Diagnostic":
            path2 = path + '/unknown_trouble' + testnm + '-' + now + '/'

        # Replace newewest test folder (path4). Remove folders from incomplete tests(path2).
        if os.path.exists(path4):
            shutil.rmtree(path4) 
        if os.path.exists(path2):
            shutil.rmtree(path2)           
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
        norm = numpy.amax(freq)
        freq = freq / norm

        # write output to file with frequency scale
        filename2 = path2 + 'fft 250Hz.txt'
        for i in range(0, int(n/2)):
            hz = float("{0:.1f}".format(i * 500/n))
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
        norm = numpy.amax(freq2)
        freq2 = freq2 / norm
        freq = numpy.append(freq,freq2)

        # write output to file with frequency scale
        filename2 = path2 + 'fft 125Hz.txt'
        for i in range(0, int(n/2)):
            hz = float("{0:.1f}".format(i * 250/n))
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
        norm = numpy.amax(freq3)
        freq3 = freq3 / norm
        freq = numpy.append(freq,freq3)

        # write output to file with frequency scale
        filename2 = path2 + 'fft 62.5Hz.txt'
        for i in range(0, int(n/2)):
            hz = float("{0:.1f}".format(i * 125/n))
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
        message_out = 0

        # if we are running a diagnostic load the compare files from baseline and compare them to current data.
        filename = path3 + '/Compare.txt'
        if str(test_data['test_type']) == "Diagnostic" and os.path.isfile(filename):
            
            f=open(filename,'r')
            base_line=f.readlines()
            f.close()

            difference = numpy.zeros(384)
            base_pk_array = numpy.zeros(384)
            test_pk_array = numpy.zeros(384) 

            peaks = [p for p in range(len(base_line)) if float(base_line[p]) > .18]
            for i in range(0,len(peaks)):
                index = peaks[i]
                base_pk_array[index] = 1

            fpeaks = [q for q in range(len(freq)) if freq[q] > .18]
            for i in range(0,len(fpeaks)):
                findex = fpeaks[i]
                test_pk_array[findex] = 1

            for i in range (0 , 384):
                difference[i] = base_pk_array[i] + test_pk_array[i]

            t_match = [x for x in difference if x >= 2]
            percent = 100 * float("{0:.2f}".format(len(t_match) / len(peaks)))
            print('Baseline match ')
            print(percent)

            # if the match is above 90% compare with historical data, timestamp, and inform user of baseline match.
            if percent > 90:
                message_out = 1
                strong_base=tmb.showinfo(title="Strong Match", message="Strong match to saved baseline. Vehicle condition is normal") 
                match_file = ""
                pathm = path + '/'
                match = {}
                current = path2 + 'Compare.txt'

                # compare to all historical data for the selected vehicle.
                
                for root, dirs, files in os.walk(path):
                    if 'Compare.txt' in files:
                        match_file = os.path.join(root,'Compare.txt')
                    if testnm in match_file and not match_file == current:
                        match_path = match_file.replace('/Compare.txt','')
                        f=open(match_file,'r')
                        comp=f.readlines()
                        f.close()

                        match_pk_array = numpy.zeros(384)
                        difference = numpy.zeros(384)

                        peaks = [p for p in range(len(comp)) if float(comp[p]) > .18]
                        for i in range(0,len(peaks)):
                            index = peaks[i]
                            match_pk_array[index] = 1

                        for i in range (0 , 384):
                            difference[i] = match_pk_array[i] + test_pk_array[i]

                        t_match = [x for x in difference if x >= 2]
                        percent = 100 * float("{0:.2f}".format(len(t_match) / len(peaks)))
                        match[str(match_path.replace(pathm,''))] = str(percent)

                        print(match_path)
                        print(percent)

                with open(path2 + 'match.json','w') as f:
                        json.dump(match,f)
                        f.close
                # Rename as baseline with timestamp. Copy into newest test.
                path5 = path3 + '-' + now + '/'
                shutil.copytree(path2, path4)
                os.rename(path2, path5)

            elif percent > 75:
                message_out = 2
                moderate_base=tmb.showinfo(title="Moderate Match", message="Moderate match to saved baseline. View plots to determine vehicle condition")

            # if the baseline was not a match check historical trouble cases for selected vehicle.
            if not message_out == 1:
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

                        match_pk_array = numpy.zeros(384)
                        difference = numpy.zeros(384)

                        peaks = [p for p in range(len(comp)) if float(comp[p]) > .18]
                        for i in range(0,len(peaks)):
                            index = peaks[i]
                            match_pk_array[index] = 1

                        for i in range (0 , 384):
                            difference[i] = match_pk_array[i] + test_pk_array[i]

                        t_match = [x for x in difference if x >= 2]
                        percent = 100 * float("{0:.2f}".format(len(t_match) / len(peaks)))
                        match[str(match_path.replace(pathm,''))] = str(percent)

                        print(match_path)
                        print(percent)

                        # if the match is above 75% we have a high confidence match.
                        if percent > 75:
                            message_out = 3
                            trouble_match = 'Strong match to: ' + match_path.replace(pathm,'') + '. View plots to verify trouble'
                            t_match=tmb.showinfo(title="Strong Match", message=trouble_match) 
                            print(trouble_match)

                with open(path2 + 'match.json','w') as f:
                    json.dump(match,f)
                    f.close    
                if message_out == 0:
                    no_match=tmb.showinfo(title="No Match", message="No match to historical data. Refer to Key Frequencies to isolate trouble")
                shutil.copytree(path2, path4)



        # baseline test does not do comparisons. Folder is still copied to newest test.       
        else:
            shutil.copytree(path2, path4)

        self.destroy()
