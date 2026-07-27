from array import *

arr = array('i' , [])

n = int(input('Enter A Number : '))

for i in range(0 , n):
    arr.append(int(input("Enter The Next Number :")))

for x in arr:
    print(x  , end = " ")