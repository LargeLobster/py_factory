## Class Living Thing Factory
# Uses reflection to create instances of living things
# Requires that classes have the same name as the import they 
# come from

class LivingThingFactory():
    def __init__(self):
        pass
    
    ##Create life method
    #@param name    name of the class to create.
    #@param return  instance of the class created
    def create_life(self, name):
        mod = __import__(name)
        cls = getattr(mod, name)
        return cls()