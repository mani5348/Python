#write a  Program to Check if a Given Key Exists in a Dictionary or Not
dict1={'Manish':1,'Kartik':2,'Shubham':3,'Yash':3,'Aman':4}
key=input("enter the key values what we want to check:")
if key in dict1.keys():
    print("Exists")
else:
    print("Not Exists")
