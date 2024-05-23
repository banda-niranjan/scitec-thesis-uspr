import pyvisa as py

#USB0::6833::1200::DS2D244503546::0::INSTR

rm = py.ResourceManager()
print(rm.list_resources())

#Instrument ID obtained from query
my_instrument = rm.open_resource("USB0::6833::1200::DS2D244503546::0::INSTR")
#Query for verification
my_instrument.query("*IDN?")
my_instrument.write(":SYSTem:BEEPer 1")

#Display Channel 1 only with counter
my_instrument.write(":CHANnel1:DISPlay ON")
my_instrument.write(":CHANnel2:DISPlay ON")
my_instrument.write(":MEASure:COUNter:SOURce CHANnel1")

#To set the channel 1, 2 at -10.5V and -10.2V
my_instrument.write(":CHANnel2:OFFSet -10.4")
my_instrument.write(":CHANnel1:OFFSet -8.5")

#To set the horizontal scaling to 2us
my_instrument.write(":TIMebase:SCALe 1e-6")

#To set the horizontal timebase delay to 5us
my_instrument.write(":TIMebase:DELay:ENABle 0")
my_instrument.write(":TIMebase[:MAIN]:OFFSet 6e-6")

#To set the channel 1 vertical scaling to 1.0V
my_instrument.write(":CHANnel1:SCALe 2.0")
my_instrument.write(":CHANnel2:SCALe 0.5")


#To set the channel 2 as a trigger with a trigger voltage of 2V
my_instrument.write(":TRIGger:EDGE:SOURce CHANnel1")
my_instrument.write(":TRIGger:EDGe:LEVel 2.4")

#time based refernce position: Set to triger position
my_instrument.write(":TIMebase:HREF:MODE TPOSition")

#single triger mode
my_instrument.write(":SINGle")
my_instrument.write(":CHANnel1:DISPlay OFF")

#To save the CSV onto an external pendrive
my_instrument.write(":SAVE:CSV D:\\22_05\\SCPI\\Inner_Ring_Damage_X+Position.csv")   
my_instrument.write(":SAVE:IMAGe D:\\22_05\\SCPI\\Inner_Ring_X+Position.jpeg")



