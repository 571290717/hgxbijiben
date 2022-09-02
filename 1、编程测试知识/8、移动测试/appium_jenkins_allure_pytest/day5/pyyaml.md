# python解析yaml文件

## 学习目标

- 掌握python对yaml文件的读写操作



### 1. PyYaml库安装

```
PyYAML为python解析yaml的库.
安装：pip3 install -U PyYAML
```

### 2. python对yaml文件的操作

#### 2.1 读取yaml文件

**使用的方法:**

- yaml.load(stream, Loader=Loader)
  - stream 是等待读取的文件对象

准备yanl文件

```yaml
Search_Data:
      search_test_001:
        value: 456
        expect: [4,5,6]
      search_test_002:
        value: "你好"
        expect: {"value":"你好"}
```

python代码

```python
import yaml

with open("./search_page.yaml", "r") as f:
  data = yaml.load(f)
  print(data)

# 执行结果
{'Search_Data': {
          'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'}, 
          'search_test_001': {'expect': [4, 5, 6], 'value': 456}
			}
}
```

#### 2.2 写入文件内容

**使用的方法:**

- yaml.dump(data, stream, **kwds)
  - Data: 等待写入的数据,类型为字典
  - stream: 打开文件对象
  - encodig: utf-8, 设置写入的编码格式
  - allow_unicode: True/False 

准备数据:

```json
{'Search_Data': {
          'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'}, 
          'search_test_001': {'expect': [4, 5, 6], 'value': 456}
			}
}
```

python代码

```python
import yaml

data = {'Search_Data': {
          'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
          'search_test_001': {'expect': [4, 5, 6], 'value': 456}
			}
}

# 要设置编码格式,否则会出现中文乱码
with open('./yaml_hello.yaml', 'w', encoding='utf-8',allow_unicode=True) as f:
    yaml.dump(data, f)

```

执行结果:

```yaml
Search_Data:
  search_test_001:
    expect:
    - 4
    - 5
    - 6
    value: 456
  search_test_002:
    expect:
      value: 你好
    value: 你好  # 设置编码后不出现乱码

```

