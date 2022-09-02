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