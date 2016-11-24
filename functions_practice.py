"""
Created on Tue Nov 16 14:04:47 2016
From Umedy course: The Python Bible™
Section 9: Functions
"""

#Functions
def rev(text):
    return text[::-1]

a=rev('Ramin Resch').lower()    
print(a)
a=rev('Ramin Resch').upper()    
print(a)
a=rev('Ramin Resch').capitalize()   
print(a)
a=rev('Ramin Resch').title()   
print(a)
b=rev([1,2,3,4])
print(b)

# Variable Scope: Global or Local
a=100
def f1():
    print(a) # Global scope
    
def f2():
    a=50 # local scope
    print(a)
f1()
f2()
print(a) # Still uses Global scope
print("\n")

# Overwrite a global variable inside a function by keyword global    
a=100
print(a)
def f1():
    global a
    a=200    
    print(a) # Global scope
    
def f2():
    a=50 # local scope
    print(a)
f1()
f2()
print(a) # New value of Global a
print("\n")
    
# List elements are exception!
a=[80,90,100]
print(a)
def f1():
    global a
    a[0]=200    
    print(a) # Global scope
    
def f2():
    a[0]=50 # local scope
    print(a)
f1()
f2()
print(a) # New value of Global a based on change in f2()
print("\n")   

# Function Parameters and Arguments
def about(name,age,likes): #parametes are name, age, and likes
    sentence="Meet {}! They are {} years old and they like {}".format(name,age,likes)
    return sentence

text=about("Jack",23,"Python") #Position arguments are Jack, 23 and Python
print(text)
# OR, alternatively:
text=about(age=23,likes="Python",name="Jack") #Keyword arguments are age=23, etc
print(text)    
#Parameters with default values    
def about(name="Jack",age=29,likes="Python"): #parametes are name, age, and likes
    sentence="Meet{}! They are {} years old and they like {}".format(name,age,likes)
    return sentence    
text=about("Ramin",32,"Tennis") 
print(text)    

text=about(likes="Tennis",name="Ramin",age=32) 
print(text)        

#Packing and Unpacking variables
numbers=[1,2,3,4,5]
print(numbers)
# Unpack the list with *, DID not work!
#print(*numbers)
  
board=["" for i in range(9)]
print(board)  