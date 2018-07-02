 
# Author: Jim Gabriel
# The purpose of this class provides serial communcion with the CircuitPlayground Express

import serial
class Pi_CPX:
    def __init__(self, myport = '/dev/ttyAMA0' ):
        self._ser = serial.Serial(
            port= myport,
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
            ) 
        self._active = self._ser.isOpen()
    
    #  this will send method calls to the circuitplayground to run
    #  example "i_will_not_comply"
    #          "
    def send (self, cmd_methodname = ''):        
        if self._active and (cmd_methodname != '') :
          byteswritten = self._ser.write(cmd_methodname)  #send the command to the circuitplayground
          print ("wrote %d bytes to serial port" % ( byteswritten) + '\n' )
      
    def receive (self):
        receiveddata = self._ser.readline()
        if receiveddata :  # the circuit playground sais something back
           print ("read successful %d"%(len(receiveddata)) + ' read this: ' + receiveddata + '\n')
           return receiveddata
    