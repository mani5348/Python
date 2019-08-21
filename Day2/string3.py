str1=input("enter any string")
str2=""
for i in str1:
    if(i.isupper()):
        str2=str2+i.lower()
    else:
        str2=str2+i.upper()
print(str2)