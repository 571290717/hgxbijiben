# Yaml介绍

## 学习目标

- 掌握数据的存储方式
- 了解什么是yaml

### 1. 数据存储方式

在了解数据的存储方式之前我们要先知道什么是数据, **数据就是资源,是一切资源的统称**, 数据有不同表现方式和存储方式, 例如文本类型(txt文件、doc文件)、图片、音视频等都是数据,都有不同的表现形式.

**数据存储方式有下面4种**:

- 内存,包括RAM(运行内存)和ROM(物理硬盘)中.
- 文件, 包括文本文件(word、excel、ppt等等)、xml(标记语言)、html(超文本标记语言)、 json、yaml
- 数据库, 例如mysql、oracle、sqlserver、sqlite等等
- 网络

### 2. Yaml简介

> Yaml 是一种所有编程语言可用的友好的数据序列化标准. 
>
> 其语法和其他高阶语言类似,并且可以简单表达清单、散列表、标量等资料形式.

### 3. yaml语法规则及支持的数据结构

#### 3.1 语法规则

1. 大小写敏感
2. 使用缩进表示层级关系
3. 缩进时不允许使用tab键,只允许使用空格
4. 缩进的空格数目不重要,只要相同层级的元素左侧对齐即可

#### 3.2 支持的数据结构

- **object(对象)**, 键值对的集合,又称为映射/hash/字典
- **array(数组),** 一组按照次序排列的值,又称序列(sequence)、列表
- **scalars(纯量)**, 单个的、不可再分的值, 包括**字符串、布尔值、整数、浮点数、null、日期**

#### 3.3 数据结构的使用

**(1)、对象**

- 值为字符

  ```yaml
  data.yaml
     animal: pets # 注意冒号后面必须要有一个空格
  
  转换为python代码
     {'animal': 'pets'}
  ```

- 值为字典

  ```yaml
  data.yaml
     animal: {"ke1":"pets","key2":"app"} # python字典
  
  转换为python代码
     {animal: {"ke1":"pets","key2":"app"}} # 嵌套字典结构
  ```

**(2)、数组**

- 方式一

  ```yaml
  data.yaml
     animal: 
       - data1
       - data2
  转换为python代码
     {'animal': ['data1', 'data2']}
  ```

- 方式二

  ```yaml
  data.yaml
     animal: ['data1', 'data2'] # python列表
  
  转换为python代码
     {'animal': ['data1', 'data2']} # 字典嵌套列表
  ```

**(3)、纯量**

主要包括: **字符串、布尔值、整数、浮点数、null、日期**

```
# 字符串
data.yaml
     value: "hello"
转换为python代码
     {"value":"hello"}

# 布尔值
data.yaml
     value1: true
     value2: false
转换为python代码
     {'value1': True, 'value2': False}
     
# 整数，浮点数
data.yaml
     value1: 12
     value2: 12.102
# 转换为python代码
     {'value1': 12, 'value2': 12.102}
     
# 空(Null)
data.yaml
     value1: ~ # ~ 表示为空
转换为python代码
     {'value1': None}
     
# 日期
data.yaml
     value1: 2017-10-11 15:12:12
转换为python代码
     {'languages': {'value1': datetime.datetime(2017, 10, 11, 15, 12, 12)}}
```

**(4)、锚点和引用**

> 锚点: 标注一个内容,锚点名称自定义, 标示符号是 **&**
>
> 引用: 被标注的内容. 标示符号好是*****,  使用方式: <<: *锚点名

```
data: &imp   # & 是锚点标示符号
    value: 456
name:
    value1: 123
    <<: *imp # "<<:" 合并到当前位置，"*imp" 引用锚点imp
转换为python代码
    {'data': {'value': 456}, 'name': {'value': 456, 'value1': 123}}
```