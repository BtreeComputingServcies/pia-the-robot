#!/usr/bin/env python
# Author: Jim Gabriel
# License: Public Domain
#
# the purpose of this is just to test the commmunication is working between the PI and the Circuitplayground express.
# commands (i.e. object method names) can be sent to the circuitplayground over the serial port
import time 
import serial

myport = '/dev/ttyAMA0' 
ser = serial.Serial(
      port= myport,
      baudrate = 9600,
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS,
      timeout=1
      ) 

if ser.isOpen() :
  print ('started')
  counter=0
  while True:
     cmd_methodname  = "i_will_not_comply"
     #cmd_methodname = "giggle"
     #cmd_methodname = "flash_all_pixels"
     try:
       byteswritten = ser.write(cmd_methodname)  #send the command to the circuitplayground       
       print ("wrote %d bytes to serial port" % ( byteswritten) + '\n' )
       
       data = ser.readline()
       if data :  # the circuit playground sais something back
           print ("read successful %d"%(len(data)) + ' read this: ' + data + '\n')
     except Exception, e:
        print ("error writing to serial port" + str(e))
 
     time.sleep(1)
     counter += 1
