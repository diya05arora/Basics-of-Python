'''
# SET
# set begins with {}
# set does not allow duplicates
# mutable
# unordered
set1 = {1,2,3,4,5,3,4,4, "abc", True, 8.9}
print(set1)
set2 = {} # dictionary
print(type(set2))

# set2.add(1) # AttributeError, since it is a dictionary
set1.add(55) # addition is not always at end
print(set1)

# update()
list1 = [1,43, 56, 89]
set1.update(list1)
print(set1)
tup1 = (90, 89, 56)
set1.update(tup1)
print(set1)
set2 = {4,5,8}
set1.update(set2)
print(set1)

# remove() 
set1.remove(3)
print(set1)
# set1.remove(9999) #keyError

# discard()
set1.discard(55)
print(set1)
set1.discard(9999) # no error
print(set1)


# builtin methods of set, tuple, list

# 1. all() -> checks for the True set of boolean values
# all values must be true to get true as ans
set1 = {1,2,3,4,5,6,7}
print("The set values are: ", set1)
print(all(set1))
set2 = {False, 1, 8}
print(all(set2))
set3 = {0, 1}
print(all(set3))

list = [1,2,4,-1, ""] # ""=>False
print(all(list))

tuple = (0,)
print(all(tuple))                 

# 2. any() -> checks if there is atleast one true value in collection/sequence or not
set1 = {1,2,3,4,5,6,7,0,0,0}
print("The set values are: ", set1)
print(any(set1))
set2 = {False, 1, 8}
print(any(set2))
set3 = {0, 1}
print(any(set3))

list = [1,2,4,-1, ""] # ""=>False
print(any(list))

tuple = (0,)
print(any(tuple))

# 3. len() method
print(len(set1)) 
set2 ={1,1,True,0,0}
# 1 and True are considered as same in a set
# 0 and False are considered as same in a set
print(len(set2))

# 4. max() and min()
set1 = {1,3,77,99,12,-4,-11}
print("the maximum value in set is:",max(set1))
print("the minimum value in set is:",min(set1))

# 5. sum()
# adds all the elements
set1 = {1,3,77,99,12,-4,-11}
print(sum(set1))

# set operations => union, Intersection, difference
# UNION => combines unique elements from set A and B
# union() and |
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
print(set1.union(set2))
print(set1) # original sets are not changed

print("using | operator:", set1 | set2)

# INTERSECTION => common elements from set A and B
print(set1.intersection(set2))
print(set1 & set2)

# DIFFERENCE => A-B gives the elements of A removing the common elements between A and B
# only those elements are returned which are not in B
print(set1.difference(set2))
print(set1 - set2)

#Inplace update set operations
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
print("original set1:", set1)
print("original set2:", set2)
set1.intersection_update(set2)
print("Updated set1:", set1) #set1 is changed
print("Set2:", set2) #set2 is not changed

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
print("original set1:", set1)
print("original set2:", set2)
set2.intersection_update(set1)
print("set1:", set1) #set1 is not changed
print("Updated Set2:", set2) #set2 is changed

# SIMILARLY difference_update()
# but there is no method as union_update(), we have update()


#...................Symmetric-difference()...................
# This method returns all the values present in given set data structures except the common values in them
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
print("original set1:", set1)
print("original set2:", set2)
print(set1.symmetric_difference(set2))
print(set1)
print(set2) 

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
print("original set1:", set1)
print("original set2:", set2)
print(set1.symmetric_difference_update(set2))
print(set1)
print(set2) 
'''

# issuperset(), issubset(), isdisjoint()
set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6,7,8,9,10}
set3 = {11,22,33,44}
print("If set1 is a subset of set2:", set1.issubset(set2))
print("If set1 is a superset of set2:", set1.issuperset(set2))
print("If set2 is a subset of set1:", set2.issubset(set1))
print("If set2 is a superset of set1:", set2.issuperset(set1))
print("If set2 is a superset of set1:", set2.issuperset(set1))
print("If set1 and set3 are disjoint sets:", set1.isdisjoint(set3))

