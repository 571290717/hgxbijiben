# Day48 移动端测试详解（8）——Pytest





## 学习目标

- 掌握pytest使用
- 掌握pytest测试报告的生成
- 掌握pytest函数执行顺序
- 掌握pytest函数参数化





## 1、Pytest安装和介绍

### 1.1 Pytest介绍

```
pytest是python的一种单元测试框架，同自带的Unittest测试框架类似，相比于Unittest框架使用起来更简洁,效率更高.
```

### 1.2 Pytest特点

```
1.非常容易上手,入门简单,文档丰富，文档中有很多实例可以参考
2.支持简单的单元测试和复杂的功能测试.
3.支持参数化.
4.执行测试过程中可以将某些测试跳过，或者对某些预期失败的Case标记成失败
5.支持重复执行失败的Case.
6.支持运行由Nose,Unittest编写的测试Case
7.具有很多第三方插件,并且可以自定义扩展
8.方便的和持续集成工具集成.
```

### 1.3 Pytest安装

```
安装命令: pip install -U pytest
参数解释:   
	-U 是upgrade, 表示已安装就升级为最新版本.

安装成功校验: pytest --version # 会展示当前已安装版本
```

## 2、pytest第一个例子

```
# 创建文件: test_abc.py

import pytest

def test_a():
	print("---->test_a")
	# 断言成功
	assert 1 
	
def test_b():
	print("---->test_b")
	# 断言失败
	assert 0


if __name__ == "__main__":
	pytest.main("-s. test_abc.py")
	
	
执行结果:
				test_abc.py 
        ------->test_a
        . # .(代表成功)
        ------->test_b
        F # F(代表失败)
```

## 3、运行方式

### 3.1 测试类主函数模式

```
pytest.main("-s test_abc.py")
```

### 3.2 命令行模式

```
pytest。文件路径/测试文件名

例如: pytest ./test_abc.py
```

# setup和teardown函数

## 学习目标

- 能够区分setup和teardown函数在函数级别和类级别的不同

### 1. 概述

```
1. setup和teardown函数主要分为:模块级、类级、功能级、函数级别、
2. 存在于测试类内部
```

### 2. 函数级别的setup和teardown函数

**特点:**

>  当是函数级别的时候,运行测试方法的始末,即运行一次测试函数运行一次setup和teardown.

```
import pytest


class Test_ABC:
		def setup(self):
			print("-----> setup_method")
		
		def teardown(self):
			print("----> teardown_method")
			
		def test_a(self):
			print("----> test_a")
			assert 1
		
		def test_b(self):
			print("----> test_b")

if __name__ == "__main__":
		pytest.main("-s test02.py")
```

执行结果

```
test_abc.py 
------->setup_method # 第一次 setup()
------->test_a
.
------->teardown_method # 第一次 teardown()
------->setup_method # 第二次 setup()
------->test_b
.
------->teardown_method # 第二次 teardown()
```



### 3. 类级别

**特点:**

> 运行于测试类的始末,即:在一个测试内只运行一次setup_class和teardown_class，不关心测试类 内有多少个测试函数.

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

        
if __name == "__main__":
  	pytest.main("-s test_abc.py")
      	
```

执行结果

```
test_abc.py 
------->setup_class # 第一次 setup_class()
------->test_a
.
------->test_b
F 
------->teardown_class # 第一次 teardown_class()
```

## 1. pytest配置文件

pytest的配置文件通常放在测试目录下，名称为pytest.ini，命令运行时会使用该配置文件中的配置

- 配置pytest命令行运行参数

```
[pytest]
addopts = -s ... # 空格分隔，可添加多个命令行参数 -所有参数均为插件包的参数
```

- 配置测试搜索的路径

```
[pytest]
testpaths = ./scripts # 当前目录下的scrip文件夹  可自定义
```

- 配置测试搜索的文件名

```
[pytest]
python_files = test_*.py
# 当前目录下的scripts文件夹下，以test_开头，以.py结尾的所有文件 -可自定义
```

- 配置测试搜索的测试类名

```
[pytest]
python_classes = Test_*
# 当前目录下的scripts文件夹下，以test_开头，以.py结尾的所有文件中，以Test_开头的类
```

- 配置测试搜索的测试函数名

```
[pytest]
python_functions = test_*
# 当前目录下的scripts文件夹下，以test_开头，以.py结尾的所有文件中，以Test_开头的类内，以test_开头的⽅法 -可自定义
```





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

 - 修改Test_App/pytest.ini文件，添加报告参数，即：addopts = -s --html=./report.html 

   参数解释:

   -  -s是输出程序运行信息
   -  —html=./report.ml 在当前目录下生成report.html文件

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
-  —rerun 2 : 失败重试2次
-  —html=./report.ml 在当前目录下生成report.html文件







# pytest提高--fixture

## 学习目标

- 掌握fixture的作用
- 掌握fixture的使用方法

------

### 1. 简介

fixture是pytest特有的功能，它用pytest.fixture标识，以**装饰器形式定义在函数上面**,在编写测试函数的时候，可以将此函数名称做为传入参数，pytest将会以依赖注入方式，将该函数的返回值作为测试函数的传入参数.

fixture有明确的名字，在其他函数，模块，类或整个工程调用它时会被激活。

fixture是基于模块来执行的，每个fixture的名字就可以触发一个fixture的函数，它自身也可以调用其他的fixture.

我们可以把fixture看做是资源，在你的测试用例执行之前需要去配置这些资源，执行完后需要去释放资源。比如module类型的fixture，适合于那些许多测试用例都只需要执行一次的操作。

fixture还提供了参数化功能，根据配置和不同组件来选择不同的参数。

### 2. fixture函数的作用

fixture修饰器来标记固定的工厂函数,在其他函数，模块，类或整个工程调用它时会被激活并优先执行,**通常会被用于完成预置处理和重复操作**。

例如,

- 在测试网站的功能时，每个测试用例都要登录和退出，利用fixture就可以只做一次，否则每个测试用例都要做这两步也是冗余。
- 完成setup和teardown操作,处理数据库或文件的打开、关闭操作
- 准备测试数据.将数据提前写入数据库或通过params返回给测试用例

### 3. 使用方法

```
pytest.fixture(scope='function', params=None, autouse=False, ids=None, name=None)

常用参数解释:
-	scope: 被标记方法的作用域;
		"function": 默认值,表示每个测试方法都要执行一次
		"class": 作用于整个类, 表示每个类的所有测试方法只运行一次
		"module": 作用于整个模块, 每个module的所有测试方法只运行一次.
		"session": 作用于整个session, 每次session只运行一次. ⚠️(此方法慎用!!)
		
- params: list类型,默认None, 接收参数值,对于param里面的每个值，fixture都会去遍历执行一次.
- autouse: 是否自动运行,默认为false, 为true时此session中的所有测试函数都会调用fixture

⚠️ 以上的所有参数也可以不传
```

### 4. 使用案例

#### 4.1 基本使用--作为参数应用

```python
import pytest

@pytest.fixture()
def before():
  print("-----> 在每个函数前执行")
 

def test_1(before):
  print('-----> test_1')
  assert 1
  
def test_2(before):
  print("----> test_2")
  assert 0

if __name__ == "__main__":
  pytest.main("-s test_1.py")	
```

#### 4.2 基本使用--作为函数应用

```python
import pytest

@pytest.fixture()
def before():
    print('\nbefore each test')

@pytest.mark.usefixtures("before")
def test_1():
    print('--->test_1')

@pytest.mark.usefixtures("before")
def test_2(before):
  print("----> test_2")


@pytest.mark.usefixtures("before")
class Test2:
    def test_5(self):
        print('test_5')

    def test_6(self):
        print('test_6')

if __name__ == "__main__":
    pytest.main("-s test_1.py")
```

基本使用中我们发现结果基本是类似的,都是在每个测试函数前被调用执行.

#### 4.3 带参数使用—设置为默认启动形式

**设置true,是自动运行, 代表这个session的所有测试函数都会调用**

```
import pytest

@pytest.fixture(autouse=True)
def before():
    print('\nbefore each test')


class Test2:
    def test_5(self):
        print('test_5')

    def test_6(self):
        print('test_6')

if __name__ == "__main__":
    pytest.main("-s test_1.py")
```

#### 4.4 带参数使用—设置作用域为function

**设置为function,  表示每个测试方法都要执行一次**

```
import pytest

@pytest.fixture(scope="function", autouse=True)
def before():
    print('\nbefore each test')

class Test2:
    def test_5(self):
        print('test_5')

    def test_6(self):
        print('test_6')

if __name__ == "__main__":
    pytest.main("-s test_1.py")
```

#### 4.5 带参数使用— 设置作用域为class

**作用于整个类, 表示每个类的所有测试方法只运行一次**

```
import pytest


@pytest.fixture(scope="class", autouse=True)
def before():
    print('\nbefore each test')


@pytest.mark.usefixtures("before")
def test_1():
    print('--->test_1')

class Test2:
    def test_5(self):
        print('test_5')

    def test_6(self):
        print('test_6')

if __name__ == "__main__":
    pytest.main("-s test_1.py")
```

#### 4.6 带参数使用— 设置作用域为module

**作用于整个模块, 表示这个模块的只运行一次fixture**, 例如所有的test都需要连接同一个数据库,可以使用此方法,对于此模块的所有test都有效

```
import pytest


@pytest.fixture(scope="module", autouse=True)
def before():
    print('\nbefore each test')


@pytest.mark.usefixtures("before")
def test_1():
    print('--->test_1')

class Test2:
    def test_5(self):
        print('test_5')

    def test_6(self):
        print('test_6')

if __name__ == "__main__":
    pytest.main("-s test_1.py")
```

#### 4.7 带参数使用— fixture 返回值

默认为none, 传入list类型参数, fixture会遍历调用list中每个元素.

```
import pytest

@pytest.fixture(params=[1, 2, 3])
def need_data(request): # 传入参数request 系统封装参数
      return request.param # 取列表中单个值，默认的取值方式

class Test_ABC:
    def test_a(self,need_data):
        print("test_a 的值是 %s" % need_data)
        assert need_data != 3 # 断言need_data不等于3

if __name__ == '__main__':
    pytest.main("-s  test_abc.py")
```

### 5. 总结

使用fixture我们可以把一些重复的操作进行简化或者提前处理,来提升代码的效率.使用方式有很多要灵活使用.





# Pytest 提高2

## 学习目标

- 掌握如何进行函数数据参数化

### 1. 跳过测试函数

**使用场景:** 根据特定条件、不执行标识的测试函数

**方法:**

skipif(condition, reason=None)

参数解释:

- condition: 跳过的条件,必传参数
- reason: 标注原因,必传参数

**使用方法:**

```
@pytest.mark.skipif(condition, reason='xxx')
```

**代码示例**

```python
import pytest

class Test_ABC:
    def setup_class(self):
        print("\nsetup")

    def teardown_class(self):
        print("\nteardown")

    def test_a(self):
        print("test_a")

    @pytest.mark.skipif(condition=2>1, reason="跳过")
    def test_b(self):
        print("test_b")
        assert 0
执行结果:
collected 2 items                                                                                                     

test_2.py 
setup
test_a
.s   # 代表跳过不执行
teardown

```

### 2. 标记为预期失败函数

**使用场景:** 标记某测试函数会失败

**方法:**

```
xfail(condition=None, reason=None, raises=None, run=True, strict=False)
常用参数：
   condition：预期失败的条件，必传参数
   reason：失败的原因，必传参数
```

**使用方法:**

```py
@pytest.mark.xfail(condition, reason="xxx")
```

**代码示例**

```python
import pytest

class Test_ABC:
    def setup_class(self):
        print("\nsetup")

    def teardown_class(self):
        print("\nteardown")

    def test_a(self):
        print("test_a")

    @pytest.mark.xfail(condition=2>1, reason="预期失败")
    def test_b(self):
        print("test_b")
        assert 0
        
# 执行结果
collected 2 items                                                                                                     

test_2.py 
setup
test_a
.test_b
x  # 代表预期失败
teardown

```

### 3. 函数数据参数化

**作用:** 方便测试函数对测试属性的获取

**方法:**

```
parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)
常用参数：
argnames：参数名
argvalues：
- 参数对应值，类型必须为list
- 当参数为一个时,参数格式：[value]
- 当参数个数大于一个时，格式为:[(param_value1,param_value2.....),(param_value1,param_value2.....)]
```

**使用方法:**

```
@pytest.mark.parametrize(argnames,argvalues)
⚠️ 参数值为N个，测试方法就会运行N次
```

**示例代码**

```python
import pytest

class Test_ABC:
    def setup_class(self):
        print("setup")

    def teardown_class(self):
        print("teardown")

    def test_a(self):
        print("test_a")

    @pytest.mark.parametrize("a", [3,6])
    def test_b(self, a):
        print("test data:a=%d" % a)
        assert a%3 == 0
        
# 执行结果
test_2.py setup
test_a
.
test data:a=3
.
test data:a=6
.
teardown

```

