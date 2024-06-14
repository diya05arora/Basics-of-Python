'''
# Functions ->
# 1. Built-in Functions (Pre-defined functions)
# 2. User defined Functions
# 3. Lambda Functions (Anonymous functions)

# 1. BUILT IN FUNCTIONS 
# Eg: print(), input(), sort(), int(), float(), abs(), complex(), list(), max(), min(), pow(), bool(), len()

# 2. USER DEFINED FUNCTIONS
# def keyword -> to start the function definition
# followed by a function name
# then parentheses()
# then colon:

# def function_name(arguments):
#   statements
#   return statement

# always begin the name of the function with small letter, next words' first letter should be capital

# WITH PARAMETERS
# defining
def printOutput(str1):
    print("The parameter given to function:", str1)
    return # optional in this case

input1 = input("Enter user name: ")
# calling
printOutput(input1)

# input1 -> actual parameter, real value sent to the function
# str1 -> formal parameter as it is a formality of copying value of actual parameter to formal


# WITHOUT PARAMETERS
def print_output():
    input1=input("Enter your name: ")
    print(input1)

print_output()


def appendInList(list1):
    list1.append(1)
list=[1,2,3]
appendInList(list)
print(list)

# ALL PARAMETERS(ARGUMENTS) IN THE PYTHON LANGUAGE ARE PASSED BY REFERENCE
# This means that any change in function will be reflected in the actual argument.
# Memory addresses of both actual and formal reference are same.

def sumOfNumbers(num1, num2):
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "=", sum)
sumOfNumbers(3,5)

def sumOfNumbers(num1, num2):
    total = num1 + num2
    print("The sum of", num1, "and", num2, "=", total)
sumOfNumbers(3,5)
print("The sum is", total) #NameError, name 'total' is not defined


def sumOfNumbers(num1, num2):
    total = num1 + num2
    return total
sum = sumOfNumbers(3,5)
print("The sum is", sum)


# Default arguments: in case user fails to give necessary arguments, default parameters will be taken
# default arguments should always be added after the non-default arguments
def sumOfNumbers(num1, num2=10):
    total = num1 + num2
    return total
sum = sumOfNumbers(3)
print("The sum is", sum)

def sumOfNumbers(num1, num2=10):
    total = num1 + num2
    return total
sum = sumOfNumbers(3,6)
print("The sum is", sum)

# Keyword Arguments
# Dynamically passing any number of arguments **args
def func1(**args): # **args will by default act as a dictionary with key-value pairs
    for key, value in args.items():
        print("The key is:", key, "The value is:", value)
# call function with any number of arguments
func1(name="Ajay", age=20, salary=10000, degree=["BCA", "MCA", "MBA"])
'''

# Dynamically give many simple arguments not in form of key-value pairs
def function(*args): # *args is a tuple here
    total = 0
    for i in args:
        total += i
    print("The sum is", total)
function(1,3,9)
function(9)
function(8,9)
function(0,56,2,3,5)
function()
# any word can be used in place of args/arg like var