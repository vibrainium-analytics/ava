from scipy.fftpack import fft, ifft, rfft, rfftfreq
class FFT_Library:
    ## CalculateFFT
    ## Description: Inputs an aray of data and performs an rFFT.
    ##              Uses all 256 data points for FFT, then returns
    ##              Last 255 data points, which excludes freq = 0 (DC component)ß
    ## Inputs:
    ##              data = array of values (x,y) to process
    ## Outputs:
    ##              x = array of frequencies from 1 to 256 (excludes DC freq 0)
    ##              y = array of magnitudes from 1 to 256 (excludes DC freq 0)
    ##
    def CalculateFFT (data):
        freq_ndarray = rfftfreq(256,.002)   # Array of frequencies
        top1k = data[:256] # First 1000 data points
        data_fft = rfft(top1k)  # Perform rfft on top1k
        y=abs(data_fft[1:256])  # Get magnitude of all y points 0 -> 256
        x=freq_ndarray[1:256]   # Get all points 0 -> 256

        return x,y  # return x and y values from FFT

