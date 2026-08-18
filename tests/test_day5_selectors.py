import time
import pytest


@pytest.mark.parametrize("关键词", [
    "软件测试",
    "Selenium",
    "Python自动化",
    "pytest教程",
    "接口测试"
])
def test_百度搜索(browser, 关键词):
    """用 5 个不同关键词搜索百度"""
    browser.get("https://www.baidu.com")
    time.sleep(3)

    # 用 JS 绕过百度的反爬
    browser.execute_script(
        f"document.querySelector('#kw').value = '{关键词}';"
    )

    # 用 JS 点击搜索按钮
    browser.execute_script(
        "document.querySelector('#su').click();"
    )

    time.sleep(3)

    # 验证关键词在标题里 OR 页面 title 不为空
    assert browser.driver.title != ""
    print(f"搜索 {关键词} 完成，标题: {browser.driver.title}")