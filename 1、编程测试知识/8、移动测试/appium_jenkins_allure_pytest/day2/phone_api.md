## 手机操作api

针对手机的一些常用设置功能进行操作.

前置代码:

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

#### 1.1 获取手机时间

```
方法:device_time 

代码:
# 获取当前手机的时间
print(driver.device_time)
```

#### 1.2 获取手机宽高

获取手机宽高,可以根据宽高做一些坐标操作

```
方法：get_window_size()

代码实现：
print(driver.get_window_size())
```

#### 1.3 发送键到设备

模拟系统键值操作,比如home键,音量键,返回键等.

```
方法:keyevent(keycode, metastate=None):

参数：
	keycode：发送给设备的关键代码
	metastate：关于被发送的关键代码的元信息，⼀般为默认值

示例:打开设置,按多次音量增加键
代码实现:

for i in range(3):
		driver.keyevent(24)
```

#### 1.4 操作手机通知栏

打开手机通知栏,可以获取通知栏的相关信息和元素操作

```
方法: open_notifications()

需求:
	启动设置、打开通知栏

代码实现:
driver.open_notifications()
```

#### 1.5 获取当前手机网络

```
方法:network_connection 

示例:获取当前手机网络模式 

代码实现：
print(driver.network_connection)
```

#### 1.6 设置手机网络

更改手机的网络模式,模拟特殊网络情况

```
方法:set_network_connection(connectionType)
参数:connectionType：需要被设置成为的⽹络类型

示例:
	启动设置,设置手机网络为飞行模式.
代码实现:
driver.set_network_connection(1)
```

#### 1.6 手机截图

```
截取 手机当前屏幕,保存指定格式图片到指定位置

方法:get_screenshot_as_file(filename)
参数：
filename：指定路径下，指定格式的图⽚.

需求:
	打开设置页面,截图当前页面,命名为screen.png

代码实现:
import os
driver.get_screenshot_as_file(os.getcwd() + os.sep + './screen.png')
```