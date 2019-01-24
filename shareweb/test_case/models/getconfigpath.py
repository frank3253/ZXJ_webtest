import os


def getConfigPath():

    path = str(os.path.dirname(os.path.dirname(__file__)))
    path = path.replace('\\', '/')
    path = path.split('/shareweb')[0] + "/config/config.ini"

    return path


if __name__ == '__main__':
    print(getConfigPath())
