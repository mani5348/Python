a=int(input("Enter a  Number "))
sum=0
while(a>0):
    rem=a%10
    sum=sum+rem
    a=a//10
print("sum of digits of no is:",sum)