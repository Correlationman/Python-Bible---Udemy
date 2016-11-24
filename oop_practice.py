"""
Created on Tue Nov 16 14:04:47 2016
From Umedy course: The Python Bible™
Section 10: OOP
"""

# These libraries are not needed here, just to test if they load
import pandas
import numpy
import matplotlib
import IPython
import sklearn
import seaborn

# Classes are like templates
# We instantiate a class to make an object, object is an instance of a class
# Objects have States (proprties) and Methods (behaviours)

# Create a class
class Pound:
    value=1.00
    colour="gold"
    diameter=22.5 #mm
    thickness=3.15 #mm
    heads=True
# Create an object coin1 as an instance of the class Pound
coin1=Pound()
print(type(Pound))
print(type(coin1))
print(coin1.value)
print(coin1.colour)
coin1.colour="greenish"
print(coin1.colour)
# Another instance of the Pound class
coin2=Pound()
print(coin2.colour)

import random
#Encapsulation
#Class Methods, Constructors and Destructors
#Wrapping up data member and method together into a single unit (i.e. Class)
#is called Encapsulation. Encapsulation means hiding the internal details of 
#an object,i.e. how an object does something.
class Pound:
    #init method (constructor)   
    def __init__(self,rare=False):
        
        self.rare=rare
        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
              
        self.colour="gold"
        self.num_edges=1
        self.diameter=22.5 #mm
        self.thickness=3.15 #mm
        self.mass=9.5
        self.heads=True
    #rust method    
    def rust(self):
        self.colour="greenish"
    #clean method    
    def clean(self):
        self.colour="gold"
    #flip method    
    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads=choice
    
    #del method (destructor)      
    def __del__(self):
        print("Coin Spent!")

coin1=Pound(rare=True)
coin2=Pound()
print(coin1.value,coin2.value)
print(coin1.colour,coin2.colour)
coin1.rust() #rust coin1 by method rust()
print(coin1.colour,coin2.colour)
coin1.clean() #clean coin1 by method clean()
print(coin1.colour,coin2.colour)
print(coin1.heads,coin2.heads)
coin1.flip();coin2.flip() #clean coin1 & coin2 by method flip()
print(coin1.heads,coin2.heads)
del coin1;del coin2 #destruct coin1 & coin2 by method del()

#Inheritance
#Abstract class Coin
class Coin:
    #init method (constructor)
    #Pack down all the information from child class Pound (see below) into
    #keyword arguments dictionary called kwargs
    def __init__(self,rare=False,clean=True,heads=True,**kwargs):
        
        for key,value in kwargs.items():
            setattr(self,key,value)
            #for example, it passes all the vlaues as follows:     
            #self.original_vlaue=1.00
            #self.thickness=3.15
            
        self.is_rare=rare
        self.is_clean=clean
        self.heads=True
        
        if self.is_rare:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value
       
        if self.is_clean:
            self.colour=self.clean_colour
        else:
            self.colour=self.rusty_colour
            
    #rust method    
    def rust(self):
        self.colour=self.rusty_colour
        
    #clean method    
    def clean(self):
        self.colour=self.clean_colour
        
    #flip method    
    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads=choice
        
    #del method (destructor)      
    def __del__(self):
        print("Coin Spent!")
        
    #Special method __str__ which sets what comes out when we print the object,
    #instead of hexadecimal memory address
    
    def __str__(self):
        if self.original_value>=1:
            return "{} Pound Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value*100))
         
#Pound class inherits from Coin class, it inherits all the methods from Coin
#This is callled Inheritance.         
class One_Pound(Coin):
    #some vlaues are specific to each type of coin, put them in a dictionary:
    def __init__(self):
        data={
          "original_value":1.00,
          "clean_colour":"gold",
          "rusty_colour":"greenish",
          "num_edges":1,
          "diameter":22.5, #mm
          "thickness":3.15, #mm
          "mass":9.5
          }
        # Access everything else from parent class by using super() keyword
        # Unpack the data from the dictionary by using **data
        super().__init__(**data)  # works in Python 3.x, not in 2.7  
        #super(Pound,self).__init__(**data)    
# Run the code:
one_pound_coin=One_Pound()
print(one_pound_coin.diameter)
print(one_pound_coin.colour)
one_pound_coin.rust()
print(one_pound_coin.colour)
one_pound_coin.flip()
print(one_pound_coin.heads)
one_pound_coin.flip()
print(one_pound_coin.heads)

#Polymorphism
#Make rest of the coins by using Polymorphism (multiple forms for a method) 
#See method rust(), the five-pence coin is silver and does not rus like others 
#
class One_Pence(Coin):
    #some vlaues are specific to each type of coin, put them in a dictionary:
    def __init__(self):
        data={
          "original_value":0.01,
          "clean_colour":"bronze",
          "rusty_colour":"brownish",
          "num_edges":1,
          "diameter":20.3, #mm
          "thickness":1.52, #mm
          "mass":3.56
          }
        # Access everything else from parent class by using super() keyword
        # Unpack the data from the dictionary by using **data
        super().__init__(**data)  

class Two_Pence(Coin):
    #some vlaues are specific to each type of coin, put them in a dictionary:
    def __init__(self):
        data={
          "original_value":0.02,
          "clean_colour":"bronze",
          "rusty_colour":"brownish",
          "num_edges":1,
          "diameter":25.9, #mm
          "thickness":1.85, #mm
          "mass":7.12
          }
        # Access everything else from parent class by using super() keyword
        # Unpack the data from the dictionary by using **data
        super().__init__(**data)  

class Five_Pence(Coin):
    #some vlaues are specific to each type of coin, put them in a dictionary:
    def __init__(self):
        data={
          "original_value":0.05,
          "clean_colour":"silver",
          "rusty_colour": None,  # does not rust, use
          "num_edges":1,
          "diameter":18.0, #mm
          "thickness":1.77, #mm
          "mass":3.25
          }
        # Access everything else from parent class by using super() keyword
        # Unpack the data from the dictionary by using **data
        super().__init__(**data)  
        
        #new version of the rust method for five-pence coin, this is Polymorphism (multiple form of a method)    
        def rust(self):
            self.colour=self.clean_colour
            
class Ten_Pence(Coin):
    #some vlaues are specific to each type of coin, put them in a dictionary:
    def __init__(self):
        data={
          "original_value":0.10,
          "clean_colour":"silver",
          "rusty_colour": None,  # does not rust, use
          "num_edges":1,
          "diameter":24.5, #mm
          "thickness":1.85, #mm
          "mass":6.50
          }
        # Access everything else from parent class by using super() keyword
        # Unpack the data from the dictionary by using **data
        super().__init__(**data)
        #new version of the rust method for ten-pence coin, this is Polymorphism (multiple form of a method)    
        def rust(self):
            self.colour=self.clean_colour

coins=[One_Pence(),Two_Pence(),Five_Pence(),Ten_Pence(),One_Pound()]
for coin in coins:
   arguments=[coin,coin.colour,coin.value,coin.diameter]
   string="{} - Colour: {},value: {},Diameter(mm): {}".format(*arguments)
   # see speacil method __str__ in class Coin() for showing the name of the object        
   print(string)     
