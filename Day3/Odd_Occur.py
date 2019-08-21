#Python Program to Find Element Occurring Odd Number of Times in a List
list1=[]
list2=[]
n=int(input("how many no. you want to enter:"))
for i in range(0,n):
    a=int(input("enter the no.: "))
    list1.append(a)
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(list1[i]==list1[j]):
            c=c+1
    if(c%2!=0):
        list2.append(list1[i])
a=list(set(list2))
print(a)
print(len(a))
