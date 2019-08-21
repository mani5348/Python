#write a  Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n=int(input("enter the no. of keys in Dictionary:"))
dict1={}
for i in range(1,n+1):
    dict1.update({i:(i*i)})
print(dict1)
    