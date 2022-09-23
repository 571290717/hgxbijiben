# 前提准备

### 1. 需求

- 给指定手机号发送三条短信

### 2. 准备目录

```py
- script
-- test_sms_sending.py
- pytest.ini
```

### 3. 代码

**test_sems_sending.py**

```py
import pytest
from appium import webdriver


"""
业务流程分析：
1.启动短信应用
2.定位到新增按钮
3.定位接收者元素
4.涉及到输入框的先clear 在输入
5.定义三条信息
6.定位到发送元素
7.遍历发送的信息
8.关闭app driver对象不会关闭
9.关闭驱动对象

"""

class TestSmsSending:
    def setup(self):
        desired_caps = dict()
        # 测试设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app信息
        desired_caps['appPackage'] = 'com.android.mms'
        desired_caps['appActivity'] = '.ui.ConversationList'

        # 驱动信息
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_sms(self):
        # 2. 定位到新增
        self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()
        # 3.定位接收者元素
        receive_number = self.driver.find_element_by_id("com.android.mms:id/recipients_editor")
        # 4.涉及到输入框的先clear 在输入
        receive_number.clear()
        receive_number.send_keys("17611111111")
        send_list = [11, 'aaa', 'bbbb']
        # 5.定位到发送元素
        send_sms = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        send_btn = self.driver.find_element_by_id("com.android.mms:id/send_button_sms")
        # 6.遍历发送的信息
        for i in send_list:
            send_sms.clear()
            send_sms.send_keys(i)
            send_btn.click()
        # 关闭app driver对象不会关闭
        self.driver.close_app()

```

**pytest.ini**

```
[pytest]
addopts = -s
# 测试环境
testpaths = ./script
#测试文件
python_files = test_*
# 测试的类
python_classes = Test*
# 测试的函数
python_functions = test_*
```

