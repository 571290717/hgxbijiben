# Day31 Web自动化详解（5）——WebDriver(Selenium)——元素操作方法、及控制浏览器

[TOC]



![](https://the-toast.oss-cn-shenzhen.aliyuncs.com/image-20230630092014948.png)

# 目标

```
1. 掌握WebDriver常用的元素操作方法
2. 掌握WebDriver常用的操作浏览器方法
```

------

# 1. 为什么要学习操作元素的方法？

```
1. 需要让脚本模拟用户给浏览器指定元素输入值
2. 需要让脚本模拟人为删除元素的内容
3. 需要让脚本模拟点击按钮    
```

# 2. 元素常用操作方法

```
1. clear()            清除文本
2. send_keys()        模拟输入
3. click()            单击元素

说明：由于这三个方法非常简单，并且有些之前已经使用过，所以在这里用一个案例一起来讲解
```

### 2.1 案例-1 用户注册A

```
需求：
    1. 通过脚本执行输入 用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com;
    2. 间隔3秒后，修改电话号码为：18600000000
    3. 间隔3秒，点击注册用户A
    4. 间隔3秒，关闭浏览器
    5. 元素定位方法不限
```

### 2.2 案例-1 实现步骤难点分析：

```
1. 间隔3秒 --> sleep(3)
2. 修改电话号码，先清除在输入新的号码； 清除  --> clear()
3. 点击按钮  --> click()
```

### 问题

```
1. 脚本启动浏览器窗口大小默认不是全屏？
2. 脚本执行结束如何关闭浏览器？
```

------

# 3. 浏览器常用方法

```
说明：主要了解通过WebDriver操作浏览器的常用方法
```

### 3.1 WebDriver操作浏览器常用方法

```
1. maximize_window()                最大化 --> 模拟浏览器最大化按钮
2. set_window_size(100,100)            浏览器大小 --> 设置浏览器宽、高(像素点)
3. set_window_position(300,200)     浏览器位置 --> 设置浏览器位置
4. back()                             后退 --> 模拟浏览器后退按钮
5. forward()                         前进 --> 模拟浏览器前进按钮
6. refresh()                         刷新 --> 模拟浏览器F5刷新
7. close()                            关闭 --> 模拟浏览器关闭按钮(关闭单个窗口)
8. quit()                            关闭 --> 关闭所有WebDriver启动的窗口
```

### 3.2 WebDriver 操作浏览器方式-总结

```
# 最大化浏览器
driver.maximize_window()
# 刷新
driver.refresh()
# 后退
driver.back()
# 前进
driver.forward()
# 设置浏览器大小
driver.set_window_size(300,300)
# 设置浏览器位置
driver.set_window_position(300,200)
# 关闭浏览器单个窗口
driver.close()
# 关闭浏览器所有窗口
driver.quit()
```

# 4. WebDriver 其他常用的方法

### 4.1 为什么要学习WebDriver其他方法？

```
1. 如何获取元素大小？
2. 如果获取元素的文本？
3. 如何获取元素属性值？
4. 如果让程序判断元素是否为可见状态？

我们想解决以上问题，就需要学习WebDriver封装其他操纵元素的方法
```

### 4.2 WebDriver其他常用方法

```
1. size                 返回元素大小
2. text                 获取元素的文本
3. title                 获取页面title
4. current_url            获取当前页面URL
5. get_attribute("xxx") 获取属性值;xxx：要获取的属性
6. is_display()            判断元素是否可见
7. is_enabled()            判断元素是否可用

提示：
    1. size、text、title、current_url：为属性，调用时无括号；如：xxx.size
    2. title、current_url：使用浏览器实例化对象直接调用；    如： driver.title
```

# 5.总结

### WebDriver常用方法 

```
....
# 获取用户名文本框大小
size=driver.find_element_by_id("userA").size
print('size:',size)
# 获取a标签内容
text=driver.find_element_by_id("fwA").text
print('a标签text:',text)
# 获取title
title=driver.title
print('title:',title)
# 获取当前页面url
url=driver.current_url
print('url:',url)
# 获取a标签href属性值
href=driver.find_element_by_id("fwA").get_attribute("href")
print('href属性值为:',href)
# 判断span是否显示
display=driver.find_element_by_css_selector('span').is_displayed()
print('span标签是否显示：',display)
# 判断取消按钮是否可用
enabled=driver.find_element_by_id('cancelA').is_enabled()
print('取消按钮是否可用：',enabled)

执行结果：
size: {'height': 30, 'width': 163}
a标签text: 访问 新浪 网站
title: 注册A
url: file:///E:/%E6%B5%8B%E8%AF%95/%E8%AF%BE%E4%BB%B6/Web%E8%87%AA%E5%8A%A8%E5%8C%96/Web%E8%87%AA%E5%8A%A8%E5%8C%96%E8%AF%BE%E4%BB%B6/02img/%E6%B3%A8%E5%86%8CA.html
href属性值为: http://www.sina.com.cn/
span标签是否显示： False
取消按钮是否可用： False
```



![9c7bc198b36f77679bc7983f2f02810 (1)](https://the-toast.oss-cn-shenzhen.aliyuncs.com/9c7bc198b36f77679bc7983f2f02810%20(1)-16872526113086.jpg)



