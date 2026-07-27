from array import *

# Integers
var = array('i' , [1 , 2 , 3 , 4 , 5 , 6])

for i in range(0 , 6):
    print(var[i] , end  = " ")

print("\n")

# Double Float
var2 = array('d' , [1.1 , 2.2 , 3.3])

for x in var2:
    print(x , end = " ")

print("\n")

# Character
var3 = array('u' , ['a' , 'b' , 'c' , 'd'])

for x in var3:
    print(x , end = " ")

# Array Reverse
print("\n")

var.reverse()
for x in var:
    print(x , end = " ")
