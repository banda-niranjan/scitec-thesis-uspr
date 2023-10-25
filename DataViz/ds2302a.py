import pyvisa
import numpy as np
import pandas as pd

resource_manager = pyvisa.ResourceManager()

#Instrument settings
my_instrument = resource_manager.open_resource("USB0::0x1AB1::0x04B0::DS2D244503546::INSTR")
print(my_instrument.query("*IDN?"))
my_instrument.timeout = 10000

#System Preset
my_instrument.write(":SYSTem:PRESet")

#Enables counter on Oscilloscope for selected channel
my_instrument.write(":MEASure:COUNter:SOURce CHANnel1")

#Returns frequency for the selected channel
tempval = my_instrument.query(":MEASure:FREQuency? CHANnel1")
print("Frequency in MHz", float(tempval)/1e6)

#Returns Voltage amplitude for the selected channel
vamp = my_instrument.query(":MEASure:VAMP? CHANnel1")
print(vamp)



