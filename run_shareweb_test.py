# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from shareweb.test_case.models.getconfig import *
import smtplib
import unittest
import time
import os

# =========================邮件接收者============================
mailto_list = get_mail()[4]

# ============= 设置服务器，用户名、口令以及邮箱的后缀===============
mail_host = get_mail()[0]
mail_user = get_mail()[2]
mail_pass = get_mail()[3]


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

    # 创建邮件文本并添加到邮件中
    msgtext = MIMEText(mail_body, 'html', 'utf-8')       # subtype有plain,html等格式
    msg.attach(msgtext)

    # 初始化邮件体
    msg['Subject'] = Header('转写机分享页自动化测试报告')   # 邮件标题
    msg['From'] = me                                      # 发送人
    msg['To'] = ";".join(to_list)                         # 接收人 join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

    # 创建html附件并加入到邮件中
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
    for browser_name, browser_version in get_browser_type().items():
        print(browser_name, browser_version)
        set_browser_name(browser_name)         # 设置当前测试使用的浏览器名称
        set_browser_version(str(browser_version))       # 设置当前测试使用的浏览器版本号
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filename = './shareweb/report/' + now + browser_name + '-result.html'
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
