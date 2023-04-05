from web_test_data import test_data
from selenium import webdriver
# 初始化一个会话
driver = webdriver.Chrome()
# 隐士等待10s
driver.implicitly_wait(10)
# 获取测试数据中的信息，并赋值给新的变量
url = test_data.url["url"]
username = test_data.login_data[0]["username"]
password = test_data.login_data[1]["password"]
search_word = test_data.search_word["search_word"]

result = webAutoTesting.search(url, username, password, driver, search_word)

if search_word in result:
    print("案例通过")
else:
    print("案例不通过")

