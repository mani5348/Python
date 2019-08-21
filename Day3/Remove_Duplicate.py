#write a program to Remove the Duplicate Items from a List
a=[]
n=int(input("how many no. you want to enter:"))
for j in range(0,n):
    c=int(input("enter the no.: "))
    a.append(c)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items:")
print(unique)