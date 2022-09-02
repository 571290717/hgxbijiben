# 常用插件

## 学习目标

- 掌握常用的插件
- 知道查找需要安装插件的方法

### 1. 概述

pytest包含很多插件包,可以根据需求选择安装即可.

[插件列表地址](https://plugincompat.herokuapp.com)

**我们这里只讲解常用的!!**

### 2. 前置条件

```
1.文件路径：
   - Test_App
   - - test_abc.py
   - - pytest.ini
2.pyetst.ini配置文件内容：
[pytest]
# 命令行参数
addopts = -s
# 搜索文件名
python_files = test_*.py
# 搜索的类名
python_classes = Test_*
# 搜索的函数名
python_functions = test_*
```

### 3.常用插件

#### 3.1  pytest测试报告

**作用**: 通过命令行方式，生成xml/html格式的测试报告，存储于用户指定路径。

**安装方式: ** pip install pytest-html

**使用方法:** 

​	命令行格式: pytest —html=存储路径/report.html

**示例代码1 **

```python
import pytest

class Test_ABC:
		def setup_class(self):
      	print("-----> setup_class")
       
    def teardown_class(self):
      	print("----> teardown_class")
        
    def test_a(self):
      	print("----> test_a")
        assert 1
    
    def test_b(self):
      	print("----> test_b")
        assert 0
 
```

**同时更改配置文件**

 -   修改Test_App/pytest.ini文件，添加报告参数，即：addopts = -s --html=./report.html 

     参数解释:

     -  -s是输出程序运行信息
     - —html=./report.ml 在当前目录下生成report.html文件

     ⚠️ 若要生成xml文件，可将--html=./report.html 改成 --html=./report.xml

#### 3.2 Pytest 控制函数执行顺序

默认情况下，pytest是根据测试方法名由小到大执行的,可以通过第三方插件包改变其运行顺序。

**作用:** 以函数修饰符的方式标记被测函数,通过参数控制函数执行顺序

**安装插件:** pip install purest-ordering

**使用方法:**

1. 标记于被测函数, @pytest.mark.run(order=x)
2. 根据order传入参数来决定运行顺序:
   1. order值全为正数或全为负数时, 值越小,优先级越高
   2. 正数和负数同时存在,正数优先级高

**示例代码2**

```python
import pytest


class Test_ABD:
		def setup_class(self):
      	print("-----> setup_class")
       
    def teardown_class(self):
      	print("----> teardown_class")
     
    @pytest.mark.run(order=2)
    def test_a(self):
      	print("----> test_a")
        assert 1
    
    @pytest.mark.run(order=1)
    def test_b(self):
      	print("----> test_b")
        assert 0

if __name__ == "__main__":
  	pytest.main("-s test_abc.py")

执行结果：
        test_abc.py
        ------->setup_class
        ------->test_b # order=1 优先运行
        F
        ------->test_a # order=2 晚于 order=1 运行
        .
        ------->teardown_class
```

### 3.3 失败重试

**插件名称:** pytest-rerunfailures

**作用:** 使用命令行方式,控制失败函数的重试次数.

**安装方式:** pip install purest-rerunfailures

**使用方法:**

​		命令行格式, pytest —rerun  n # n为重试的次数

**示例代码3**

```py
import pytest


class Test_ABD:
		def setup_class(self):
      	print("-----> setup_class")
       
    def teardown_class(self):
      	print("----> teardown_class")
     
    def test_a(self):
      	print("----> test_a")
        assert 1
    
    def test_b(self):
      	print("----> test_b")
        assert 0

if __name__ == "__main__":
  	pytest.main("-s test_abc.py")
```

**修改配置文件** , 修改Test_App/pytest.ini文件，添加失败重试参数，即：addopts = -s  --reruns 2 --html=./report.html 

参数解释:

-  -s是输出程序运行信息
- —rerun 2 : 失败重试2次
- —html=./report.ml 在当前目录下生成report.html文件