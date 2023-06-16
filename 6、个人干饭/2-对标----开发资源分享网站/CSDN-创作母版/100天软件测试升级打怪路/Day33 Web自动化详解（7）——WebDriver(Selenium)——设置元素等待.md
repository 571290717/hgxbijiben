# Day33 Web自动化详解（7）——WebDriver(Selenium)——设置元素等待

# 设置元素等待

------

## 目标

```
1. 了解元素显式等待
2. 掌握元素隐式等待
```

------

## 1. 元素等待

### 1.1 什么是元素等待？

```
概念：WebDriver定位页面元素时如果未找到，会在指定时间内一直等待的过程；
```

### 1.2 为什么要设置元素等待？

```
1. 由于网络速度原因
2. 电脑配置原因
3. 服务器处理请求原因

WebDriver元素等待有几种类型呢？
```

### 1.3 元素等待类型

```
1. 显式等待
2. 隐式等待
```

------

## 2. 显式等待【了解】

```
概念：使WebDriver等待指定元素条件成立时继续执行，否则在达到最大时长时抛出超时异常(TimeoutException)

提示：
    1). 在WebDriver中把显式等待的相关方法封装在WebDriverWait类中
    2). 等待是判定条件成立时，那如何判断条件成立？相关判断的方法封装在expected_conditions类中
```

### 2.1 案例-1 注册页面A

```
需求：
    1. 如果用户名文本框存在，就输入admin
```

### 2.2 实现难点分析

```
1. 导包 等待类         --> from selenium.webdriver.support.wait import WebDriverWait
2. 导包 判断条件     --> from selenium.webdriver.support import expected_conditions as EC
                        (将expected_conditions 通过as关键字起个别名：EC)
3. WebDriverWait(driver, timeout, poll_frequency=0.5)
        1). driver：浏览器对象
        2). timeout：超时的时长，单位：秒
        3). poll_frequency：检测间隔时间，默认为0.5秒
4. 调用方法 until(method)：直到..时
        1). method：调用EC.presence_of_element_located(element)
                    element：调用By类方法进行定位
```

### 2.3 案例-1 代码示例

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
url = r'E:\测试\课件\Web自动化\Web自动化课件\02img\注册A.html'
driver = webdriver.Firefox()
driver.get(url)
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'userA')))
element.send_keys("admin")
```

## 3. 隐式等待【掌握】

```
说明：等待元素加载指定的时长，超出抛出NoSuchElementException异常，实际工作中，一般都使用隐式等待；

显式与隐式区别：
    1. 作用域：显式等待为单个元素有效，隐式为全局元素
    2. 方法：显式等待方法封装在WebDriverWait类中，而隐式等待则直接通过浏览器实例化对象调用
```

### 3.1 隐式等待调用方法

```
方法：implicitly_wait(timeout)
      (timeout：为等待最大时长，单位：秒)

调用：driver.implicitly_wait(10)
      (driver：为浏览器实例化对象名称)
```

### 3.2 隐式等待执行-说明

```
如果定位某一元素定位失败，那么就会触发隐式等待有效时长，如果在指定时长内加载完毕，则继续执行，否则
抛出NoSuchElementException异常，如果元素在第一次就定位到则不会触发隐式等待时长；
```

------

## 4. 元素等待-总结

```
1. 为什么要设置元素等待
2. 显式等待与隐式等待区别
3. 掌握隐式等待
```