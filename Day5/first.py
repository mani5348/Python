# Create a python script which will create three separate files named as Dept_10.csv,dept_20.csv,dept_30.csv
# putting the data in readable format based on the deptno values of each record.
import pandas as pd
cs=pd.read_csv("EMP.csv",usecols=['EMPNO','ENAME','JOB','SAL'])
print(cs)