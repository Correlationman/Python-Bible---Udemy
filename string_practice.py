""""
Created on Tue Nov 15 12:04:47 2016
From Umedy course: The Python Bible™
Section 5: How to use Strings to handle text in Python
""""
#Slicer
x="sdweBIRTHDAYwsdmds"
print(x.count("d"))
print(x[0],x[-2])
#Slicer, just wants to get BIRTHDAY
print(x[x.index("B"):x.index("ws")])
print(x[x.index("B"):])
print(x[:x.index("ws")])

"""
#Input & string formatting
#Why input has to be in '' or "" to be considered as string?!
name=input('what is your name?: ')
age=input("How old are you?: ")
place=input("where do you live?: ")
like=input("What do you like to do?: ")
string="Your name is {} and you are {} years old. You live in {} and you love {}"
output=string.format(name,age,place,like)
print(output)
"""

#Email slicer
#Why input has to be in '' or "" to be considered as string?!
email=input("what is your email address?: ").strip() #onlystrips off whitespace around the string
email=email.replace(" ","") #strips off whitespaces elsewhere
string="Your email is: {}"
output=string.format(email)
print(output)
# or, alternatively:
print("Your email is {}".format(email))

username=email[:email.index("@")]
string="Your username is: {}"
output=string.format(username)
print(output)

domain=email[email.index("@")+1:]
string="Your doamin is: {}"
output=string.format(domain)
print(output)




        
    

           






