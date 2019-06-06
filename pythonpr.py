Name = 222;
print("Name")
print('Name')
print(Name)

#How to write outputs like "Bikash Likes BLue"?

nm = input('What is your name? ')
colr = input('Your Favourite Colour? ')
print(nm + ' Likes ' + colr)



#How To Make an "Age Calculator" using pythong?


yob = input( 'Year of Birth Please: ')
DOB = 2019 - int(yob);
print(DOB)
print(type(DOB)) #To find the type of a variable


#How to convert weight(lbs) into weight(kg)

wgt_pnd = input('Enter Weight(Pound): ')
wgt_kg = int(wgt_pnd)  * 0.45
print(wgt_kg)

#How to write output or string differently in Python

course = 'My name is "Bikash"' #if using double quote as a string we need to use single quote outside or vice versa
print(course)
Course = '''
Hey Bikash,

I am glad to tell you that this is just a sample text.

Thank you,
Companies.com'''

print(Course) #It prints everything same as exactly written<formatting same>


sample = "My Name is Bikash"
        # 01234567890123456
print(sample[0:5]) #All the letters from 0 to 5
print(sample[:5])  #All the ;etters from 0 to 5
print(sample[:])   #All the letters from 0 to end
print(sample[-1])  #If M = 0 then h the ending letter =-1
print(sample[-4])

#To copy a string into another variable

another = sample[:]
print(another)  #It will show the same thing which is in sample


sample = 'Bikash'
        # 012345
print(sample[1:-1]) #--->ikas
#How? 1=i index, h =-1 so starting from i excluding h

first = 'nampi'
last = 'tro'
msg = f'{first} {last} is a coder'   #'f' here used is common format and must be used
print(msg)

name = 'Bikash'
last_name = "Tiwari"
full_name = f'{name} {last_name} is your full name'
print(full_name)

#Methods in Python
course = 'Python For Beginners'

#To find length of the string
print(len(course))
print(course.upper()) #To Convert To uppere case
print(course)
#The upper() method makes a copy of the string course and the real one exists as it is

#Using 'Replace' & 'find' -->methods in python
course = "Python For Beginners"
print(course.find("F")) #If the letter is found --> return index of that
print(course.find("M")) # -1 is the letter is not found
print(course.find("Beginners"))#The first letters index is returned
print(course.replace('P', "F"))
#Are case sensitives; you cannot use 'beginners' instead of 'Beginners'

course = "Python For Beginners"
#To find a boolean value susing 'in' operator

print('Python' in course) #Output: True
print('python' in course) #Output: False

*/----------------#QUICK NOTE: 1.Find   2.Replace  3.len() 4.in  5. upper ---------------------------------------- 

len()
course.upper()
course.title()
course.find()
course.replace(,)
'...' in course
-----------------------------------------------------------------------------------------------------------------/*
course = "python for beginners"
print(course.title()) #Converts the first letter of each word into capital letter
#Output : Python For Beginners


#Mathematical operators in Python

print(10//3) #divison with rounded output that is integer
print(10/3) #division with float output as well
print(10**3) #10 to the power 3

#Adding modules/libraries to python code
import math
x=10
print(math.exp(x))

#testing if statement in python

is_hot = True


if is_hot:
    print("Yes! it's very hot outside today>..")
    print("Be safe, take a cream with you.")

print("No it's not included") #This doesnt includes in the if statement

is_hot =False  #Now, the boolean value is set to false

if is_hot:  #You wont see it now it is ignored
    print("Yes! it's very hot outside today>..")
    print("Be safe, take a cream with you.")

print("No it's not included") #You will just see this output
