import time


def test_css选择器练习(browser):
    """CSS 选择器练习"""
    browser.get("https://www.baidu.com")
    time.sleep(2)
    # 用 JS 绕过反爬，直接用 JS 注入关键词
    browser.execute_script(
        "document.querySelector('#kw').value = 'selenium';"
    )
    time.sleep(2)
    # 验证关键词被填入
    js = "return document.querySelector('#kw').value;"
    value = browser.execute_script(js)
    assert "selenium" in value

def test_xpath选择器练习(browser):
    """XPath 选择器练习"""
    browser.get("https://www.baidu.com")
    time.sleep(2)
    # 用 JS 绕过反爬
    browser.execute_script(
        "document.querySelector('#kw').value = 'pytest';"
    )
    time.sleep(2)
    # 用 JS 验证
    js = "return document.querySelector('#kw').value;"
    value = browser.execute_script(js)
    assert "pytest" in value