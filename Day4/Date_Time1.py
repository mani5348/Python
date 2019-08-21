# write a program to create a function as day_type(datevalue) input as date value and return holiday if it is Saturday 
#or Sunday and working day if it is other than Saturday and Sunday and if it is last day of the month return as salary day.
import datetime
import calendar

def day_type(datevalue):
    year,month,day=datevalue[0],datevalue[1],datevalue[2]
    wd=calendar.weekday(year,month,day)
    if((wd==5)or(wd==6)):
        print("Holiday")
    if(((day==31)and(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12))or((day==30)and(month==4 or month==6 or month==9 or month==11))):
        print("Salary day")
    elif((month==2)and(day==28 or day==29)):
        print("Salary day")
    else:
        print("Working day")

now=datetime.datetime.now()
dval=[now.year,now.month,now.day]
print(dval)
day_type(dval)
        
