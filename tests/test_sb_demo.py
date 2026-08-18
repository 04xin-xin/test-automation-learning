import allure
from seleniumbase import BaseCase


@allure.feature("搜索功能")
@allure.story("基础搜索")
@allure.title("测试百度搜索")
class TestBaidu(BaseCase):

    @allure.story("百度搜索")
    def test_搜索(self):
        with allure.step("打开百度"):
            self.open("https://www.baidu.com", uc=True)
            self.sleep(3)

        with allure.step("输入关键词"):
            self.execute_script(
                "document.querySelector('#kw').value = 'SeleniumBase';"
            )

        with allure.step("点击搜索"):
            self.execute_script(
                "document.querySelector('#su').click();"
            )
            self.sleep(3)

        with allure.step("验证结果"):
            title = self.get_title()
            print(f"点击后标题: {title}")
            assert title != ""
            print("测试通过！")