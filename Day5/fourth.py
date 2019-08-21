# create a python script which will generate a file as allmanagers.csv, 
# data records with managers as job to be pulled from emp.csv.
import pandas as pd
sc=pd.read_csv("EMP.csv",usecols=['ENAME','EMPNO','SAL','DEPTNO','JOB'])
d1=sc.loc[sc['JOB']== 'MANAGER']
d1.to_csv("allmanagers.csv")
