#write a program to create function as long_name(stringvalue,stringvalue) input two strings and find which is lengthy
def long_name(str1,str2):
    s1=len(str1)
    s2=len(str2)
    if(s1>s2):
        return str1
    else:
        return str2
str1=input("enter first string :")
str2=input("enter 2nd string :")
res=long_name(str1,str2)
print("lengthy string is :",res)