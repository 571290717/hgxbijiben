# 模拟手势操作

## 学习目标

- 掌握模拟手势操作的api



### 前置代码

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



### 1. 手指轻敲操作

模拟手指轻敲一下屏幕操作

```
方法: 
			tap(element=None, x=None, y=None)
			perform() # 发送命令到服务器执行操作
			
参数:
	1.element：被定位到的元素
	2.x：相对于元素左上⻆的坐标，通常会使⽤元素的X轴坐标
	3.y：通常会使用元素的Y轴坐标

需求:
	进入设置,点击wlan选项

代码:
# 通过元素定位方式敲击屏幕
el = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
TouchAction(driver).tap(el).perform()
# 通过坐标方式敲击屏幕，WLAN坐标:x=149,y=324
# TouchAction(driver).tap(x=149,y=324).perform()
```

### 2. 手指按下操作

模拟手指按下屏幕,按就要对应着离开

```
方法:
	press(el=None, x=None, y=None)
	release() # 结束动作，手指离开屏幕
	
参数:
	1.element：被定位到的元素
	2.x：通常会使用元素的X轴坐标
	3.y：通常会使用元素的Y轴坐标

需求:
	进入设置,点击wlan选项

代码:

# 通过元素定位方式按下屏幕
el = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
TouchAction(driver).press(el).release().perform()
```

### 3. 等待操作

```
方法:
	wait(ms=0)
参数:
	ms暂停的毫秒数

需求:
	进入设置,点击wlan选项,长按wiredSSID选项5秒

代码:
	driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()
	el = driver.find_element_by_id("android:id/title")
	TouchAction(driver).press(el).wait(3000).release().perform()
```

#### 4. 手指长按操作

模拟手机按下屏幕一段时间,按就要对应着离开

```
方法:
	long_press(el=None, x=None, y=None, duration=1000)
参数:
	1.element：被定位到的元素
  2.x：通常会使用元素的X轴坐标
  3.y：通常会使用元素的Y轴坐标
  4.duration：持续时间，默认为1000ms
 
需求:
	进入设置、点击wlan选项、长按wired选项5秒
代码:
			# 点击WLAN
      driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()
      # 定位到WiredSSID
      el =driver.find_element_by_id("android:id/title")
      # 通过元素定位方式长按元素
      TouchAction(driver).long_press(el,duration=5000).release().perform()

      # 通过坐标方式长按元素，WiredSSID坐标:x=770,y=667
      # 添加等待(有长按)／不添加等待(无长按效果)
      # TouchAction(driver).long_press(x=770,y=667).perform()
```

### 5. 手指移动操作

模拟手机的滑动操作

```
方法:
	move_to(el=None, x=None, y=None)
参数:
	1.el:定位的元素
	2.x:相对于前一个元素的x轴偏移量
	3.y:相对于前一个元素的y轴偏移量

需求:
	进入设置、向上滑动屏幕
代码:
# 定位到存储
el = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 定位到更多
el1 = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
# 元素方式滑动
TouchAction(driver).press(el).move_to(el1).release().perform()
# 坐标的方式向上滑动
# TouchAction(driver).press(x=240,y=1000).move_to(x=0,y=-400).release().perform() 
# press().move_to() 实际使用的是TouchAction方法，需要给相对坐标.
# TouchAction(driver).press(x=240,y=600).wait(100).move_to(x=240,y=100).release().perform()
# press().wait().move_to()实际调用的是swip方法，会向下拉，感觉属于bug，可在log中查询swip，不建议这么用.
```

```
业务场景2：
        1.进入设置
        2.向上滑动屏幕到可见"安全"选项
        3.进入到安全
        4.点击屏幕锁定方式
        5.点击图案
        6.绘制图案
```

```
代码实现：
        # 定位到WLAN
        el1 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
        # 定位到存储
        el2 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
        # 存储上滑到WLAN
        driver.drag_and_drop(el2,el1)
        # 定位到用户
        el3 = driver.find_element_by_xpath("//*[contains(@text,'用户')]")
        # 注意 这次使用drag_and_drop方法，传入的"存储定位"仍使用其原始在屏幕上的位置，所以是由存储滑动到用户才可以上滑，否则需要重新"定位存储"
        # 存储上滑倒用户位置
        driver.drag_and_drop(el2,el3)
        # 点击安全按钮
        driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
        # 点击屏幕锁定方式按钮
        driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
        # 点击图案按钮
        driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()
        # 绘制图案四个坐标 1:(244,967) 2:(723,967) 3:(723,1442) 4:(244,1916)
        TouchAction(driver).press(x=244,y=967).wait(100).move_to(x=479,y=0).wait(100)\
            .move_to(x=0,y=475).wait(100).move_to(x=-479,y=474).release().perform()
```