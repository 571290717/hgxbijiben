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