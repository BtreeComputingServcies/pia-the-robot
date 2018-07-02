#!/usr/bin/env python
"""
 * This file is part of the Pia-the-robot project, 
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2018 Jim Gabriel
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
"""
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
