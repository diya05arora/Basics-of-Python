'''
import keyword
print(keyword.kwlist)
print("Number of keywords:", len(keyword.kwlist))
#automatic completing of statements or giving suggestions is known as INTELLISENSE (code-completion aid)
print(keyword.iskeyword("del"))

#Taking inout from the user
num = input("Enter a number: ")
print(num)
print(type(num)) #every type in python is an object of a class
#By default input() function will only accept string values

#Type casting -> changing a data type into another data type
#methods -> int(), str(), float(), ...
num1 = int(input("Enter a number: "))
print(num1)
print(type(num1))

# Standard Output
# Actual Syntax: print(*objects, sep='', end='\n', file=sys.stdout, flush=True/False)
print(7, 8, 9, 10, sep="*", end="$$")

#Creating file object (samplefile)
#For URL, use forward slashes instead of backward slashes.
#Two modes to open a file : 'r' for reading and 'w' for writing into the file
samplefile = open('C:/Users/diya0/Machine Learning/Basics of Python/text file.txt', 'w')
samplefile.write("I am happy")
#Another method
print("\n",7,8,9,10, sep = "^", end = "&&", file=samplefile)

#COMMENTS
#Single line -> #
#Multiple lines -> '''
'''Hi'''
'''
#OUTPUT FORMATTING USING format() FUNCTION
message = input("Enter message: ")
print("{}, Hello! Welcome to Python lecture".format(message))

#STRINGS
str1 = "Hello "
str2 = "Welcome"
num = 10
str3 = str1 + str2 #concatenation
print(str3)
# str = str1 + num #error
#Solution: change the type og either variable
num = str(num)
str = str1 + num
print(str)

i=1
j=2
k=i+j #addition
print(k)

num1 = 10
print("The num is:", num1, "The type is:", type(num1))

num2 = 10.13
print("The num is:", num2, "The type is:", type(num2))

num3 = 10+5j
print("The num3 is:", num3, "The type is:", type(num3))

#Number System
#Integer base 10 (default)
#Binary base 2, for using binary numbers, use prefix 0b or 0B
print(0b101)
print(0B101)
#Octal base 8, for using octal number, use prefix 0o or 0O
print(0o123)
print(0O123)
#Hexadecimal base 16, for using hexadecimal number, use prefix 0x or 0X
print(0x8A)
print(0X8A)

#Type casting in numbers is implicit or automatic
#At times we may need to force typecasting so it will be explicit

#Implicit-> smaller data will be converted into bigger data
print(100+15.67)

#Explicit-> convert a bigger data into a smaller data
print(int(19.87))
print(int(-19.87))
val = complex("10+3j")
print(val)

#Number based modules
# random and math modules
# random module -> generate numbers randomly on the fly
import random
print(random.random()) # 0<=x<1
print(random.randrange(20, 50)) #randrange(start, stop, step) end is stop-1
print(random.randint(2,3)) #both included
list = [1,4,2,0]
print(random.choice(list))
random.shuffle(list)
print(list)

# math module
# mathematical calculations
#Aliases - nicknames
import math as mt

print(mt.sqrt(4))
print(mt.pow(2,3))
print(mt.factorial(5))
print(mt.ceil(3.5))
print(mt.floor(3.5))
print(mt.ceil(-3.5))
print(mt.floor(-3.5))
print(mt.log10(1000000))
print(mt.pi)

#Sequence data
#List, String, Tuple

#LIST
#very flexible sequence of data as it allows all sorts of modifications
#Mutable data type
#data in list can be pf different data types
#data starts from index position 0
#Charactersitics of lists-> ordered by position(both positive and negative(backwards) indexing)
#mutable, repeated or duplicate elements are allowed
list1 = [1, 2, 3, "Hello", "Hi", 12.77, True, False, 1, 'a']
print(list1)
#Accessing elements of list
print(list1[0])
print(list1[-1])
print(list1[8-len(list1)]) #neg index = pos index - length of list
for i in range (len(list1)):
    print(list1[i], end=" ")
list1[-1]="abc"
print(list1)


#TUPLES
#sequence of data having order or postions of elements
#immutable i.e. we can not change them
#() -> use these parentheses
#index starts with 0 left to right and from -1 to -n from right to left
tup=(1,2,3,"Hello","Bye",True, False)
print(tup)
print(tup[0])
print(tup[-1])
tup[1]=100 #TYPEERROR! 'tuple' object does not support item assignment

#Collections type data that do not have any index or position
#Dictionary
#Set

#Dictionary 
#Curly braces {}
#key:value pairs
#Each value is recognized by key
#Keys are immutable but values are mutable
#unordered
dict1 = {"Name":"Ajay", "Age":20, "Salary":10500}
print(dict1)
print(dict1["Age"])
dict1["Age"]=25
dict1["degree"]="M.Tech"
#dict = {[1,2,3]:1} #TypeError: unhashable type: 'list', keys cannot be of mutable data type
#values can be of any type
print(dict1.keys())
print(dict1.items()) #list of tuples of key value pairs
print(dict1.values())
'''

#SET
#used with {}
#no duplicate elements are allowed
#unordered
set = {1,2,7,3,1,5, "hi"}
print(set)
set.add(5)
print("heLLo".lower())
execute = 1
