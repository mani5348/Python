#write a program to generate Random Numbers from 1 to 20 and Append Them to the List
#write a program to generate Random Numbers from 1 to 20 and Append Them to the List
import random
a=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)