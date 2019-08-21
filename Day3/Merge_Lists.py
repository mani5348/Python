#write a program to Merge Two Lists and Sort them in decending order
list1=[2,3,4,5,6]
list2=[7,8,9,0,1]
list1.extend(list2)
list1.sort(reverse=True)
print(list1)
