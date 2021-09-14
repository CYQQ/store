import random
print("猜数字游戏!")
print("输入1开始游戏，输入0关闭游戏")
a=input("开始/关闭")
if a=='1' :
    s_money = 0
    index = 0
    num=0
    ran = random.randint(0, 90)
    i_money = int(input("输入充值金额"))
    print("每次猜数字需要500")
    s_money = (s_money + i_money) * (1 + i_money / 10000)
    print("总金额",s_money)
    print('开始猜数字')
    while index<=4 and (s_money-index*500>500):
        index+=1
        num=int(input("输入数字"))
        if num==ran :
            print("猜中了！")
            break
        elif num>ran :
            print("你猜的数太大了！")
        elif num<ran :
            print("你猜的数太小了！")
    if index<5 and num!=ran:
        print('金额不足，游戏结束')
    elif index ==5 :
        print('五次没有猜中，游戏结束')
    s_money = s_money - index * 500
    print('总金额',s_money)