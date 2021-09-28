import  xlwt
from DUBTILE import update,select
sql="select * from t_employees"
prarm=[]
date=select(sql,prarm,mode='all') #获取数据
row=0
col=0
list=[]
list2=[]
wb = xlwt.Workbook(encoding = True)
st = wb.add_sheet("三国员工")
for i in date :
    list.append(i)
for j in range(len(list)) :
    for k in list[j] :
        list2.append(k)
print(list2)
for k in range(len(list2)) :
    st.write(row,col,list2[k])
    col+=1
    if col==8 :
        row+=1
        col=0

wb.save("三国集团.xls")

