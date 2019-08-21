#write a  Program to Multiply All the Items in a Dictionary
n=int(input("enter the no.of keys:"))
dict1={}
mul=1
for i in range(1,n+1):
    key=input("enter keys:")
    value=int(input("enter the value of keys:"))
    dict1.update({key:value})
for i in dict1:
    mul=mul*dict1[i]
print(mul)