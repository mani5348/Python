# create a python script which will pull the data from EMP.CSV file and 
# create a new file that will have the calculated average salary based on deptno where total_sal is sal+comm.
import pandas as pd
sc=pd.read_csv("EMP.csv")
d1=sc.loc[sc['DEPTNO']==10]
d2=d1['SAL']+d1['COMM']
AVG_10=d2.mean(axis=0)
#print(AVG_10)
d3=sc.loc[sc['DEPTNO']==20]
d4=d3['SAL']+d3['COMM']
AVG_20=d4.mean(axis=0)
d5=sc.loc[sc['DEPTNO']==30]
d6=d5['SAL']+d5['COMM']
AVG_30=d6.mean(axis=0)
#sc1=pd.write_csv("average_sal.csv",usecols=['DEPTNO','AVG_SAL'])
#dep={10,20,30}
#me={AVG_10,AVG_20,AVG_30}
dict1={'dep10':[AVG_10],'dept20':[AVG_20],'dept30':[AVG_30]}
df1=pd.DataFrame(dict1)
df1.to_csv("AVGSAL.csv")