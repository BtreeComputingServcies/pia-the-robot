
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
    
     
 