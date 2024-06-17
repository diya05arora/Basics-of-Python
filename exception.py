# EXCEPTIONS IN PYTHON
# error before running- not an exception
# Runtime error - exception

# Syntax
'''
try:
    Lines of code that may raise an exception
except Exception1:
    if Exception1 occurs, execute this block of code
except Exception2:
    if Exception2 occurs, execute this block of code
else: #optional
    if no exception occurs, execute this block of code
finally: #optional
    executed always, regardless of try and except blocks
'''

# How to view all built in exceptions and functions
# print(dir(locals()['__builtins__']))
'''
try:
    print('Happy')
except:
    print("Excepting the error")
else:
    print("No exceptions occured")
finally:
    print("This will always be executed")
'''

# Arithmetic error -> division by zero
'''
try:
    num1 = int(input("Enter the dividend: "))
    num2 = int(input("Enter the divisor: "))
    print("Division:", num1/num2)
    index = int(input("Enter the index value of the list element for access: "))
    list = [1,2,3,4,5]
    print(list[index])
except ZeroDivisionError:
    print("Divisor can't be zero")
except IndexError:
    print("Index given is out of bounds!")
except: #for all the exceptions
    print("An exception occured! Please check inouts again")
else:
    print("No exceptions occured")
finally:
    name=input("Enter your name: ")
    print("Welcome to Python Programming", name)

# case1: When no exception occurs -> try..else..finally
# case2: When an exception occurs -> try till error occurs..except..finally
'''

# User-defined Exceptions
# Create a new user class which is derived from Exception class

# Create exception for retired senior citizen candidates
class InvalidAgeException(Exception):
    pass
age=int(input("Enter a relevant age for retired employee: "))
try:
    if(age<60):
        raise InvalidAgeException
    else:
        print("Valid age inserted!")
        print("The employee is eligible for pension scheme")
except InvalidAgeException:
    print("Exception occured!")

