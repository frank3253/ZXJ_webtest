from selenium import webdriver
import os


# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(6)
    driver.get("https://www.baidu.com")
    time.sleep(1)
    insert_img(driver, "1111.png")

