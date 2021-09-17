import  random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={'Frank': {'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002', 'ran': 38340677, 'money': 10},
      'cy': {'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002', 'ran': 38340678, 'money': 100}}
bank_name="汉科软地球中国老牛湾分行"#全局变量
def bank_adduser(username,password,country,province,street,door,account,money):
    if username in bank :#如果一个变量在容器内就运行代码
        return 2
    if len(bank)>=100:
        return 3
    bank[username]={
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "ran": account,
        "money":money,
        "bank_name":bank_name
    }
    return 1
def useradd():
    username=input("请输入您的用户名：")#局部变量
    password = input("请输入密码：")#print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10000000,99999999)
    money=0
    bankadd=bank_adduser(username,password,country,province,street,door,account,money)
    if bankadd == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    elif bankadd ==2:
        print("用户已存在")
    elif bankadd == 3:
        print("数据库已满")
def save_money():
    username=input("输入存款用户名：")
    if username in bank :
        print("用户名存在")
        save=int(input("输入存入金额："))
        bank[username]['money']=save
    else:
        print("用户名不存在")
def withdraw_money():
    username=input("输入取款用户名：")
    if username in bank :
        print("用户名存在")
        ran=int(input("请输入账号："))
        if bank[username]['ran']==ran :
            password=input("请输入密码：")
            if bank[username]['password']==password:
                print("登录成功！！")
                withdraw=int(input("输入取出金额："))
                if bank[username]['money']<withdraw :
                    print("余额不足")
                elif bank[username]['money']>=withdraw :
                    bank[username]['money']=bank[username]['money']-withdraw
            else:
                print("密码错误")
        else:
            print("账号错误")
    else:
        print("用户名不存在")
def loge(username,ran,password):
    if username in bank:
        print("用户名存在")
        if bank[username]['ran'] == ran:
            if bank[username]['password'] == password:
                print("登录成功！！")
            else:
                print("密码错误")
        else:
            print("账号错误")
    else:
        print("用户名不存在")
def transfer_accounts():
    username = input("输入转出用户名：")
    ran = int(input("请输入转出账号："))
    password = input("请输入转出密码：")
    loge(username,ran,password)
    transfer_user=input("输入转入用户名：")
    if transfer_user in bank :
        print("转入用户存在")
        transfer_money=int(input("输入转账金额："))
        if bank[username]['money']>=transfer_money :
            print("转账成功")
            bank[username]['money']=bank[username]['money']-transfer_money
            bank[transfer_user]['money']=bank[transfer_user]['money']+transfer_money
        else:
            print("余额不足")
    else:
        print("转入用户不存在")
def query():
    username = input("输入用户名：")
    ran = int(input("请输入账号："))
    password = input("请输入密码：")
    loge(username,ran,password)
    print("查询用户信息成功，以下是您的信息")
    info = '''
                ------------个人信息------------
                用户名:%s
                账号：%s
                密码：%s
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
                余额：%s
            '''
    # 每个元素都可传入%
    print(info % (username, ran,password,bank[username]['country'],bank[username]['province'],bank[username]['street'],bank[username]['door'],bank[username]['money']))

while True:#永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
        print(bank)
    elif begin == "2":
        print("取钱")
        withdraw_money()
        print(bank)
    elif begin == "3":
        print("存钱")
        save_money()
        print(bank)
    elif begin == "4":
        print("转账")
        transfer_accounts()
        print(bank)
    elif begin == "5":
        print("查询")
        query()
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")





