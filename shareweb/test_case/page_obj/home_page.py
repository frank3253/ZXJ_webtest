# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base import Page
from time import sleep


class Home(Page):
    """
    分享页首页
    """

    url = "/"

    # element
    home_01_header_title = (By.XPATH, "//div[@class='hisee-app-header-title']")  # 演讲标题
    home_02_page_number = (By.XPATH, "//html//li[1]/div[1]/div[1]/div[1]/div[1]/span[1]")  # 页码
    home_03_text_title = (By.XPATH, "//div[@class='text-title']")  # 段标题
    home_04_text_area = (By.XPATH, "//html//li[1]/div[1]/div[1]/div[2]/div[2]/p/span")  # 段文本
    home_05_text_button = (By.XPATH, "//html//li[1]/div[1]/div[1]/div[1]/a[1]")  # 展开按钮
    home_06_browse_button = (By.XPATH, "//a[@class='browse-mode-toggle-button normal-mode']")  # 快速浏览
    home_07_browse_pagenumber = (By.XPATH, "//html//li[3]/div[1]/div[2]")  # 快速浏览页码
    home_08_browse_picture = (By.XPATH, "//html//li[3]/div[1]/div[1]/img[1]")  # 点击快速浏览的图片
    home_09_active_page = (By.XPATH, "//span[@class='picture-index active']")  # 获取焦点的页码
    home_10_audio_button = (By.XPATH, "//button[@class='iflyrec-audio-action-play']")  # 音频播放
    home_11_audio_currentime = (By.XPATH, "//span[@class='iflyrec-audio-time-current']")  # 已播放音频时间
    home_12_in_video = (By.XPATH, "//a[@class='header-video']")  # 进入视频
    home_13_video_button = (By.XPATH, "//button[@class='iflyrec-video-action-play']")  # 视频播放
    home_14_video_currentime = (By.XPATH, "")  # 已播放视频时间
    home_15_out_video = (By.XPATH, "//button[@class='video-exit-action']")  # 退出视频

    def get_header_title(self):
        # 获取演讲标题
        try:
            element = self.find_element(*self.home_01_header_title)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def get_page_number(self):
        # 获取总页码
        try:
            element = self.find_element(*self.home_02_page_number)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def get_text_title(self):
        # 获取段落标题
        try:
            element = self.find_elements(*self.home_03_text_title)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def get_text_area(self):
        # 获取文本
        try:
            element = self.find_element(*self.home_04_text_area)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def click_text_button(self):
        # 点击文本展开按钮
        try:
            element = self.find_element(*self.home_05_text_button)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def click_browse_button(self):
        # 点击快速浏览按钮
        try:
            element = self.find_element(*self.home_06_browse_button)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def get_browse_pagenumber(self):
        # 获取快速浏览页码
        try:
            element = self.find_element(*self.home_07_browse_pagenumber)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def click_browse_picture(self):
        # 点击快速浏览的图片
        try:
            element = self.find_element(*self.home_08_browse_picture)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def get_active_page(self):
        # 获取active状态的页码
        try:
            element = self.find_element(*self.home_09_active_page)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def click_audio_button(self):
        # 点击音频播放
        try:
            element = self.find_element(*self.home_10_audio_button)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def get_audio_currenttime(self):
        # 获取音频播放时间
        try:
            element = self.find_element(*self.home_11_audio_currentime).text
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def click_in_video(self):
        # 点击进入视频播放
        try:
            element = self.find_element(*self.home_12_in_video)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def click_video_button(self):
        # 点击视频播放
        try:
            element = self.find_element(*self.home_13_video_button)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def get_video_currentime(self):
        # 获取视频播放时间
        try:
            element = self.find_element(*self.home_14_video_currentime)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element

    def click_out_video(self):
        # 退出视频播放
        try:
            element = self.find_element(*self.home_15_out_video)
        except NoSuchElementException as msg:
            print("查找元素异常%s" % msg)
        else:
            return element
