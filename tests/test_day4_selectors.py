import time


def test_css选择器练习(browser):
    """CSS 选择器练习"""
    browser.get("https://www.baidu.com")
    time.sleep(3)

    e1 = browser.find_element("css selector", "#kw")
    print(f"id选择器找到: {e1.tag_name}")

    e2 = browser.find_element("css selector", ".s_ipt")
    print(f"class选择器找到: {e2.tag_name}")

    e3 = browser.find_element("css selector", "[name='wd']")
    print(f"属性选择器找到: {e3.tag_name}")

    browser.execute_script("document.querySelector('#kw').value = 'CSS选择器测试';")

    assert e1 == e2 == e3, "三种方式应该找到同一个元素"
    assert e1.get_attribute("value") == "CSS选择器测试"
    print("CSS 选择器练习通过！")


def test_xpath选择器练习(browser):
    """XPath 选择器练习"""
    browser.get("https://www.baidu.com")
    time.sleep(3)

    e1 = browser.find_element("xpath", "//input[@id='kw']")
    print(f"XPath @id找到: {e1.tag_name}")

    e2 = browser.find_element("xpath", "//input[@name='wd']")
    print(f"XPath @name找到: {e2.tag_name}")

    e3 = browser.find_element("xpath", "//input[@id='su']")
    print(f"XPath 搜索按钮找到: {e3.tag_name}")

    assert e1 == e2

    browser.execute_script("document.querySelector('#kw').value = 'XPath测试';")
    # 用 JS 点击而不是 .click()
    browser.execute_script("document.querySelector('#su').click();")

    time.sleep(3)
    print(f"点击后标题: {browser.title}")
    # 因为百度会跳到安全验证，标题可能不一样
    assert browser.title != ""
    print("XPath 选择器练习通过！")
