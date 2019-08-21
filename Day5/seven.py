# create a script which will read the data from EMP.CSV file and
# create will all the data a new file in sort order of sal in ascending.
import pandas as pd
cs=pd.read_csv("EMP.csv",usecols=['EMPNO','ENAME','JOB','MGR','HIREDATE','SAL','COMM','DEPTNO','ROWNUM'])
#sal1=cs.loc[cs["SAL"]]
cs.sort_values('SAL', axis=0,ascending=True,inplace=True)
df=pd.DataFrame(cs)
df.to_csv("EMP1.csv")
