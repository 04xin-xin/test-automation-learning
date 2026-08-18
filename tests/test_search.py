import time


def test_搜索框能输入文字(browser):
    browser.get("https://www.baidu.com")
    time.sleep(3)
    browser.execute_script("document.querySelector('#kw').value = 'Selenium';")
    value = browser.execute_script("return document.querySelector('#kw').value;")
    assert value == "Selenium"


def test_点击搜索按钮(browser):
    browser.get("https://www.baidu.com")
    time.sleep(3)
    browser.execute_script("document.querySelector('#kw').value = 'pytest';")
    browser.execute_script("document.querySelector('#su').click();")
    time.sleep(20)
    title = browser.driver.title
    assert "pytest" in title, f"期望标题包含 pytest，实际为 {title}"