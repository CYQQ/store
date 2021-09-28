import xlrd
wb=xlrd.open_workbook(filename=r"D:\python-test\day09【xlrd】\2020年每个月的销售情况.xls",encoding_override=True)
cloth=[]
cloth_piece={}
for i in range(12) :
    st=wb.sheet_by_index(i)
    row=st.nrows
    for j in range(1,row) :
        date=st.row_values(j)
        cloth.append(date[1])
cloth0=[]
for i in cloth:
    if not i in cloth0:
        cloth0.append(i)
print("展示所有衣服",cloth0)#展示所有衣服
a=input("查看具体衣服详情输入1，查看总销售情况输入2   :")
if a=='1' :
    for key in cloth0 :
        year_sum = 0
        year_piece = 0
        piece1 = 0
        piece1_money = 0
        piece_name=key
        for i in range(12) :
            moon_money = 0
            moon_piece=0
            st=wb.sheet_by_index(i)
            row=st.nrows
            for j in range(1,row) :
                date=st.row_values(j)
                year_piece=year_piece+date[4]
                year_sum=date[2]*date[4]+year_sum
                if date[1]==piece_name :
                    piece1=piece1+date[4]
                    piece1_money=piece1_money+date[2]*date[4]
                    moon_money=moon_money+date[2]*date[4]
                    moon_piece=moon_piece+date[4]
            print(piece_name,"的",i+1,"月销售量为：",moon_piece,"销售额为：",moon_money)
        print(piece_name,'全年总销量：',piece1,"占比为：",piece1/year_piece,"销售额占比：",piece1_money/year_sum)
        cloth_piece.update({piece_name:piece1_money/year_sum})
    print(cloth_piece)
    print(min(cloth_piece,key=cloth_piece.get),"销量最差")
    print(max(cloth_piece, key=cloth_piece.get),"销量最好")

elif a=='2':
    year_sum1=0
    year_piece1=0
    for i in range(12) :
        st=wb.sheet_by_index(i)
        row=st.nrows
        for j in range(1,row) :
            date1=st.row_values(j)
            year_piece1=year_piece1+date1[4]
            year_sum1=date1[2]*date1[4]+year_sum1
    print("所有衣服全年的总销售额：",year_sum1)
    print("所有衣服全年销售总件数：",year_piece1)



