import os


def get_configpath():

    path = str(os.path.dirname(os.path.dirname(__file__)))
    path = path.replace('\\', '/')
    configpath = path.split('/shareweb')[0] + "/config/config.ini"

    return configpath


if __name__ == '__main__':
    print(get_configpath())

