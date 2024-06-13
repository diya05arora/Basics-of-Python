# STRINGS
#Strings are immutable

# #Single line strings
# str1 = "Hello Python" #single quotes are also allowed
# #Multi line strings
# #no new line is added, its only the way code is written
# str = "Hello " \
# "all welcome " \
# "to my " \
# "lecture"
# #new line is added when we are giving different lines
# str2 = '''Hello all
# Welcome to my lecture'''
# print(str1)
# print(str)
# print(str2)

'''
# Slicing str[start, stop, step]
# end is stop-1
str = "My name is Diya"
print(str[::-1]) #reverse a string
print(str[3:5])
print(len(str[-1]))
print(str[1:5])
print(str[-14:-10]) #neg index = pos ind - length of string
print(str[-14:-10:2])
print(str[-10:-14:-2])
print(str[-7::-2])

# Comparison between strings
str1 = "hello"
str2 = "Hello"
print(str1==str2)
print(str1>str2)

#ord() -> gives ascii code for character
#chr() -> gives character at given ascii code
print(ord('h'))
print(ord('H'))
print(chr(65))
print(chr(97))

# String repetition
# * operator
str1 = "Hello "
str2 = "Diya"
print(str1*5)
print(5*str1)

# concatenation (+) operator
print(str1 + str2)

# findlength or number of characters in a string
print("the length of str1 is", len(str1)) 

# Membership test
# To check whether a character or substring is present in the substring or not
str1 = "Hello dear friends, welcome to my class.."
print("dear" in str1)
print("...." in str1)
print("...." not in str1)

#String Methods
#returns index of first character if the substring is present in string else returns -1
print(str1.find("dear"))
print(str1.find("."))
print(str1.find("...."))

#returns index of first character if the substring is present in string else gives an error
print(str1.index("dear"))
#print(str1.index("....")) #ValueError substring not found
print(str1.index("."))

print(str1.upper())
print(str1) #no change as strings are immutable
print(str1.lower())

print(str1.replace("dear", "all"))
print(str1.replace(" ", "*")) #replaces at every " "
print(str1.replace(" ", "*", 1)) #only first " " is replaced
'''
# to slice or split or cut the string (default sep is " ")
str1 = "Hello dear    friends, welcome to my class.."
list = str1.split()
print(list)
list2 = str1.split("d")
print(list2)
list3 = str1.split("    ",2)
print(list3)

# strip() -> removes leading and trailing spaces from text string 
str2 = "             Hello            all stuents           "
print(str2.strip())
print(str2.lstrip()) #leading spaces will be removed
print(str2.rstrip()) #trailing spaces will be removed
str3 = "hello dear"
print(str3.strip("he"))
print(str3.title())