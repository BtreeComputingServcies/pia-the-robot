# pia_servo for the PCA9685 PWM servo/LED controller library.
 
# Author: Jim Gabriel
# License: Public Domain
from __future__ import division
import time
import sys

import Adafruit_PCA9685

def map( degrees, in_min, in_max, out_min, out_max) :
  return int ((degrees - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

class Servo:    
    servo_min   = 150 # 150  # Min pulse length out of 4096
    servo_max   = 600 # 600  # Max pulse length out of 4096 
 
    maxposition = 70  #70  #degrees
    minpostion  = 140 #degress
    
    delay       = 0.1
    currentpos  = 0
    channel     = 1

    def __init__(self, _channel=0, _alias="", _zero=101, _step=1):
      self.channel      = _channel
      self.alias        = _alias
      self.sleepdelay   = 0.008  #sleep in between steps
      self.pausewhendone = 1     #after the final move, then pause this much
      self.deltadegrees = 0
      self.degrees      = _zero
      self.zero         = _zero
      self.currentpos   = _zero
      self.step         = _step
      self.pwm          = Adafruit_PCA9685.PCA9685()
      self.pwm.set_pwm_freq(60)
      
    def setPauseWhenDone( self, _pause ):
      self.pausewhendone = _pause               
                
    def setSpeedStep (self, _step):
      self.step = _step    
                
    def setSleepDelay (self, _sleepdelay):
      self.sleepdelay = _sleepdelay
      
    def setDegrees (self, _degrees):
      if _degrees [:1] in ['+', '-'] :
        #print ('1 going delta ' + `_degrees` + ' deltadegrees:' +  `self.deltadegrees` + '  degreees:' + `self.degrees` )
        self.deltadegrees = int (_degrees)
        self.degrees      += int(_degrees)
        #print ('2 going delta ' + `_degrees` + ' deltadegrees:' +  `self.deltadegrees` + '  degreees:' + `self.degrees` )
      else:
        self.deltadegrees = 0
        self.degrees = int(_degrees)
        #print ('going ' + `self.degrees`)
      
    def go (self):      
      direction = 1
      if self.currentpos > self.degrees :
        direction = -1 
      direction  = direction * self.step  
      print ('going from ' + `self.currentpos` + ' to ' + `self.degrees` + ' by ' + `direction` ) 
      for degree in range(self.currentpos, self.degrees, direction) : 
        #print ('***>' +`degree`)       
        self.pwm.set_pwm(self.channel, 0,  map(degree, 0, 180, self.servo_min, self.servo_max))
        time.sleep(self.sleepdelay)
      self.currentpos = self.degrees 
      #print (self.alias + ' now @ ' + `self.currentpos`) 
      time.sleep(self.pausewhendone)      
      
      
    def goMiniDelta(self):
      direction = 1
      if self.deltadegrees < 0 :
        direction = -1   
       
      direction = self.step * direction
      degree = self.currentpos + direction
     
      self.pwm.set_pwm(self.channel, 0,  map(degree, 0, 180, self.servo_min, self.servo_max))
      time.sleep(self.sleepdelay)
      self.currentpos = degree
      
        
    def goDelta (self):
      direction = 1
      if self.deltadegrees < 0 :
        direction = -1   
       
      direction = self.step * direction
      
      #print ('currentpos: ' +  `self.currentpos`  + '  moving to: ' + `self.currentpos + self.deltadegrees` + ' direction = ' + `direction` )
      for degree in range(self.currentpos, self.currentpos + self.deltadegrees, direction) :         
        self.pwm.set_pwm(self.channel, 0,  map(degree, 0, 180, self.servo_min, self.servo_max))
        time.sleep(self.sleepdelay)    
        
      self.currentpos = self.currentpos + self.deltadegrees  
      #print (self.alias + ' now @ ' + `self.currentpos`)  
      print ('')
    
    def reset(self):
        print ("resetting " + self.alias + ' to zero ' + `self.servo_min` +  ' ' + `self.servo_max`)
        #zero = map(self.zero, 0, 180, self.servo_min, self.servo_max)
        #self.setDegrees (`zero`)
        #self.setSpeedStep(1)
        #self.setSleepDelay(0.01)
        #self.go()
        
        self.pwm.set_pwm(self.channel, 0,  map(self.zero, 0, 180, self.servo_min, self.servo_max))  


