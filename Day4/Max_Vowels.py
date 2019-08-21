#write a program to create function as find_vowel(string,string,string) with three strings as input and return a vowel that is occurred maximum times.
def find_vowel(str1,str2,str3):
    str4=str1+str2+str3
    a=str4.count("a")+str4.count("A")
    e=str4.count("e")+str4.count("E")
    i=str4.count("i")+str4.count("I")
    o=str4.count("o")+str4.count("O")
    u=str4.count("u")+str4.count("U")
    list1=[a,e,i,o,u]
    max1=max(list1)
    ind=list1.index(max(list1))
    list2=['a','e','i','o','u']
    print(list2[ind],"occuring max of times",max1)
str1=input("enter string:")
str2=input("enter string:")
str3=input("enter string:")
find_vowel(str1,str2,str3)