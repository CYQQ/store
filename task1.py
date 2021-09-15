#case1
#i=0
# sum=0
# for i in range(10) :
#     i+=1
#     a=int(input("number:"))
#     sum=sum+a
# print('数字之和',sum)

#case2
# i=0
# sum=0
# max=0
# for i in range(10) :
#     i+=1
#     a=int(input("number:"))
#     sum=sum+a
#     if a>max :
#         max=a
# print('数字之和',sum)
# print('平均数',sum/10)
# print('最大值',max)

#case3
# import random
# ran=random.randint(50,150)
# print(ran)

#case4
# a=int(input("A边:"))
# b=int(input("B边:"))
# c=int(input("C边:"))
# if a+b>c :
#     print("构成普通三角行")
#     if a==b or b==c or a==c :
#         print('等腰三角形')
#         if a==b==c :
#             print('等边三角形')

#case5
# A=56
# B=78
# print(A,B)
# T=A
# A=B
# B=T
# print(A,B)


#case6
# import sys
# user='root'
# password='admin'
# lock_usr=[]
# i=0
# while i<3 :
#     user1=input("user:")
#     if user1==user :
#         password1 = input("password:")
#         if password1==password :
#             print('密码输入正确')
#             sys.exit()
#         else:
#             print('密码输入错误')
#             i+=1
#             if i==3 :
#                 lock_usr.append(user1)
#     else:
#         print("用户名输入错误")
# print('锁定账号',lock_usr)

#case7
# for i in range(8) :
#     for k in range(8-i-1) :
#         print(' ',end='')
#     for j in range(i) :
#         print('* ',end='')
#     print()

#case8
# i=1
# while i<=9:
#     j=1
#     while j<=i :
#         print(i,'*',j,'=',i*j,' ',end='')
#         j+=1
#     i+=1
#     print()

#case9
# i=9
# while i>=1:
#     j=1
#     while j<=i :
#         print(i,'*',j,'=',i*j,' ',end='')
#         j+=1
#     i-=1
#     print()

#case10
# clb=0
# index=0
# while True :
#     index=index+1
#     clb=clb+3
#     if clb>=20 :
#         break
#     clb=clb-2
# print('第',index,'天出来')

#case11
# char
# Cy%ty 非法
# Oax_li
# $123 非法
# fLul
# 3_3 非法
# BYTE
# T_T

#case12
# import random
# s_money = 0
# num = 0
# print("猜数字游戏!")
# while True :
#     print("输入1开始游戏，输入0关闭游戏")
#     a=input("开始/关闭")
#     if a=='1' :
#         ran = random.randint(0, 90)
#         i_money = int(input("输入充值金额"))
#         print("每次猜数字需要500")
#         s_money = (s_money + i_money) * (1 + i_money / 10000)
#         print("总金额",s_money)
#         print('开始猜数字')
#         index = 0
#         while index<=4 and (s_money-index*500>500):
#             index+=1
#             num=int(input("输入数字"))
#             if num==ran :
#                 print("猜中了！")
#                 break
#             elif num>ran :
#                 print("你猜的数太大了！")
#             elif num<ran :
#                 print("你猜的数太小了！")
#         if index<5 and num!=ran:
#             print('金额不足，游戏结束')
#         elif index ==5 :
#             print('五次没有猜中，游戏结束')
#         s_money = s_money - index * 500
#     elif a=='0' :
#         break

#case13
# def factorial(n):
#     if n == 1: return 1
#     return n*factorial(n-1)
# sum=0
# for i in range(1, 21):
#     sum=sum+factorial(i)
# print(sum)



