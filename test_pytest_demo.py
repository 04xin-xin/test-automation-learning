import time
from selenium.webdriver.edge.service import Service


def test_百度首页能打开():
    from selenium import webdriver
    service = Service(executable_path=r"E:\webdriver\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("https://www.baidu.com")
    assert "百度" in driver.title  # 断言：标题里必须有"百度"
    driver.quit()


def test_搜索框存在():
    from selenium import webdriver
    service=Service(executable_path=r"E:\webdriver\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("https://www.baidu.com")
    time.sleep(3)
    search_box = driver.find_element("id", "kw")  # 找搜索框
    assert search_box is not None  # 断言：搜索框存在
    driver.quit()

def test_加法计算():
    # pytest 也可以测普通代码，不只是 selenium
    assert 1 + 1 == 2
    assert 10 - 5 == 5