# write a program to create a functions as Lpad(string,number) input a string value and number 
# it will return the exact number of characters from the string starting from first character
# If the number increases the no of characters then it will add “ * ” at the beginning of the string
def Lpad(str1,num):
    len1=len(str1)
    if(len1==num):
        print(str1)
    elif(len1>num):
        print(str1[0:num])
    else:
        d=num-len1
        e='*'
        m=e*d
        print(m+str1)
        
str1=input("enter any string:")
num=int(input("enter any number:"))
Lpad(str1,num)