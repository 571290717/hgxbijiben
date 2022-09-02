# Allure

## 学习目标

- 掌握allure的安装和基本使用

### 1. Allure介绍

[Allure](http://allure.qatools.ru/)是一款非常轻量级并且非常灵活的开源测试报告生成框架,  能够生成美观易读的报告，目前支持语言：Java, PHP, Ruby, Python, Scala, C#。它支持绝大多数测试框架， 例如TestNG、Pytest、JUint等。它简单易用，易于集成.



### 2. Pytest框架集成Allure

Pytest是Python的单元测试框架，非常方便和易用,我们已经使用过了,接下来主要介绍如何将测试报告生成工具Allure集成到Pytest中。

#### 2.1 安装Allure Pytest Adaptor

Allure Pytest Adaptor是Pytest的一个插件，通过它我们可以生成Allure所需要的用于生成测试报告的数据。安装[pytest-allure-adaptor](https://pypi.python.org/pypi/pytest-allure-adaptor)插件方法

```shell
pip install pytest-allure-adaptor
```

#### 2.2 Allure Pytest Adaptor使用案例

创建项目allpure_hello,在项目下创建pytest的配置文件

pytest.ini

```ini
[pytest]
; 在执行命令目录生成report文件夹，文件夹下包含xml文件
addopts = -s --alluredir report 
testpaths = ./script
python_files = test_*.py
python_classes = Test_*
python_functions = test_*
```

在项目根目录下创建script/test_allure_report.py 文件

test_allure_report.py

```python
class TestAllure:

    def setup(self):
        print('---> setup')

    def teardown(self):
        print('teardown')

    def test_a(self):
        print('test_a')
        assert 1

    def test_b(self):
        print('test_')
        assert 0

```

执行命令: pytest , 会在项目根目录下生成report文件夹,文件夹下生成xml文件

#### 2.3 xml转html工具安装

xml是可以用浏览器打开,但是并不美观,我们要把它转化为html格式的,需要安装转化工具: allure

- mac版本

  ```
  1.执行命令: brew install allure
  2.进入report上级目录执行命令：allure generate report/ -o report/html
  3.report目录下会生成index.html文件，即为可视化报告
  ```

- windows版本

  ```
  1.下载压缩包allure-2.5.0.zip
  2.解压
  3.将压缩包内的bin目录配置到path系统环境变量
  4.进入report上级目录执行命令：allure generate report/ -o report/html
  5.report目录下会生成index.html文件，即为可视化报告
  ```

