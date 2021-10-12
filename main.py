# 生产测试报告
from HTMLTestRunner import HTMLTestRunner  # 界面报告运行，给用户，返回报告
import unittest
from email.mime.text import MIMEText
from email.header import Header
import time
import os.path as pth
import smtplib
#读取报告，定义邮件正文#定义邮件标题
#发送邮件

def sendEmail(content, title, from_name, from_address, to_address, serverport, serverip, username, password):
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    msg['Subject'] = Header(title, 'utf-8')
    # 这里的to_address只用于显示，必须是一个string
    msg['To'] = ','.join(to_address)
    msg['From'] = from_name
    try:
        s = smtplib.SMTP_SSL(serverip, serverport)
        s.login(username, password)
        # 这里的to_address是真正需要发送的到的mail邮箱地址需要的是一个list
        s.sendmail(from_address, to_address, msg.as_string())
        print('%s----发送邮件成功' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except Exception as err:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(err)
 #HEFEN_D = pth.abspath(pth.dirname(__file__))
def main2():
    TO = ['18339181263@163.com']
    config = {
         "from": "chenyifree@foxmail.com",
         "from_name": '自动化测试unittest测试框架报告:',
         "to": TO,
         "serverip": "smtp.qq.com",
         "serverport": "465",
         "username": "chenyifree@foxmail.com",
         "password": "vpirrocsbjctbcci"  # QQ邮箱的SMTP授权码
    }

    title = "自动化测试"
    f = open("D:\python-test\day13【单元测试】\代码\day13\计算器.html", 'rb')
    mail_body = f.read()
    f.close()
    sendEmail(mail_body, title, config['from_name'], config['from'], config['to'], config['serverport'], config['serverip'],
               config['username'], config['password'])

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\python-test\day13【单元测试】\代码\day13",pattern="Test*.py")



# 2.创建 运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title= "计算器测试报告",
    description="计算器的加法报告",
    verbosity=1,
    stream = open(file="计算器2.html",mode="w+",encoding="utf-8")
)

# 3.运行用例
runner.run(tests)
main2()


# 4.邮件发送
# 代码的方式发送邮件，报告当成附件发送给我。
# 温馨提示：授权码，不是登陆密码。开启授权码。







