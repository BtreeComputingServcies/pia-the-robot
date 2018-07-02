import time

# Author: Jim Gabriel
"""
Timer class will keep track of elasped time.   
  * Use the getElapedTime() method to retreive the number of seconds that have elasped since it was started
  * Use the reset() to reset the elapsed time

"""
class Timer():
    
    def __init__ (self):
      self.start = time.monotonic() 
    
    def getElapsedTime (self) :
      self.stop = time.monotonic()    
      return self.stop - self.start
      
    def reset (self) :
        self.start = time.monotonic() 