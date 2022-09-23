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

