x =input("enter any string :")
count=0
vowels='aeiouAEIOU'
for s in x:
    if s in vowels:
        count=count+1
print("no. of vowels are:",count)
    