num=int(input("enter any no: "))
a=len(str(num))
temp=num
sum=0
while(temp>0):
    rem=temp%10
    sum=sum+(rem**a)
    temp=temp//10
if(num==sum):
    print("armstrong no")
else:
    print(" not armstrong no")
