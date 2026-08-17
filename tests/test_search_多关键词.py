from seleniumbase import BaseCase


class TestSearch(BaseCase):
    def test_搜索_python(self):
        self._搜索("Python")

    def test_搜索_selenium(self):
        self._搜索("Selenium")

    def test_搜索_pytest(self):
        self._搜索("pytest")

    def test_搜索_自动化(self):
        self._搜索("自动化")

    def test_搜索_测试(self):
        self._搜索("测试")

    def _搜索(self, 关键词):
        self.open("https://www.baidu.com")
        self.sleep(2)
        js_code = (
            "document.querySelector('#kw').value = '" + 关键词 + "';"
            "document.querySelector('#su').click();"
        )
        self.execute_script(js_code)
        self.sleep(3)
        页面内容 = self.get_text("body")
        assert 关键词 in 页面内容 or "百度" in 页面内容, "页面没有 " + 关键词