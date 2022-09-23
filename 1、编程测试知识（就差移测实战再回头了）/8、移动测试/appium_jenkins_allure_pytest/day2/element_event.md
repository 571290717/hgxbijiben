# 元素事件操作

## 学习目标

- 掌握常用的事件操作

### 1. 前置代码

```
from appium import webdriver
# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
```

### 2. swip滑动事件

从一个坐标位置滑动到另⼀个坐标位置,是两个点之间的滑动.

```
方法: swipe(start_x, start_y, end_x, end_y, duration=None)
参数解释:
1.start_x：起点X轴坐标
2.start_y：起点Y轴坐标
3.end_x： 终点X轴坐标
4.end_y,： 终点Y轴坐标
5.duration： 滑动这个操作一共持续的时间长度，单位：ms
例如: driver.swipe(144,1017,144,444,2000)

需求:
 进入设置,从存储滑动到更多

# 找到存储和更多坐标
save = driver.find_element_by_xpath("//*[contains(@text,'存储')]").location
more = driver.find_element_by_xpath("//*[contains(@text,'更多')]").location
# 移动
driver.swipe(save[‘x’], save[“y”], more[“x”], more[“y”], 2000)

```

### 3. scroll滚动事件

从一个元素滚动到另外一个元素,直到页面自动停止

```
方法: scroll(origin_el, destination_el)
参数:
1. origin_el:开始位置
2. destination_el: 结束元素

需求:
  进入设置页,模拟手指从存储菜单位置到WLAN菜单位置上滑动操作

el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 定位到WLAN菜单栏
el2 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# 执行滑动操作
driver.scroll(el1,el2)
```

### 4. drag拖拽事件

从一个元素滑动到另外一个元素,第二个元素替代第一个元素原本屏幕上的位置

```
方法: drag_and_drop(origin_el, destination_el)
参数:
1. origin_el:开始位置
2. destination_el: 结束元素

需求: 
	进入设置页,模拟手指将存储菜单 滑动到 WLAN菜单栏位置

el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 定位到WLAN菜单栏
el2 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# 执行滑动操作
driver.drag_and_drop(el1,el2)
```

### 5. 将应用置于后台事件

将应用放置到后台,模拟热启动

```
方法: background_app(seconds)
参数:
 seconds: 停留在后台时间,单位,秒
 
需求:
	进入设置,将app至于后台5s
	

driver.background_app(5)

```

