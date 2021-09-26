import  random
from DBUtils import update,select
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")

def adduser(username, account, password, country, province, street, door, money, bank_name):
    sql="select * from bank where ename=%s"
    sql1="select * from bank"
    param=[username]
    param1=[]
    date1=select(sql,param,mode='all')
    date2=select(sql1,param1,mode='all')
    if len(date1)==1 :#如果一个变量在容器内就运行代码
        return 2
    if len(date2)>=100:
        return 3
    else:
        sql3="insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [username, account, password, country, province, street, door, money, bank_name]
        update(sql3,param2)
        return 1
def useradd():
    username=input("请输入您的用户名：")#局部变量
    password = int(input("请输入密码："))
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    bank_name=input("\t\t银行:")
    account=random.randint(10000000,99999999)
    money=0
    add=adduser(username, account, password, country, province, street, door, money, bank_name)
    if add == 1:
        print("添加用户成功")
    elif add ==2:
        print("用户已存在")
    elif add == 3:
        print("数据库已满")
def save_money():
    sql = "select * from bank where ename=%s"
    username=input("输入存款用户名：")
    param=[username]
    date=select(sql, param, mode='all')
    if len(date)==1:
        print("用户名存在")
        save=int(input("输入存入金额："))
        sql2="update bank set money=%s where ename=%s"
        param2=[save,username]
        update(sql2,param2)
    else:
        print("用户名不存在")
def withdraw_money():
    username=input("输入取款用户名：")
    ran=int(input("请输入账号："))
    password=input("请输入密码：")
    sql="select * from bank where ename=%s and username=%s and password=%s"
    param=[username,ran,password]
    date=select(sql,param,mode='all')
    if len(date)==1 :
        print("登录成功")
        save=int(input("输入取出金额："))
        sql2="update bank set money=money-%s where ename=%s"
        param2=[save,username]
        update(sql2,param2)
        return 1
def loge(username,ran,password):
    sql="select * from bank where ename=%s and username=%s and password=%s"
    param=[username,ran,password]
    date=select(sql,param,mode='all')
    if len(date)==1 :
        print("登录成功")
        return 1
def transfer_accounts():
    username = input("输入用户名：")
    ran = int(input("请输入账号："))
    password = input("请输入密码：")
    log=loge(username,ran,password)
    if log==1 :
        tra_ename=input("输入转账账号名：")
        tra_money=int(input("输入转账金额："))
        sql1="update bank set money=money-%s where ename=%s"
        sql2="update bank set money=money+%s where ename=%s"
        param=[tra_money,username]
        param2=[tra_money,tra_ename]
        update(sql1,param)
        update(sql2,param2)

def query():
    username = input("输入用户名：")
    ran = int(input("请输入账号："))
    password = input("请输入密码：")
    log = loge(username, ran, password)
    if log == 1 :
        sql = "select * from bank where ename=%s"
        param=[username]
        select(sql,param,mode='all')


while True:#永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        print("取钱")
        withdraw_money()
    elif begin == "3":
        print("存钱")
        save_money()
    elif begin == "4":
        print("转账")
        transfer_accounts()
    elif begin == "5":
        print("查询")
        query()
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")





