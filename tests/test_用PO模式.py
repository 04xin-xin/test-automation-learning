from seleniumbase import BaseCase
from pages.baidu_page import BaiduPage


class TestWithPO(BaseCase):
    def test_搜索(self):
        page = BaiduPage(self)
        page.open()
        page.search("Page Object")
        # 断言结果页加载完成（不一定有 Page Object 文字）
        assert page.is_result_loaded()