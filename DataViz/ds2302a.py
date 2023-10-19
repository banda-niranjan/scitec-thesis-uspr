import pyvisa

instrument= pyvisa.ResourceManager().open_resource("TCPIP::192.168.1.141::INSTR")
instrument.query(":MEASure:FREQuency:SMAXimum")



