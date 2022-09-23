# 按照业务逻辑抽取代码

## 学习目标

- 能够按照功能进行代码的抽取

### 1. 抽取后的目录

```
- base
- - __init__.py
- - base_driver.py
- page
- - sms_page.py
- script
- - test_sms_send.py
- pytest.ini
```

### 2. 代码

代码的抽取一般先抽取业务功能代码,其次再抽取业务功能中用到的信息.

#### 2.1 抽取功能代码

创建**page(名字是默认的,不要变化)**目录,在目录中创建sms_page文件,把新增短信、输入用户手机号、发送短信功能进行抽取

```pyth
class SmsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_sms(self):
        # 2. 定位到新增
        self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()

    def input_phone_number(self):
        '''定位接受者，填写手机号'''
        # 3.定位接收者元素
        receive_number = self.driver.find_element_by_id("com.android.mms:id/recipients_editor")
        # 4.涉及到输入框的先clear 在输入
        receive_number.clear()
        receive_number.send_keys("17611111111")

    def send_sms(self):
        '''发送短信内容'''
        send_list = [11, 'aaa', 'bbbb']
        # 5.定位到发送元素
        send_sms = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        send_btn = self.driver.find_element_by_id("com.android.mms:id/send_button_sms")
        # 6.遍历发送的信息
        for i in send_list:
            send_sms.clear()
            send_sms.send_keys(i)
            send_btn.click()
```

**修改test_sms_send.py**

```python
from page.sms_page import SmsPage

class TestSmsSending:
  ...
  def setup(self):
    ...
    # 增加
    self.sms_page = SmsPage(self.driver)
    
  ...
  
	def test_sms(self):
        # 点击新增按钮
        self.sms_page.click_add_sms()
        # 点击输入框输入手机号
        self.sms_page.input_phone_number()
        # 发送短信
        self.sms_page.send_sms()
```

#### 2.2 抽取前置代码

由于设备和应用的基本信息不发生变化,我们也可以进行抽取, 同时把药进行测试的应用名进行变量化,便于后期维护.

**新建base包**, 在包里创建base_driver.py文件

```python
from appium import webdriver


def init_driver(app_package, app_activity):
    desired_caps = dict()
    # 测试设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = app_package # 抽取为常量
    desired_caps['appActivity'] = app_activity # 抽取为常量

    # 返回驱动对象
    return  webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

```

在__init__.py文件中定义用到的常量和要测试的功能

```python
"""
1.应用的包名和启动名
"""
app_package = 'com.android.mms'
app_activity = ".ui.ConversationList"
```

*修改script/test_sms_send.py*的代码

```python
from base.base_driver import init_driver

class TestSmsSending:

    def setup(self):
        # 更改driver的代码
        self.driver = init_driver(base.app_package, base.app_activity)
        
    ... 
```





