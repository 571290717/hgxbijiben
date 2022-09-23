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

