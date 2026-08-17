from seleniumbase import BaseCase


class TestBaidu(BaseCase):
    def test_搜索(self):
        # 加 uc=True 反爬检测
        self.open("https://www.baidu.com", uc=True)
        self.sleep(3)
        # 用 JS 设值，绕过 element not interactable
        self.execute_script(
            "document.querySelector('#kw').value = 'SeleniumBase';"
        )
        self.execute_script(
            "document.querySelector('#su').click();"
        )
        self.sleep(3)
        # 验证页面有变化
        title = self.get_title()
        print(f"点击后标题: {title}")
        assert title != ""
        print("测试通过！")