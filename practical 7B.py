# Parent class
class Animal:
  # Properties
	multicellular = True
	# Eukaryotic means Cells with Nucleus
	eukaryotic = True
	
	# Function breath
	def breathe(self):
	    print("I breathe oxygen.")
    
  	# Function feed
	def feed(self):
	    print("I eat food.")
	    
# Child class	    
class Herbivorous(Animal):
    
    	# Function feed
	def feed(self):
	    print("I eat only plants. I am vegetarian.")

herbi = Herbivorous()
herbi.feed()
# Calling some other function
herbi.breathe()
