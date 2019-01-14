from selenium.webdriver import Remote

"""
运用Grid2实现分布式部署，并且在不同的节点和浏览器上运行
使用了Remote方法实现driver的初始化，即driver是Remote的实例
"""

# 定义主机与浏览器
lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
         'http://127.0.0.1:5555/wd/hud': 'firefox',
         'http://127.0.0.1:5556/wd/hud': 'internet explorer'}

# 通过不同的浏览器执行脚本
for host, browser in lists.items():
    print(host, browser)
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser,
                                          'version': '',
                                          'javascriptEnabled': True
                                          }
                    )

    driver.get("http://www.baidu.com")
    driver.close()
