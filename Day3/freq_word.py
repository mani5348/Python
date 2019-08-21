#write a  Program to Count the Frequency of Words Appearing in a String Using a Dictionary
str1=input("enter any string:")
list1=[]
list1=str1.split()
freq=[list1.count(i) for i in list1]
a=dict(zip(list1,freq))
print(a)