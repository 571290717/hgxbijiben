# 抽取基本的操作

### 1. 抽取基本操作原因

我们多次使用app后发现,我们经常的操作是点击、输入内容操作,所以我们也可以把这样的操作进一步抽取.

### 2. 抽取后的目录

```
- base
- - __init__.py
- - base_action.py
- - base_driver.py
- page
- - sms_page.py
- script
- - test_sms_send.py
- pytest.ini
```

### 3. 代码

在base_action.py中增加基本操作

```python
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, loc):
        """点击的基本操作"""
        self.find_element(loc).click()

    def input_element_content(self, loc, content):
        """输入框的基本操作"""
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(content)

    def find_element(self, loc):
        """抽取查找元素的基本动作"""
        self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0], loc[1])


```

修改sms_page.py 代码

```python
import os
import sys
sys.path.append(os.getcwd())
import base
from base.base_action import BaseAction


class SmsPage(BaseAction):
    def __init__(self, driver):
        # self.driver = driver
        # 调用父类的初始化方法
        BaseAction.__init__(self, driver)

    def click_add_sms(self):
        # 2. 定位到新增
        self.click_element(base.sms_add)
        
    def input_phone_number(self):
        '''定位接受者，填写手机号'''
        # 3.定位接收者元素
        self.input_element_content(base.sms_receiver_phone_number, "17611111111")

    def send_sms(self):
        '''发送短信内容'''
        send_list = [11, 'aaa', 'bbbb']
        # 5.定位到发送元素
        send_sms = self.find_element(base.sms_sender_edit_content)
        # 定位发送按钮
        send_btn = self.find_element(base.sms_sender_button)
       
        # 6.遍历发送的信息
        for i in send_list:
            send_sms.clear()
            send_sms.send_keys(i)
            send_btn.click()

```

### 4. 抽取手机号和发送的短信内容

由于每个人发送短信的手机好吗和短信内容也不一样,所以我们把手机号和短信也作为常量,便于修改

**修改base/__init__.py**

```
"""
2. 测试发送短信功能
"""
# 接收的手机号
phone_number = "17612345678"
# 短信内容
messages = [11, 'aaa', 'bbbb']
```

**修改sms_page.py**

```python
import os
import sys
sys.path.append(os.getcwd())
import base
from base.base_action import BaseAction


class SmsPage(BaseAction):
    
    ...
    
    def input_phone_number(self):
        '''定位接受者，填写手机号'''
        # 3.定位接收者元素
        self.input_element_content(base.sms_receiver_phone_number, base.phone_number)

    def send_sms(self):
        '''发送短信内容'''
        # 短信发送的内容
       	send_messages = base.messages
        # 5.定位到发送元素
        send_sms = self.find_element(base.sms_sender_edit_content)
        # 定位发送按钮
        send_btn = self.find_element(base.sms_sender_button)
       
        # 6.遍历发送的信息
        for i in send_messages:
            send_sms.clear()
            send_sms.send_keys(i)
            send_btn.click()
```

## 总结

到此为止我们已经把发送短信的所有功能全部抽取完成,经过抽取我们发现我们的代码文件越来越多,但是维护起来更加容易,也容易扩展,代码的复用率提高了很多.