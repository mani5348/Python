#write a program to Find the 3rd Largest Number in a List
list=[1,2,4,32,5,8,4,9,10,15]
list.sort()
print("sorted list is :",list)
len1=len(list)
print("Third largest element in the list is :",list[len1-3])
