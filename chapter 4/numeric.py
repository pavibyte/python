#INTEGER DATA TYPE
myvalue=29
x=int(False)
print(type(x))                   #<class 'int'>
print(isinstance(myvalue,int))   #True

#BOOLEAN DATA TYPE
myvalue=29.980
print(type(myvalue))            #<class 'float'>

#COMPLEX DATA TYPE
myvalue=29 +5j
print(type(myvalue))           #<class 'complex'>

#BUILT IN FUNCTIONS FOR NUMBERS
gpa=9.28
print(abs(gpa))               #9.28
print(abs(gpa * -1))          #9.28
print(round(gpa))             #9
print(round(gpa,1))           #9.3

import math
print(math.pi)                #3.141592653589793
print(math.sqrt(25))          #5.0
print(math.ceil(gpa))         #10
print(math.floor(gpa))        #9

