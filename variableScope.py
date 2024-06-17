# Variable Scope is the region/area where that variable can be accessed and used
# Lifetime of Variable is the number of lines of code till that variable is used

# Acoording to scope, we have three kinds of variables:
# 1. Local Variable
# 2. Global Variable
# 3. Non-local Variable

# LOCAL SCOPE OF VARIABLES
'''
def func1():
    result = "FInal Message inside function!" # local variable
    print("The result is", result)
func1()
print("The result is", result) # not accessible outside the function
'''

# GLOBAL SCOPE OF VARIABLES
'''
def func2():
    print("calling result inside function:", result)
result = "Message outside any function scope" # global variable
func2()
print("calling result outside function:", result)
'''

'''
result = "Message outside any function scope" # global variable
def func2():
    result = "Local result" 
    print("calling result inside function:", result) #local variable will override global variable
    # lifetime of local result = 2 lines(28-29)
func2()
print("calling result outside function:", result)
# lifetime of global result = 7 lines(27-33)
'''

# NON-LOCAL VARIABLES
# Non-local variables are used in context of nested functions such that these variables cannot be assumed to be in simple local pr global scope
# neither local or global variable
'''
def func_outer():
    result = "Inside func_outside()"
    # create a nested function
    def func_inner():
        print("The result inside func_inner():", result)
    func_inner()
func_outer()
'''


def func_outer():
    result = "Inside func_outer()"
    print("The result inside func_outer():", result)
    # create a nested function
    def func_inner():
        nonlocal result # changes in result will be reflected in the original result 
        result="Inside func_inner()" # not a  local variable
        print("The result inside func_inner():", result)
    func_inner()
    print("The result inside func_outer():", result)
func_outer()


