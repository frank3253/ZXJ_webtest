# coding=utf-8
from selenium.webdriver import Remote
from shareweb.test_case.models.getconfig import get_host
import configparser
from time import sleep
from selenium import webdriver


# 启动浏览器驱动
def browser(browser_name, browser_version):

    name = browser_name
    version = browser_version
    host = get_host()                                                   # 设置运行主机：端口号
    print(host, name)

    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': name,  # 指定浏览器名称
                                          'version': version,
                                          'javascriptEnabled': 'True'})
    return driver


if __name__ == '__main__':
    a = 'Ie'
    b = ''
    dr = browser(a, b)
    dr.maximize_window()
    dr.get("http://www.baidu.com")
    sleep(10)
    dr.quit()
