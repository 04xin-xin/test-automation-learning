# 第一个自动化测试
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

service = Service(executable_path=r"E:\webdriver\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.maximize_window()  # 最大化窗口，避免元素被裁掉

time.sleep(2)
driver.get("https://www.baidu.com")
time.sleep(3)  # 等页面加载完

# 用 JS 注入值（绕过遮挡问题）
search_box = driver.find_element("id", "kw")
driver.execute_script(
    "arguments[0].value = arguments[1];"
    "arguments[0].dispatchEvent(new Event('input'));"
    "arguments[0].dispatchEvent(new Event('change'));",
    search_box, "软件测试"
)

time.sleep(1)
driver.execute_script("document.getElementById('su').click();")
time.sleep(3)
driver.quit()