#   RECURSION IN FUNCTIONS
# re-currence of calling self by the function
# Calling self repetively by a function is known as recursion

# Syntax
'''
def func1(arg1, arg2):
  statements
  func1(v1, v2) # will self call itself
'''

# Factorial calculation for a number without Recursion
# 5! = 5 x 4 x 3 x 2 x 1 or 1 x 2 x 3 x 4 x 5
'''
n = int(input("Enter a number to calculate its factorial: "))
fact = 1
if(n==0 or n==1):
    print("The factorial of", n, "is", 1)
elif n>1:
    for i in range (1,n+1):
        fact = fact*i
    print("The factorial of", n, "is", fact)
else:
    print("Enter valid number")
'''

# Using recursion

# Recursive function  
'''  
def calc_factorial(num):
    if(num==1 or num==0):
        return 1
    elif(num<0):
        print("Cannot calculate factorial of negative numbers!")
    else:
        return (num * calc_factorial(num-1))

num = int(input("Enter a number: "))
fact=calc_factorial(num)
print(f"The factorial of {num} is", fact)
'''
# None : None is a special value which is returned when nothing can be calculated and returned by the function 

# Use recursion to calculate sum of n numbers
def calc_sum(num):
    if(num==0):
        return 0
    return num + calc_sum(num-1)
num=int(input("Enter the limit of sum calculation: "))
if(num<=0):
    print("Cannot calculate sum of 0 or negative limit!")
else:
    print(f"The sum of first {num} numbers = {calc_sum(num)}")