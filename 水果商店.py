
    # 需求：
    #     购物流程。
    #     1.商品在货架上
    #     2.空的购物车
    #     3.自己的初始化资金
    # 技术选型：
    #     1.容器
    #         列表： []
    #     2.循环技术
    #         while
    #         for i in  enumerate(li)
    #     3.判断
    #     4.键盘输入
    # 任务：
    # [10张老干妈：7折优惠券，20张联想电脑1折优惠券]
    # 开始买东西之前，提示是否要抽一张优惠券。
    #     若是：随机给一张，最终要进行使用优惠券的进行结算。
    #     若否：正常买东西

# 1.准备商品
import random
shop = [
    ["劳力士手表",200000],
    ["Iphone 12X plus",12000],
    ["lenovo PC",6000],
    ["HUA WEI WATCH",1200],
    ["Mac PC",15000],
    ["辣条",2.5],
    ["老干妈",13]
]
# 2. 初始化钱包
money = input("请输入您的余额：")
money = int(money)  # "200000" --> 200000

# 3.空的购物车
mycart = []
i = 0
index1 = 10
index2 = 20
discount_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30]
while i <= 20:
        discount=input("是否使用优惠卷yes/no:")
        if discount=='yes' :
            dis=random.sample(discount_number,1)
            if dis[0]<=10 :
                index1=index1-1
                discount_number.remove(dis[0])
                print("抽到老干妈优惠券")
                for key, value in enumerate(shop):
                    print(key, value)
                    # 4.2 请输入您想要的商品
                chose = input("亲输入您想要的商品编号：")  # "1"
                # 4.3
                if chose.isdigit():
                    chose = int(chose)
                    # 4.4 先判断是否存在该商品
                    if chose > 6:
                        print("您输入的商品不存在！别瞎弄！")
                    else:
                        # 4.5 判断您的余额是否足够
                        if money < shop[chose][1]*0.7:
                            print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                        else:
                            # 4.6 将商品添加到购物车 ，余额减去对应的钱
                            mycart.append(shop[chose])
                            money = money - shop[chose][1]*0.7
                            print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                elif chose == "q" or chose == "Q":
                    print("拜拜了，您嘞！欢迎下次光临！")
                    break
                else:
                    print("对不起，您输入有误，请重新输入！")
            elif dis[0]>10 :
                index2=index2-1
                discount_number.remove(dis[0])
                print("抽到联想电脑优惠券")
                for key, value in enumerate(shop):
                    print(key, value)
                    # 4.2 请输入您想要的商品
                chose = input("亲输入您想要的商品编号：")  # "1"
                # 4.3
                if chose.isdigit():
                    chose = int(chose)
                    # 4.4 先判断是否存在该商品
                    if chose > 6:
                        print("您输入的商品不存在！别瞎弄！")
                    else:
                        # 4.5 判断您的余额是否足够
                        if money < shop[chose][1]*0.1:
                            print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                        else:
                            # 4.6 将商品添加到购物车 ，余额减去对应的钱
                            mycart.append(shop[chose])
                            money = money - shop[chose][1]*0.1
                            print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                elif chose == "q" or chose == "Q":
                    print("拜拜了，您嘞！欢迎下次光临！")
                    break
                else:
                    print("对不起，您输入有误，请重新输入！")
        elif discount=='no' :
            for key, value in enumerate(shop):
                print(key, value)
                # 4.2 请输入您想要的商品
            chose = input("亲输入您想要的商品编号：")  # "1"
            # 4.3
            if chose.isdigit():
                chose = int(chose)
                # 4.4 先判断是否存在该商品
                if chose > 6:
                    print("您输入的商品不存在！别瞎弄！")
                else:
                    # 4.5 判断您的余额是否足够
                    if money < shop[chose][1]:
                        print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                    else:
                        # 4.6 将商品添加到购物车 ，余额减去对应的钱
                        mycart.append(shop[chose])
                        money = money - shop[chose][1]
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
            elif chose == "q" or chose == "Q":
                print("拜拜了，您嘞！欢迎下次光临！")
                break
            else:
                print("对不起，您输入有误，请重新输入！")


        i=i+1
print("老干妈券",index1)
print("联想券",index2)
