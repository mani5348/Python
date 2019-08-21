#write a  Program to Remove the Given Key from a Dictionary
n=int(input("enter the no.of keys:"))
dict1={}
for i in range(1,n+1):
    key=input("enter keys:")
    value=int(input("enter the value of keys:"))
    dict1.update({key:value})
rem=input("enter the key want to remove:")
if rem in dict1:
    del dict1[rem]
else:
    print("not exists!")
print(dict1)
