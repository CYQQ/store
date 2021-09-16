#case1
# listcity = ['北京','上海','广东']
# listcity[1]='广东'
# listcity[2]='上海'
# print(listcity)
# listgdp =[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# sum=0
# for i in range(len(listgdp)) :
#     sum=sum+listgdp[i]
# print('GDP总和:','%.2f'%sum)
# avg=sum/8
# print('平均GDP:','%.2f'%avg)

#case2
# sum=0
# a = [1,5,21,30,15,9,30,24]
# for i in range(len(a)) :
#     if a[i]%5==0 :
#         print(a[i])
#         sum=a[i]+sum
# print(sum)

#case3
# List = [1,2,3,4,5,6,7,8,9]
# newList = []
# for i in  range(len(List)) :
#     newList.append(List[len(List)-i-1])
# List=newList
# print(List)

#case4
# lists=[]
# list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# for i in range(len(list)) :
#     lists.append(list[i])
#     if lists.count(list[i])>1:
#         break
#     print(list[i],"出现了",list.count(list[i]),"次")