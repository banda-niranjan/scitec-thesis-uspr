import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Sampling frequency
# Rule of thumb - 10 times the central frequency of the transducer
sampling_freq = 1e7

#Sampling Interval
sampling_interval= 1/sampling_freq

fft_data = pd.read_csv("C:/Users/niran/PycharmProjects/scitec/Excel data/FFTCircuitMine.csv", header = 0)

time = fft_data["X"][1:].tolist()
amplitude = fft_data["CH1"][1:].tolist()

array_time = np.array(time)
array_amplitude = np.array(amplitude)

#Fourier for raw data
fourier_1mhz = np.fft.fft(amplitude)/len(amplitude)
fourier_1mhz = fourier_1mhz[range(int(len(amplitude)/2))]

tpcount_raw = len(amplitude)
values_raw = np.arange(int(tpcount_raw/2))
timePeriod_raw = tpcount_raw/sampling_freq
frequencies_raw = values_raw/timePeriod_raw

plt.plot(frequencies_raw, abs(fourier_1mhz) )
plt.show()