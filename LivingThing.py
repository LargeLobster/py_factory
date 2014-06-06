##Abstract class representing all of the
# Animals and plants in the world

from abc import ABCMeta, abstractmethod

class LivingThing():
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self._age = 0
    
    ##Get Age method
    #@return gives the current age of the living thing
    def get_age(self):
        return self._age
    
    ##Increment age method
    #Increases the age of the living thing by one
    def increment_age(self):
        self._age = self._age + 1
    
    