#write a program to move Even and Odd elements from a list into two seperate Lists
list1=[]
n=int(input("how many no. you want to enter:"))
for j in range(1,n+1):
    a=int(input("enter the no.: "))
    list1.append(a)
even=[]
odd=[]
for i in list1:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("odd elements are:",odd)
print("even elements are:",even)    