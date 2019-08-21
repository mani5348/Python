#write a program to Swap the First and Last Value of a List
list1=[]
n=int(input("how many no. you want to enter:"))
for i in range(1,n+1):
    a=int(input("enter the no.: "))
    list1.append(a)
list1[0],list1[n-1]=list1[n-1],list1[0]
print(list1)
    