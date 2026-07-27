from array import *

var = array('i' , [1 , 2 , 3 , 4 , 5 , 6])

a = var[2:-2]

for x in a:
    print(x , end = " ")

print("\n")
b = var[::-1]

for x in b:
    print(x , end = " ")