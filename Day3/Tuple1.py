#write a program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
a=[2,3,4,5]
res=[(val,pow(val,2)) for val in a]
print(res)