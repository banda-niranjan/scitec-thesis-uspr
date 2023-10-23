import pyvisa

#https://www.righto.com/2013/07/rigol-oscilloscope-hacks-with-python.html
#https://www.tek.com/en/documents/technical-brief/getting-started-with-oscilloscope-automation-and-python


instrument= pyvisa.ResourceManager().open_resource("TCPIP::192.168.1.141::INSTR")
instrument.query(":MEASure:FREQuency:SMAXimum")



