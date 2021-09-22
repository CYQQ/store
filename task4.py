#case1
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for key in dict :
#     print(key,end='')
# print('\n')
# for key in dict:
#     print(dict[key],end='')
# print('\n')
# dict.update({"k4":"v4"})
# print(dict)

#case2
# index1=0
# index2=0
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#
#     }
# }
# for key in info['小明']['fruits'] :
#     index1=info['小明']['fruits'][key]+index1
# print("小明花费金额：",index1)
# for key in info['小刚']['fruits'] :
#     index2=info['小刚']['fruits'][key]+index2
# print("小刚花费金额：",index2)
# info['小明']['money']=index1
# info['小刚']['money']=index2
# print(info)

#case3
# info={}
# def count(a) :
#     import collections
#     b=collections.Counter(a)
#     for c in b :
#         info.update({c:b[c]})
#
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# count(a)
# print(info)

#case4
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# names1={}
# for i in range(len(names)) :
#     names1.update({names[i][0]:{'年龄':names[i][1],'性别':names[i][2],'编号':names[i][3],'公司':names[i][4],'薪资':names[i][5],'部门':names[i][6]}})
# print(names1)