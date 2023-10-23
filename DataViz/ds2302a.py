import pyvisa
import pandas as pd

resource_manager = pyvisa.ResourceManager()
# You can change the variable names and resource name

oscii = resource_manager.open_resource("USB0::0x1AB1::0x04B0::DS2D244503546::INSTR")

print(oscii)
print(oscii.query("*IDN?"))


