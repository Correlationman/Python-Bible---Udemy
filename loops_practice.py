"""
Created on Tue Nov 16 14:04:47 2016
From Umedy course: The Python Bible™
Section 8: Loops
"""
"""
#while and for loops
number =1
while number<=10:
    # print only odd numbers
    if number%2!=0:
        string="This number: {} is an odd number"
        output=string.format(number)
        print(output)        
        #print(number)
    else:
        print("Does not print even numbers!")
    number=number+1

    
L=[]
while len(L)<3:
    number=input("Tell a number: ")
    L.append(number)
print('Sorry list is full')
print(L)
print(L[0],len(L))

for number in range(1,10):
    print(number)
print("Another way:")    
for number in [1,3,5,6,8,9]:
    print(number)   
"""    
# List comprehensions
even_numbers=[x for x in range(1,10) if x%2==0]
print(even_numbers)
odd_numbers=[x for x in range(1,10) if x%2!=0]
print(odd_numbers)

words=["the","quick","brown","fox"]
# create another list (answer from our list (words)
answer=[[w.upper(),w.lower(),len(w)] for w in words]
print(answer)
   
