# 接口功能脚本设计

------

## 目标

### 基于Jmeter设计学生信息管理系统-接口功能脚本

------

### 1. 配置元件分析

```
1. HTTP信息头管理器
2. HTTP请求默认值
3. CSV Data Set Config
```

### 2. 请求方法

```
1. 查询使用方法(GET)
2. 新增使用方法(POST)
3. 更新使用方法(PUT)
4. 删除使用方法(DELETE)
```

### 3. 其他

```
1. 参数文件使用Nodepad++ UTF-8无BOM格式
   2. 每个接口为一个线程组,例如：(查询所有、查询指定、新增、更新、删除)
```

### 4. 配置示例图

#### 4.1 信息头管理器设置图：

![信息头](/img/http_header.png)

#### 4.2 HTTP请求默认值设置图：

![http默认值](/img/http_default.png)

#### 4.3 CSV Data Set Config设置图

![csvdata](/img/csvdataset.png)

#### 4.4 HTTP请求设置图：

![http请求](/img/http_request.png)

#### 4.5 nodepad++ UTF-8无BOM格式

![notepad](/img/notepad.png)

#### 4.6 功能脚本示例图：

![脚本](/img/javascript.png)