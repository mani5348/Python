#write a program to create function as sort_date(date,date,date) and sort them values from tin descending order
from datetime import date
def sort_date(date1,date2,date3):
    ls=[]
    ls1=[]
    ls.append(date1)
    ls.append(date2)
    ls.append(date3)
    ls.sort()
    ls1=ls[::-1]
    print(ls)
list1=[]
for i in range(0,3):
    year=input("enter year in yyyy formate:")
    month=input("enter month in mm formate:")
    day=input("enter day in dd formate:")
    date4=date(int(year),int(month),int(day))
    
    list1.append(str(date4))
sort_date(list1[0],list1[1],list1[2])