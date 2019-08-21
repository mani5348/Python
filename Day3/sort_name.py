#write a program to add 10 names to the list and sort according to the Length of the names
list1=[]
list2=[]
list3=[]
n=int(input("enter the no. of names you want to enter:"))
for i in range(0,n):
    a=input("enter the name:")
    list1.append(a)
for i in list1:
    b=len(i)
    list2.append(b)
for i in range(0,n):
    ind=list2.index(min(list2))
    list3.append(list1[ind])
    list2.pop(ind)
    list1.pop(ind)
print(list3)