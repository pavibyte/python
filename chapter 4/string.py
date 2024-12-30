#string data type
first="Pavithra" #literal assignment that is literally assigning a value
last="darsini"   #string literal
print('')        #first line output is empty line

print(type(first))             #<class 'str'>
print(type(last)== str)        #True
print(type(last)== "str")      #false because the data type is under quotation
print(isinstance(first,str))   #True

#constuctor function
pizza="pepperoni"
print(type(pizza))
print(type(pizza)== str)
print(isinstance(pizza,str))

#concatenation
fullname= first+' '+last
print(fullname)              #pavithra darsini
fullname +='!'
print(fullname)              #pavithra darsini!

# casting a number to a string
decade=str(1980)
print(type(decade))          #<class 'str'>
statement="i love rock music from the " + decade+"s."
print(statement)             #i love rock music from the 1980s.

#escaping special charter
statement="I\'m pavithra.\tHey!\nWhere\'s this at \\located? "
print (statement)             #output:  I'm pavithra.	Hey!
                                        Where's this at \located? 
#string methods
print(first)                  #Pavithra
print(first.lower())          #pavithra
print(first.upper())          #PAVITHRA
print(first)                  #Pavithra
print(statement.title())      #I Love Rock Music From The 1980S. This method capitalises the first alphabet of each sentence.
print(statement.replace("rock","pop"))  #i love pop music from the 1980s.
print(statement)              #orginallly assigned value is the output.

print(len(statement))              #33
statement += "                 "
print(len(statement))              #50
print(statement.strip())           #removes the unnecessary space but the output is not printed
print(len(statement.strip()))      #33

# string indexing
first=cake
print(first[1])               #a
print(first[-2])              #k
print(first[1:-1])            #ak
print(first[1:])              #ake





