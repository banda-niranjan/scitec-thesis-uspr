import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Sampling frequency
sampling_freq = 1e7; #Rule of thumb - 10 times the central frequency of the transducer

#Sampling Interval
sampling_interval= 1/sampling_freq;

dataframe_raw = pd.read_excel(r'..\Excel data\1MHz_Raw_vs_Connected.xlsx', sheet_name=0);
dataframe_connected = pd.read_excel(r'..\Excel data\1MHz_Raw_vs_Connected.xlsx', sheet_name=1);
time_1mhz = dataframe_raw["Time (µs) - Channel 1"].tolist()

amplitude_1mhz_raw = dataframe_raw["Amplitude (mV) - Channel 1"].tolist()
amplitude_1mhz_connected = dataframe_connected["Amplitude (mV) - Channel 1"].tolist()


#Fourier for raw data
fourier_raw = np.fft.fft(amplitude_1mhz_raw)/len(amplitude_1mhz_raw);
fourier_raw = fourier_raw[range(int(len(amplitude_1mhz_raw)/2))];
tpcount_raw = len(amplitude_1mhz_raw)
values_raw = np.arange(int(tpcount_raw/2))
timePeriod_raw = tpcount_raw/sampling_freq
frequencies_raw = values_raw/timePeriod_raw

#Fourier for piezo connected to the sample
fourier_connected = np.fft.fft(amplitude_1mhz_connected)/len(amplitude_1mhz_connected);
fourier_connected = fourier_connected[range(int(len(amplitude_1mhz_connected)/2))];
tpcount_connected = len(amplitude_1mhz_connected)
values_connected = np.arange(int(tpcount_connected/2))
timePeriod_connected = tpcount_connected/sampling_freq
frequencies_connected = values_connected/timePeriod_connected

#Subplots
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(time_1mhz, amplitude_1mhz_raw)
axs[0, 0].set_title('t vs A - Raw')
axs[0, 1].plot(time_1mhz, amplitude_1mhz_connected, 'tab:orange')
axs[0, 1].set_title('t vs A - Connected')
axs[1, 0].plot(frequencies_raw, abs(fourier_raw), 'tab:green')
axs[1, 0].set_title('f vs A - Raw')
axs[1, 1].plot(frequencies_connected, abs(fourier_connected), 'tab:red')
axs[1, 1].set_title('f vs A - Connected')

fig.tight_layout(pad=1.8) #Size padding
fig.suptitle("1 MHz Piezo - With and without the connection")
plt.savefig("Results - Raw vs Connected")
plt.show()
