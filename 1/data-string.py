# multiplas variaveis
"""
myName = "Rodrigo"
myLastname = "Torres"
myAge = 35

# show organized information
print("My name is: " + myName + " " + myLastname + ", I have " + str(myAge) + " years old.")
"""

myName = input("What is your name? ")
myLastname = input("What is your last name? ")
myAge = input("What is your age? ")

# show organized information
print("My name is: " + myName + " " + myLastname + ", I have " + myAge + " years old.")

# format
print("My name is: {} {}, I have {} years old.".format(myName, myLastname, myAge))

