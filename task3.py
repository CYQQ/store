# #case1
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# num=0
# age=0
# man=0
# wman=0
# index1=0
# index2=0
# index3=0
# index4=0
# for i in range(len(names)) :
#     num=names[i][5]+num
# for i in range(len(names)) :
#     age=int(names[i][1])+age
# print("平均工资",num/len(names))
# print("平均年龄",age/len(names))
# names.append(["刘备", "45", "男", "220", "alibaba", 500 , "30"])
# print(names)
# for i in range(len(names)) :
#     if names[i][2]=='男' :
#         man+=1
#     elif names[i][2]=='女' :
#         wman+=1
# print("女性人数为：",wman)
# print("男性人数为：",man)
# for i in range(len(names)) :
#     if names[i][6]=='50' :
#         index1+=1
#     elif names[i][6]=='60' :
#         index2 += 1
#     elif names[i][6]=='10' :
#         index3 += 1
#     elif names[i][6]=='30' :
#         index4 += 1
# print("部门-50,人数为：",index1)
# print("部门-60,人数为：",index2)
# print("部门-10,人数为：",index3)
# print("部门-30,人数为：",index4)


#case2
# stu=[
# ['罗恩', 23 ,35 ,44],
# ['哈利' ,60, 77 ,68 ,88, 90],
# ['赫敏', 97 ,99 ,89 ,91, 95, 90],
# ['马尔福',100, 85 ,90]
# ]
# for i  in range(len(stu)) :
#     sum = 0
#     j = 1
#     while j<len(stu[i]) :
#         sum=sum+stu[i][j]
#         j=j+1
#     print(stu[i][0],'的总成绩为',sum)

#case3
# num=int(input('输入一个数：'))
# while num!=0 :
#     print(num%10)
#     num=num//10

#case4
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [5,2,4,7,9,1,3,5,4,0,6,1,3]
# bubbleSort(arr)
# print("排序后的数组:")
# for i in range(len(arr)):
#     print(arr[i],' ',end=""),

#case5
# #创建用户名和密码
# buy={}
# def buy_add(user,password):
#     buy.update(
#         {
#             user:password
#         }
#     )
# def useradd() :
#     user=int(input("输入新账号："))
#     password = int(input("输入密码："))
#     if user in buy:
#         print("账号重复")
#     else:
#         buy_add(user,password)
#         print("添加账号成功")
# def loge(user,password) :
#     if user in buy and password==buy[user]:
#         print("登录成功")
#     else:
#         print("登录失败")
# while True :
#     print("|------------1、创建              ------------|")
#     print("|------------2、登录             ------------|")
#     order=int(input())
#     if order==1 :
#         useradd()
#         print(buy)
#     elif order==2 :
#         user = int(input("输入账号："))
#         password = int(input("输入密码："))
#         loge(user,password)




