# Lambda -> anonymous funcytion
# SYNTAX: 
# defining
# variable = lambda argument(s): statement(s)
# calling
# variable() 

# Without arguments
'''
message = lambda: print("Hello user")
message()
'''

# With arguments
'''
msg = lambda username, num: print(f"Hello {username}. You have {num} coins")
msg("Diya", 18)
'''

'''
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Syntax for filter method -> filter(any function to be used as filter ex. lambda, iterable)
odd_list = list(filter(lambda num : (num%2!=0), list1))
print(odd_list)
'''

'''
result = lambda num1, num2: num1 if (num1>num2) else num2
num1 = int(input("ENter num1: "))
num2 = int(input("Enter num2: "))
print("The maximum number is", result(num1, num2))
'''

# Check for age>=60 in alist amd filter out thpse employees in a separate list
'''
age_list = [23,56,67,68,34,89,78,44,90,79,66,69]
senior_age_list = list(filter(lambda age: (age>=60), age_list))
print(senior_age_list)
'''

# map() -> helps to apply a lambda function's calculation mapped to each element of iterable
# map(lambda..., iterable)
'''
list_salary = [1000, 2400, 4500, 1100, 1000, 7800, 3600]
print("The original salary list is", list_salary)
# Add bonus of 500 Rs to all salaries and create a bonus list 

bonus_list = list(map(lambda sal: sal+500, list_salary))
print("After adding bonus, the salary list is", bonus_list)
'''

# Convert every employee name to upper case
list_emp = ["Ajay", "reema", "riTu", "Sima", "RamaNN"]
proc_list_emp = list(map(lambda emp: emp.upper(), list_emp))
print("Processed list:", proc_list_emp)