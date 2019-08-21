# Create a python script which will create three separate files named as Dept_10.csv,dept_20.csv,dept_30.csv putting 
# the data in readable format based on the deptno values of each record.
import pandas as pd
#sc=pd.read_csv=("EMP.csv",usecols=['EMPNO','ENAME','JOB','SAL','DEPTNO'])
sc=pd.read_csv("EMP.csv",usecols=['ENAME','SAL','DEPTNO'])
d1=sc.loc[sc['DEPTNO']==10]
d1.to_csv('Dept_10.csv')
d2=sc.loc[sc['DEPTNO']==20]
d2.to_csv('Dept_20.csv')
d3=sc.loc[sc['DEPTNO']==30]
d3.to_csv('Dept_30.csv')