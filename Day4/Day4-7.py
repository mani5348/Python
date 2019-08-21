# write a program to create a functions as vow_pad(string) input as a string and it will add “*” to both the side of the string as many vowels are there in the string
def vow_pad(str1):
    #vowels=='aeiouAEIOU'
    count=0
    for s in str1:
        if (s=='a' or s=='e' or s=='i' or s=='o' or s=='u' or s=='A' or s=='E' or s=='I' or s=='O' or s=='U'):
            count=count+1
    e='*'
    m=e*count
    print(m+str1+m)
str1=input("enter any string:")
vow_pad(str1)