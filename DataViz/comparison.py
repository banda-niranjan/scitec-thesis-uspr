import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Sampling frequency
sampling_freq = 2e6;

#Sampling Interval
sampling_interval= 1/sampling_freq;

time_40khz = list(np.arange(0,0.0003,0.000001));

time_1mhz = list(np.arange(0,0.0003,0.000001));

dataframe = pd.read_excel(r"C:/Users/banda/PycharmProjects/pythonProject/scitec/Excel Data/Results Overlap - 40KHz vs 1 MHz.xlsx", sheet_name=0);

amplitude_1mhz = dataframe["Amplitude (mV) - Channel 1"].tolist()
amplitude_40khz = dataframe["Amplitude (mV) - Channel 2"].tolist()

plt.plot(time_1mhz, amplitude_1mhz)
plt.plot(time_40khz, amplitude_40khz)

plt.show()

fourier = np.fft.fft(amplitude_40khz)/len(amplitude_40khz);
fourier = fourier[range(int(len(amplitude_40khz)/2))];

tpcount = len(amplitude_40khz)
values = np.arange(int(tpcount/2))
timePeriod = tpcount/sampling_freq
frequencies = values/timePeriod

fourier1 = np.fft.fft(amplitude_1mhz)/len(amplitude_1mhz);
fourier1 = fourier1[range(int(len(amplitude_1mhz)/2))];

tpcount1 = len(amplitude_1mhz)
values1 = np.arange(int(tpcount1/2))
timePeriod1 = tpcount1/sampling_freq
frequencies1 = values1/timePeriod1


plt.plot(frequencies, abs(fourier))
plt.plot(frequencies1, abs(fourier1))
plt.show()