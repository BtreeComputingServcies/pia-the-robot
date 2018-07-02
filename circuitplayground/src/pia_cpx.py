import time
import random 
import board
import digitalio
import busio

from adafruit_circuitplayground.express import cpx

# Author: Jim Gabriel

# https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/blob/master/adafruit_circuitplayground/express.py

# Configuration:
audiofiles = ["sounds/laugh.wav",
              "sounds/comply_not.wav",
              "sounds/t2_learning_computer_x.wav",
              
              "sounds/bd_zome.wav",
              "sounds/bd_tek.wav",
              "sounds/drum_cowbell.wav",
              "sounds/elec_blip2.wav",
              "sounds/elec_cymbal.wav",
              "sounds/elec_hi_snare.wav",
              "sounds/t2_terminator.wav",
              "sounds/none_shall_pass.wav",
              "sounds/hello.wav",
              "sounds/heh_heh_heh.wav",
              "sounds/for_no_man.wav",
              "sounds/bring_out_your_dead.wav",
              "sounds/yee_hah.wav",
              
              "sounds/learned_lesson.wav",
              "sounds/pee.wav",
              "sounds/goodfellas_gangster.wav"                                 
              ]
                      
class Pia ():
    def __init__(self, decay=0.5):
        self._cpx  = cpx  
        self._uart = busio.UART(board.TX, board.RX, baudrate=9600)
        self._commands = []
        
    def getRandomColor (self):
        return (random.randint(0,16), random.randint(0,16), random.randint(0,16))   
              
    def play_file(self, filename):
        #print("playing file " + filename)      
        self._cpx.play_file(filename)      
    
    def giggle(self) :
        self.play_file( audiofiles[0])
    
    def run_commands(self):
        while len(self._commands) > 0 :
            cmd = self._commands.pop(0)            
            try:
                pia_command = getattr(self, cmd)
                pia_command()
                print('running cmd:' + str(cmd))                 
            except:    
                print ('unknown command')            
        return  
            
    def set_command(self, cmd_string = None) : 
        btyeswritten = 0        
        if cmd_string is not None:
            btyeswritten = self._uart.write(cmd_string + '\n')  
            #print ('bytes written %d'%btyeswritten)
     
    def get_command(self) :
       cmd = self._uart.readline()  # read up to 32 byte            
       if cmd is not None:            
          cmd_string = ''.join([chr(b) for b in cmd])
          self._commands.append(cmd_string) # lets add the command to the queue in perparation to be run
                 
    def i_will_not_comply(self) :
       self.play_file( audiofiles[1])    
    
    def has_been_shaken (self):         
        if self._cpx.shake(shake_threshold=10): 
            #print ("I've been shaken!") 
            self.flash_all_pixels()   
            try:
                idx = random.randint(0,len(audiofiles)-1)   
                self.play_file( audiofiles[idx])   
            except:
                pass
                #print ('opps: ' + audiofiles[idx])
   
    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if (pos < 0) or (pos > 255):
            return (0, 0, 0)
        if pos < 85:
            return (int(pos * 3), int(255 - (pos*3)), 0)
        elif pos < 170:
            pos -= 85
            return (int(255 - pos*3), 0, int(pos*3))
        #else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))   
          
    def rainbow_cycle(self, wait):
        self._cpx.pixels.auto_write = False
        self._cpx.pixels.brightness = 0.3
        for j in range(255):
            for led in range(self._cpx.pixels.n):
                idx = int((led * 256 / len(self._cpx.pixels)) + j)
                self._cpx.pixels[led] = self.wheel(idx & 255)
            self._cpx.pixels.show()
            time.sleep(wait)
                   
    def flash_all_pixels (self, definedColor = None, loopcount=6):    
        #self.rainbow_cycle(0.001) 
        self._cpx.pixels.brightness = 1      
        for loop in range (loopcount):
            for led in range(10):
                if definedColor == None:  
                    self._cpx.pixels[led] = self.getRandomColor()               
                else:
                    self._cpx.pixels[led] = definedColor                 
             
                #self.rainbow_cycle(0.001) 
                time.sleep(0.02)        
                self._cpx.pixels[led] = 0x000000 #turn the pixel off
                        
    def has_been_touched(self, padtouched = "any"):
        rtn = False          
        if ((padtouched == "any") and
            ((self._cpx.touch_A1) or
            (self._cpx.touch_A2) or
            (self._cpx.touch_A3) or
            (self._cpx.touch_A4) or
            (self._cpx.touch_A5) or
            (self._cpx.touch_A6) or
            (self._cpx.touch_A7)      
            )) or ((padtouched != "any") and padtouched) :
          self.giggle()    
          rtn = True
        return rtn   
        
        
    def temperature(self, _degrees_in = 'f'):
        temperature_c = self._cpx.temperature
        rtn = str(temperature_c) + ' degrees C' 
        if _degrees_in in ['f', 'F'] :                
            temperature_f = temperature_c * 1.8 + 32
            print("Temperature fahrenheit:", temperature_f)
            rtn = str(temperature_f) + ' degrees F' 
            if temperature_f > 86 :
                self.flash_all_pixels ( definedColor = (16, 0, 0), loopcount = 1 ) #red hot
            else:
                if temperature_f < 60 :  
                    self.flash_all_pixels ( definedColor = (0, 0, 16), loopcount = 1 ) #blue
                else:  
                    print("Temperature celsius:", temperature_c)
            if temperature_c > 30 :
                self.flash_all_pixels ( definedColor= (16, 0, 0) , loopcount = 1) #red hot
            return rtn
        