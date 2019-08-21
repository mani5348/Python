# Create a python script which is accept the required value for salary and
# print on screen only the ename who are getting the same salary.
import pandas as pd
sc=pd.read_csv("EMP.csv",usecols=['ENAME','SAL'])
s1=int(input("enter salary:"))
d1=sc.loc[sc['SAL']==s1]
print(d1) 