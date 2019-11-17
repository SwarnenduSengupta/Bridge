import os
import cx_Oracle
import csv
import xlsxwriter
sql="SELECT * from customers";
filename="output.csv"
file=open(filename,"w")
con = cx_Oracle.connect('test123/test@localhost/orcl')
workbook=xlsxwriter.Workbook('output1.xlsx');
worksheet=workbook.add_worksheet();
cur=con.cursor()
cur.execute('select * from Persons')
<cx_Oracle.Cursor on <cx_Oracle.Connection to test123@localhost/orcl>>

res=cur.fetchall()
type(res)
<type 'list'>
import pandas as pd
df=pd.DataFrame(res)
write=pd.ExcelWriter('pandas_simple.xlsx',engine='xlsxwriter')
df.columns=['Batchrun_id','time','lojack']
alpha=100
df=df.rename(index= lambda x:'BatchrunID ='+str(alpha))
df.to_excel(write,sheet_name='Sheet1')
workbook=write.book
worksheet=write.sheets['Sheet1']
exit()


