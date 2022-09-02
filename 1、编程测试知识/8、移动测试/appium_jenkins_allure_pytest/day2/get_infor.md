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

