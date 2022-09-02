# 抽取find_element

### 1.抽取find_element的原因

我们发现查找元素都是使用的是find_element_by_xxx()这一类的方法,我们通过查看源码可知道,此类方法都是调用的额find_element()函数, 所以我们可以使用此实现方法.

但是,我们只是换了一种实现方法而已,我们可以在此基础上进一步抽取出find_element()的通用方法, 对于要查找的具体方法我们可以调用通用方法实现.

**find_element_by_id的源码*

```python
   def find_element_by_id(self, id_):
        """Finds an element by id.

        :Args:
         - id\_ - The id of the element to be found.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_id('foo')
        """
        return self.find_element(by=By.ID, value=id_)

    def find_elements_by_id(self, id_):
        """
        Finds multiple elements by id.

        :Args:
         - id\_ - The id of the elements to be found.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_id('foo')
        """
        return self.find_elements(by=By.ID, value=id_)
```

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

base_action.py

```python
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
        """抽取查找元素的基本动作"""
        return self.driver.find_element(loc[0], loc[1])

```

**注意事项:** 假如find_element找不到相应的元素,我们可以添加等待时间,让操作变的慢一些,这样更能模拟人的行为操作

在init.py中增加代码

```
"""
2. 测试发送短信功能
"""
sms_add = (By.ID, "com.android.mms:id/action_compose_new")
sms_receiver_phone_number = (By.ID, "com.android.mms:id/recipients_editor")
sms_sender_edit_content = (By.ID, "com.android.mms:id/embedded_text_editor")
sms_sender_button = (By.ID, "com.android.mms:id/send_button_sms")
```

更改sms_page.py 中关于查找元素部分的代码

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
        self.find_element(base.sms_add)
        # self.driver.find_element(base.sms_add[0], base.sms_add[1]).click()

        # self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()

    def input_phone_number(self):
        '''定位接受者，填写手机号'''
        # 3.定位接收者元素
        receive_number = self.find_element(base.sms_receiver_phone_number)
        # receive_number = self.driver.find_element(base.sms_receiver_phone_number[0], base.sms_receiver_phone_number[1])
        # receive_number = self.driver.find_element_by_id("com.android.mms:id/recipients_editor")
        # 4.涉及到输入框的先clear 在输入
        receive_number.clear()
        receive_number.send_keys("17611111111")
        

    def send_sms(self):
        '''发送短信内容'''
        send_list = [11, 'aaa', 'bbbb']
        # 5.定位到发送元素
        send_sms = self.find_element(base.sms_sender_edit_content)
        # send_sms = self.driver.find_element(base.sms_sender_edit_content[0], base.sms_sender_edit_content[1])
        # send_sms = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        send_btn = self.find_element(base.sms_sender_button)
        # send_btn = self.driver.find_element(base.sms_sender_button[0], base.sms_sender_button[1])
        # send_btn = self.driver.find_element_by_id("com.android.mms:id/send_button_sms")
        # 6.遍历发送的信息
        for i in send_list:
            send_sms.clear()
            send_sms.send_keys(i)
            send_btn.click()

```

