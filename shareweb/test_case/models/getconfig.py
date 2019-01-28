# coding=utf-8
import os
import configparser


# =========================获取配置文件路径============================
def get_configpath():

    path = str(os.path.dirname(os.path.dirname(__file__)))
    path = path.replace('\\', '/')
    configpath = path.split('/shareweb')[0] + "/config/config.ini"
    return configpath


# =========================加载配置文件============================
def get_cf():
    cf = configparser.ConfigParser()
    path = get_configpath()
    cf.read(path)
    cf.sections()
    return cf


# =========================创建配置项调用的方法============================
def get_browser_type():
    """获取所有浏览器类型"""
    cf = get_cf()
    browser_type = cf.get('browser', 'browser_type')        # 返回一个str
    return eval(browser_type)               # 将browser_type转成字典


def get_browser_name():
    """获取当前进程测试浏览器名称"""
    cf = get_cf()
    browser_name = cf.get('browser', 'browser_name')
    return browser_name


def set_browser_name(name):
    """设置当前进程测试浏览器名称"""
    cf = get_cf()
    path = get_configpath()
    cf.set('browser', 'browser_name', name)
    cf.write(open(path, 'w'))


def get_browser_version():
    """获取当前进程测试浏览器版本"""
    cf = get_cf()
    browser_version = cf.get('browser', 'browser_version')
    return browser_version


def set_browser_version(version):
    """设置当前进程测试浏览器版本"""
    cf = get_cf()
    path = get_configpath()
    cf.set('browser', 'browser_version', version)
    cf.write(open(path, 'w'))


def get_host():
    """获取selenium服务器地址"""
    cf = get_cf()
    host = cf.get('selenium_hub', 'host')
    return host


def get_mail():
    """获取邮箱配置下的键值对"""
    cf = get_cf()
    cf = cf.items('mail')
    return cf


if __name__ == '__main__':
    # test_browser_type = get_browser_type()
    # for i, j in test_browser_type.items():
    #     print(i, j)
    print(get_mail()[4])
