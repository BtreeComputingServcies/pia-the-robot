from pia_cpx   import Pia
from pia_timer import Timer 

pia   = Pia()
timer = Timer() #create a timer that keeps track of a elapsedTime
print ('running pia for the circuit playground express.. waiting for serial commands from raspberry pi')

pia.flash_all_pixels(None, 20)
while True:

    #pia.has_been_touched(padtouched = "any")
    if pia.has_been_touched(padtouched = pia._cpx.touch_A1) :
        print('you touched it baby')
                
    pia.get_command()    
    pia.run_commands()
        
    if timer.getElapsedTime() > 60 : #Check every 60 seconds to check the temperature 
        temperature = pia.temperature('F')
        timer.reset()
        if temperature:
            pia.set_command('it is ' + temperature)
    
     
 