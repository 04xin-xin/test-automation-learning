import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

from test_baidu import service


@pytest.fixture
def browser():
    service=Service(executable_path=r"E:\webdriver\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    yield driver  # 测试函数用完这个 driver
    driver.quit()  # 自动关闭

def test_百度首页(browser):
    browser.get("https://www.baidu.com")
    assert "百度" in browser.title

def test_搜索框存在(browser):
    browser.get("https://www.baidu.com")
    assert browser.find_element("id", "kw") is not None


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (10, 20, 30),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert a + b == expected