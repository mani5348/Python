a=int(input("enter the no:"))
k=2*a-2
for i in range (0,a):
    for j in range(0, k): 
        print(end=" ") 
    k=k-1
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")
'''for i in range (a,a-1,-1):
    for j in range (k, 0):
        print(" ")
    k=k-1
    for j in range(0, i):
        print("* ",end="")
        print("\r")'''
    