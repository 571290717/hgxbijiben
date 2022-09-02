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

