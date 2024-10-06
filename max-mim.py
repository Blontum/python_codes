# Write a Python program that prints the largest(max) and smallest(min) values in a list
# Print the two values on the same line, separated by a space.
# The largest value should appear first and the smallest value should appear second.
# You may assume that the list only contains numeric values.
# If the list is empty, print None.
#expected output: see above

list1 = [3,4,5,6]
if list1:
    print(max(list1),min(list1))
else: 
    print(list1, "None")

list2 = [-1,-2,-3,-4]
if list2: 
    print(max(list2),min(list1))
else:
    print(list2, "none")

list3 = [0,0,0,0]
if list3:
    print(max(list3),min(list3))
else:
    print(list3, "None")

list4 = []
if list4:
    print(max(list4,min(list4)))
else:
    print(list4,"none")



 