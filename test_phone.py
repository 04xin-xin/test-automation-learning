


def check_phone(phone):
    """验证手机号：必须是 11 位数字，不能为空"""
    if not phone: # 空
        return "请输入手机号"
    if len(phone) != 11:                # 长度不对
        return "手机号格式错误"
    if not phone.isdigit():             # 非数字
        return "手机号格式错误"
    return "发送验证码成功"


# 等价类划分测试：每类至少 1 个代表
def test_正确手机号():
    """有效等价类：合法的11 位手机号"""
    assert check_phone("13812345678") == "发送验证码成功"


def test_手机号为空():
    """无效等价类（空）"""
    assert check_phone("") == "请输入手机号"


def test_手机号少一位():
    """无效等价类（长度）"""
    assert check_phone("1381234567") == "手机号格式错误"


def test_手机号多一位():
    """无效等价类（长度）"""
    assert check_phone("138123456789") == "手机号格式错误"


def test_非数字字符():
    """无效等价类（类型）"""
    assert check_phone("abcdefghijk") == "手机号格式错误"


def test_手机号只有一位():
    """无效等价类（只有一位）"""
    assert check_phone("1")=="手机号格式错误"

def test_全是空格():
    """无效等价类（都是空格）"""
    assert check_phone(("         "))=="手机号格式错误"


def test_有小数点():
    """无效等价类（有小数点）"""
    assert check_phone("130.1234.5678")=="手机号格式错误"