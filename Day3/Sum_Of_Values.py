#write a  Program to Sum All the Items in a Dictionary
n=int(input("Enter the no. of keys :"))
dict1={}
for i in range(1,n+1):
    key=input("enter key values:")
    value=int(input("enter the values of keys:"))
    dict1.update({key:value})
sum1=sum(dict1.values())
print(sum1)
