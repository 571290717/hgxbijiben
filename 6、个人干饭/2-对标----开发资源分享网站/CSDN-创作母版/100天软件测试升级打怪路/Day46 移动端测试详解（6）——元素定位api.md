# Day46 移动端测试详解（6）——元素定位api



# 元素定位api

## 学习目标

- 掌握元素定位的基本方法
- 掌握定位一组元素
- 掌握设置等待时间

## 1.app元素定位操作API

#### 1.1定位介绍

```
元素的基本定位基于当前屏幕范围内展示的可见元素
```

#### 1.2 Appium常用定位方式

- 前置代码

  ```
  from appium import webdriver
  # server 启动参数
  desired_caps = {}
  # 设备信息
  desired_caps['platforName'] = 'Android'
  desired_caps['paltformVersion'] = '5.1'
  desired_caps['deviceName'] = '192.168.56.101:5555'
  # app信息
  desired_caps['appPackage'] = 'com.android.settings'
  desired_caps['appActivity'] = '.Settings'
  # 生命driver对象
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
  ```

- id

```
方法：find_element_by_id(id_value) # id_value:为元素的id属性值

需求:
	通过id定位方式点击搜索按钮

举例：
driver.find_element_by_id("com.android.settings:id/search").click()
driver.quit()
```

- class

```
方法：find_element_by_class_name(class_value) # class_value:为元素的class属性值
需求:
	1.进入设置页面
  2.点击搜索按钮
  3.通过class定位方式点击输入框的返回按钮

举例:
driver.find_element_by_id("com.android.settings:id/search").click()
driver.find_element_by_class_name("android.widget.ImageButton").click()
driver.quit()
```

- xpath

```
方法:find_element_by_xpath(xpath_value) # xpath_value:为可以定位到元素的xpath语句

Android端常用属性定位:
1. id ://*[contains(@resource-id,'com.android.settings:id/search')]
2. class ://*[contains(@class,'android.widget.ImageButton')]
3. text ://*[contains(@text,'WLA')]

模糊定位
4. contains(@key,value): value可以是部分值

需求:
	1. 进入设置页面
	2. 点击wlan菜单栏

示例:
driver.find_element_by_xpath("//*[contains(@text,'WLA')]").click()
driver.quit()
```

------

## 2. 定位一组元素

```
应用场景为元素值重复，无法通过元素属性直接定位到某个元素，只能通过elements方式来选择，返回一个定位对象的列表.
```

#### 2.1 通过id定位一组元素

```
方法: find_elements_by_id(id_value) 
需求:
	1. 进入设置页面
	2. 点击wlan菜单栏,id定位对象列表中第2个

title = driver.find_elements_by_id("com.android.settings:id/title")
# 打印title类型，预期为list
print(type(title))
# 取title返回列表中的第一个定位对象，执行点击操作
title[1].click()
```

#### 2.2 通过class定位一组元素

```
方法: find_elements_by_class_name(class_value)
需求:
	1. 进入设置页面
	2. 点击wlan菜单栏,选择定位对象是第3个

title = driver.find_elements_by_class_name("android.widget.TextView")
# 打印title类型，预期为list
print(type(title))
# 取title返回列表中的第3个定位对象,执行点击操作
title[3].click()
```

#### 2.3 通过Xpath定位一组元素

```
方法: find_elements_by_xpath(xpath_value)
需求:
	1. 进入设置页面
	2. 点击wlan菜单栏,xpath中class属性定位列表中第3个对象

data = driver.find_elements_by_xpath("//*[contains(@class,'android.widget.TextView')]")
data[3].click()
```

------

## 3.显示等待

#### 3.1 显示等待介绍

```
在一个超时时间范围内，每隔一段时间去搜索一次元素是否存在，
如果存在返回定位对象，如果不存在直到超时时间到达，报超时异常错误。
```

#### 3.2 显示等待方法

```
方法:WebDriverWait(driver, timeout, poll_frequency).until(method)
参数：
  1.driver：手机驱动对象
  2.timeout：搜索超时时间
  3.poll_frequency：每次搜索间隔时间，默认时间为0.5s
  4.method：定位方法(匿名函数)
使用示例:
WebDriverWait(driver, timeout, poll_frequency).until(lambda x: x.find_elements_by_id(id_value))
解释：
  1.x传入值为：driver，所以才可以使用定位方法.
函数运行过程：
  1.实例化WebDriverWait类，传入driver对象，之后driver对象被赋值给WebDriverWait的一个类变量：self._driver
  2.until为WebDriverWait类的方法，until传入method方法(即匿名函数)，之后method方法会被传入self._driver
  3.搜索到元素后until返回定位对象，没有搜索到函数until返回超时异常错误.
```

示例:

```
try:
    # 查找元素前时间
    print(time.strftime("%H:%M:%S",time.localtime()))
    # 显示等待
    WebDriverWait(driver,15,1).until(lambdax:x.find_element_by_id("com.android.settings:id/search")).click()
except Exception as e:
    # 查找元素后时间
    print(time.strftime("%H:%M:%S",time.localtime()))
```



# app元素信息操作

## 学习目标

- 掌握常用的手机端元素信息的获取及基本的输入操作

### 1.前置代码

```
# 从appium库里面导入driver对象
from appium import webdriver
# server 启动参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
```

### 2. 发送数据到输入框

```
方法:send_keys(vaue) # value：需要发送到输入框内的文本

需求:
	打开设置 点击搜索按钮 输入内容abc

# 点击搜索按钮
driver.find_element_by_id("com.android.settings:id/search").click()
# 定位到输入框并输入abc
driver.find_element_by_id("android:id/search_src_text").send_keys("abc")
```

注: 如果插入中文,需要在desired_caps里面增加2个参数:

```
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 点击搜索按钮
driver.find_element_by_id("com.android.settings:id/search").click()
# 定位到输入框并输入abc
driver.find_element_by_id("android:id/search_src_text").send_keys("传智播客")
```

### 3. 清空输入框内容

```
方法:clear()

需求:
	打开设置 点击搜索按钮  输入内容abc 删除已输入abc

driver.find_element_by_id("com.android.settings:id/search").click()
# 定位到输入框并输⼊abc
input_text = driver.find_element_by_id("android:id/search_src_text")
# 输入abc
input_text.send_keys("abc")
time.sleep(1)
# 删除abc
input_text.clear()
```

### 4. 获取元素的文本内容

```
方法: text

需求: 
	进入设置,获取所有元素class属性为"android.widget.TextView"的文本内容

代码:
text_vlaue = driver.find_elements_by_class_name("android.widget.TextView")
for i in text_vlaue:
		print(i.text)
```

### 5. 获取元素的属性值

```
方法: get_attribute(value) # value:元素的属性
1. value='name' 返回content-desc / text属性值
2. value='text' 返回text的属性值
3. value='className' 返回 class属性值，只有 API=>18 才能支持
4. value='resourceId' 返回 resource-id属性值，只有 API=>18 才能支持

需求:
	进入设置 获取wlan属性

data = driver.find_element_by_id("com.android.settings:id/title")
print(data.get_attribute(‘resourceId’))
```

### 6.  获取元素在屏幕上的坐标

```
方法: location

需求:
	进入设置,获取搜索按钮在屏幕上的坐标位置

#定位搜索按钮
get_value = driver.find_element_by_id("com.android.settings:id/search")
#输出按钮坐标
print(get_value.location)
```

### 7. 获取app包名和启动名

```
获取包名方法: current_package
获取启动名: current_activity

需求:
	启动设置,获取包名和启动名
	
print(driver.current_package)
print(driver.current_activity)
```

