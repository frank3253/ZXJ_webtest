# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os

# =========================邮件接收者============================
mailto_list = ["haoyan2@iflytek.com"]

# ============= 设置服务器，用户名、口令以及邮箱的后缀===============
mail_host = "smtp.126.com"
mail_user = "iflytek_webtest@126.com"
mail_pass = "iflytek2019"


# ===========================发送邮件============================
def send_mail(to_list, file_new, file_name):
    """
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("iflytek_webtest@126.com","sub","content")
    """
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    me = mail_user
    msg = MIMEMultipart('related')  # 采用related定义内嵌资源的邮件体

    msgtext = MIMEText(mail_body, 'html', 'utf-8')       # subtype有plain,html等格式
    msg.attach(msgtext)

    msg['Subject'] = Header('转写机分享页自动化测试报告')
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    attach = MIMEText(mail_body, 'base64', 'utf-8')
    attach["Content-Type"] = 'application/octet-stream'
    attach["Content-Disposition"] = 'attachment; filename=' + '"' + file_name + '"'
    msg.attach(attach)

    try:
        s = smtplib.SMTP()
        s.connect(mail_host, 25)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.quit()
        return True
    except Exception as e:
        print(str(e))
        return False


# ==============查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './shareweb/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    discover = unittest.defaultTestLoader.discover("e:/ZXJ_webtest/shareweb/test_case",
                                                   pattern='test_*.py')
    runner = HTMLTestRunner(stream=fp,
                            title='分享页面自动化测试报告',
                            description='环境 ：window 10 浏览器：chrome')
    runner.run(discover)
    fp.close()
    file_path = new_report('./shareweb/report/')

    if send_mail(mailto_list, file_path, now + 'result.html'):
        print("发送成功")
    else:
        print("发送失败")
