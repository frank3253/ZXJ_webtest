# coding=utf-8
from selenium.webdriver import Remote
from time import sleep
from selenium import webdriver


# 启动浏览器驱动
def browser():
    name = 'chrome'
    host = '127.0.0.1:4444'                                                     # 设置运行主机：端口号
    print(host, name)
    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': name,                  # 指定浏览器名称
                                          'version': '',
                                          'javascriptEnabled': 'True'})
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.maximize_window()
    dr.get("http://www.baidu.com")
    dr.quit()
