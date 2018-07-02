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

from __future__ import division
from pia_servo  import Servo
from pia_pi_cpx import Pi_CPX
import time
import sys
 

def moveServos (servolist):  
    print ('running ' + `len(servolist)`)
    for loop in range(10) : 
      for servo in servolist:
        print (servo.alias)
        if (loop < 30) or (servo.channel==2):
          servo.goMiniDelta()
      time.sleep(0.05)
    return  

print('Moving servo on channel 0, press Ctrl-C to quit...')
pia_cpx = Pi_CPX () # create the object for communicating with the circuit playground express


xServo= Servo(0,'xServo', _zero = 101)        
yServo= Servo(1,'yServo', _zero = 101)
zServo= Servo(2,'zServo', _zero = 90)

#xServo.reset()
#yServo.reset()
xServo.setPauseWhenDone(2)
xServo.setSpeedStep(1)
xServo.setSleepDelay(0.01)
xServo.reset()

yServo.setPauseWhenDone(2)
yServo.setSpeedStep(1)
yServo.setSleepDelay(0.01)
yServo.reset()

zServo.setPauseWhenDone(2)
zServo.setSpeedStep(1)
zServo.setSleepDelay(0.01)
zServo.reset()



print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
  xServo.setDegrees('+10')
  xServo.go()
  
  pia_cpx.send('i_will_not_comply')

   
  yServo.setDegrees('+20')
  yServo.go()
  
  xServo.setDegrees('-10')
  xServo.go()

  zServo.setDegrees('+15')
  zServo.go()
  pia_cpx.send('flash_all_pixels')
  
  yServo.setDegrees('-20')
  yServo.go()

  zServo.setDegrees('+30')
  zServo.go()
  
  pia_cpx.send('flash_all_pixels')
  zServo.setDegrees('-90')
  zServo.go()

  zServo.setDegrees('+45')
  zServo.go()
  
  cpx_message = pia_cpx.receive()
  if cpx_message:
    print (cpx_message)
   


