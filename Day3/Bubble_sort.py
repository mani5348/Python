#write a program to Find the Second Largest Number in a List Using Bubble Sort
list1=[9,3,6,7,4,5,8]
length=len(list1)
for i in range(0,length):
    for j in range(0,length-i-1):
        if(list1[j]>list1[j+1]):
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print("Second largest no.is:",list1[length-2])