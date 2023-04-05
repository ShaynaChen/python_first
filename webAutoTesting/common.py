"""
web自动化：
代码        翻译        浏览器
Python------驱动--------Chrome
谷歌浏览器驱动：https://registry.npmmirror.com/binary.html?path=chromedriver/
驱动版本和浏览器版本兼容
下载好驱动，将驱动解压放在Python的安装目录下（放在系统下即可）
第三方库：用pip安装
1、安装selenium
pip install selenium
2、导入
import
import selenium -- 将工具中的内容都导入进来
from……import……
from selenium import webserver          -- 从selenium导入webdriver库
from selenium.webserver import Chrome
3、卸载
pip uninstall selenium
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()  # 初始化driver，与浏览器进行沟通，建立会话
# # 打开网页
# driver.get("http://erp.lemfix.com/login.html")
# # 窗口最大会
# driver.maximize_window()
# time.sleep(3)
# # 打开新的网页
# driver.get("https://www.baidu.com/")
# time.sleep(3)
# # 后退
# driver.back()
# time.sleep(3)
# # 前进
# driver.forward()
# time.sleep(3)
# # 刷新
# driver.refresh()
# time.sleep(3)
# driver.find_element(By.ID, 'username').send_keys('test123')
# driver.find_element(By.ID, 'password').send_keys('123456')
# driver.find_element(By.XPATH, "//input[@id='rememberUserCode']/following-sibling::ins").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@id='rememberMe']/following-sibling::ins").click()
# time.sleep(2)

# 定义登录函数
def login_page(url, username, password, driver):
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, "btnSubmit").click()


# 定义搜索函数
def search(url, username, password, driver, search_word):
    login_page(url, username, password, driver)
    driver.find_element(By.XPATH, "//span[text()='零售出库']").click()
    li_id = driver.find_element(By.XPATH, "//div[text()='零售出库']/..").get_attribute("id")
    frame_id = li_id + "-frame"
    driver.find_element(By.ID, frame_id)
    # 通过frame_id切换iframe
    # driver.switch_to.frame(frame_id)
    # 通过xpath定位切换iframe
    # driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id = "{}"]'.format(frame_id)))
    # 通过iframe的下标来切换
    driver.switch_to.frame(1)
    driver.find_element(By.ID, "searchNumber").send_keys(search_word)
    driver.find_element(By.ID, "searchBtn").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, "//tr[@id = 'datagrid-row-r1-2-0']//td[@field = 'number']//div").text
    # 返回值
    return result
