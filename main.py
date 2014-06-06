#Very simple factory using refection
#Writen under python 2.2.6

from LivingThingFactory import LivingThingFactory

print "Plant"
factory = LivingThingFactory()
plant = factory.create_life("Plant")

print "Animal"
factory = LivingThingFactory()
animal = factory.create_life("Animal")
