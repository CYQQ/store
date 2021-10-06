from DUBTILE import update
from DUBTILE import select
import xlrd

wb = xlrd.open_workbook(filename=r"D:\python-test\day09【xlrd】/2020年每个月的销售情况.xls", encoding_override=True)

moon=input("导入几月份的数据:")
st = wb.sheet_by_name(moon)
rows = st.nrows #  多少行
cols = st.ncols # 多少列
for i in range(1,st.nrows) :
    date=st.row_values(i)
    sql="insert into shuju values (%s,%s,%s,%s,%s,%s)"
    param=[st.row_values(i)[0],st.row_values(i)[1],st.row_values(i)[2],st.row_values(i)[3],st.row_values(i)[4],moon]
    update(sql,param)

