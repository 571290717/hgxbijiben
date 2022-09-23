# yaml数据驱动案例

## 学习目标

- 掌握如何在项目中使用yaml动态修改数据

### 1.什么是数据驱动

> 将测试脚本中的数据独立出来,单独存放到文件中,便于对数据的管理. 

### 2.测试项目

需求:

1. 进入设置点击搜索按钮
2. 输入搜索内容
3. 点击返回

### 3.完成后目录结构

```python
search_content # 项目
- base
	- __init__.py # 初始化文件
  - base_action.py # 封装的基本操作
  - base_driver.py # 驱动初始化
  - read_data.py # 数据解析文件
- data
	- search_data.yaml
- page
	- search_page.py
-	script
	- test_search.py
- pytest.ini
```

### 4. 代码

#### 4.1 创建data目录,创建search_data.yaml

```yaml
search_test_001:
  input_text: "你好"
search_test_002:
  input_text: "1234"
seearch_test_003:
  input_text: "*&^%"
```

#### 4.2 创建base/read_data.py 解析数据

Read_data.py

```python
import yaml
import os

class ReadData:
    def __int__(self, filename):
        self.path = os.getcwd() + os.sep + "data" + os.sep + filename

    def return_data(self):
        with open(self.path, "r") as f:
            data = yaml.load(f)
            return data
```

Base_action.py

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

Base_driver.py

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

__init__.py

```python
from appium.webdriver.webdriver import By

"""
1.应用的包名和启动名
"""
app_package = 'com.android.settings'
app_activity = ".Settings"

"""
2.搜索
"""
search_button = (By.XPATH, "//*[@content-desc='搜索']")
search_edit_text = (By.CLASS_NAME, "android.widget.EditText")
back_button = (By.CLASS_NAME, "android.widget.ImageButton")
```



#### 4.3 编写测试脚本script/test_search.py

Test_search.py

```python
import base
import pytest
from page.search_page import SearchPage
from base.base_driver import init_driver
from base.read_data import ReadData

def package_param_data():
    """解析数据"""
    yaml_data = ReadData('search_data.yaml').return_data()
    list_data = []
    for i in yaml_data.keys():
        list_data.append((i, yaml_data.get(i).get('input_text')))
    return list_data


class Test_Search:
  '''测试脚本'''
    def setup_class(self):
        self.driver = init_driver(base.app_package, base.base_driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('test_id, input_text', package_param_data())
    def test_search(self, test_id, input_text):
        sp = SearchPage(self.driver)
        # 调用操作类
        # print("test_id:", test_id)
        sp.input_search(input_text)

```

#### 4.4  编写search_page.py

封装的是搜索的功能

```python
import base
from base.base_action import BaseAction


class SearchPage(BaseAction):

    def click_search(self):
        """点击搜索按钮"""
        self.click_element(base.search_button)

    def input_search(self, text):
        """输入搜索内容"""
        self.input_element_content(base.search_edit_text, text)

    def click_back(self):
        self.click_element(base.back_button)

```

#### 4.5 pytest的配置文件

Pytest.ini

```ini
[pytest]
addopts = -s
test_path = ./script
python_files = test_*
python_classes = Test*
python_functions = test_*
```

### 5. 总结

经过实现我们发现很多代码都是重复的,变化的只是要进行测试的功能模块,因此我们可以对此架构进行重复使用,更改的只是测试脚本文件、搜索功能的集体实现.

新增的是数据驱动这一块,后面也可以重复使用.重点要掌握yaml的数据驱动实现.

