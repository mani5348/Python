#write a program to Sort a List of Tuples in Increasing Order by the Last Element in Each
#write a program to Sort a List of Tuples in Increasing Order by the Last Element in Each
list1=[(2,3,5),(3,4),(2,2),(2,0)]
list2=[]
list3=[]
for i in range(0,len(list1)):
    list2.append(list1[i][-1])
for i in range(len(list2)):
    ind=min(list2)
    d=list2.index(ind)
    list3.append(list1[d])
    list1.pop(d)
    list2.pop(d)
print(list3)