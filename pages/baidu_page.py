class BaiduPage:
    SEARCH_BOX = "#kw"
    SEARCH_BTN = "#su"

    def __init__(self, sb):
        self.sb = sb

    def open(self):
        self.sb.open("https://www.baidu.com")
        self.sb.sleep(2)

    def search(self, keyword):
        # 用 JS 绕过反爬（直接修改 DOM，不触发 Selenium 检测）
        js_code = (
            "document.querySelector('#kw').value = '" + keyword + "';"
            "document.querySelector('#su').click();"
        )
        self.sb.execute_script(js_code)
        self.sb.sleep(3)

    def is_result_loaded(self):
        try:
            self.sb.wait_for_element("#content_left", timeout=10)
            return True
        except Exception:
            return False