# Day101 selenium爬虫

[TOC]





主要学习selenium自动化测试框架在爬虫中的应用，selenium能够大幅降低爬虫的编写难度，但是也同样会大幅降低爬虫的爬取速度。在逼不得已的情况下我们可以使用selenium进行爬虫的编写。



## selenium的介绍

##### 知识点：

- 了解 selenium的工作原理
- 了解 selenium以及chromedriver的安装
- 掌握 标签对象click点击以及send_keys输入

----



### 1. selenium运行效果展示

> Selenium是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，Selenium 可以直接调用浏览器，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器），可以接收指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏等。我们可以使用selenium很容易完成之前编写的爬虫，接下来我们就来看一下selenium的运行效果

#### 1.1 chrome浏览器的运行效果

> 在下载好chromedriver以及安装好selenium模块后，执行下列代码并观察运行的过程

```python
from selenium import webdriver 

# 如果driver没有添加到了环境变量，则需要将driver的绝对路径赋值给executable_path参数
# driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')

# 如果driver添加了环境变量则不需要设置executable_path
driver = webdriver.Chrome()

# 向一个url发起请求
driver.get("http://www.itcast.cn/")

# 把网页保存为图片，69版本以上的谷歌浏览器将无法使用截图功能
# driver.save_screenshot("itcast.png")

print(driver.title) # 打印页面的标题

# 退出模拟浏览器
driver.quit() # 一定要退出！不退出会有残留进程！
```



#### 1.2 phantomjs无界面浏览器的运行效果

> PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript。下载地址：<http://phantomjs.org/download.html>

```python
from selenium import webdriver 

# 指定driver的绝对路径
driver = webdriver.PhantomJS(executable_path='/home/worker/Desktop/driver/phantomjs') 
# driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')

# 向一个url发起请求
driver.get("http://www.itcast.cn/")

# 把网页保存为图片
driver.save_screenshot("itcast.png")

# 退出模拟浏览器
driver.quit() # 一定要退出！不退出会有残留进程！
```

#### 1.3 观察运行效果

- python代码能够自动的调用谷歌浏览或phantomjs无界面浏览器，控制其自动访问网站

  

#### 1.4 无头浏览器与有头浏览器的使用场景

- 通常在开发过程中我们需要查看运行过程中的各种情况所以通常使用有头浏览器
- 在项目完成进行部署的时候，通常平台采用的系统都是服务器版的操作系统，服务器版的操作系统必须使用无头浏览器才能正常运行



### 2. selenium的作用和工作原理

> 利用浏览器原生的API，封装成一套更加面向对象的Selenium WebDriver API，直接操作浏览器页面里的元素，甚至操作浏览器本身（截屏，窗口大小，启动，关闭，安装插件，配置证书之类的）

![selenium的工作原理](D:\hgx笔记\hgxbijiben\4、爬虫知识\课件\04-selenium的使用\images\selenium的工作原理.png)

- webdriver本质是一个web-server，对外提供webapi，其中封装了浏览器的各种功能
- 不同的浏览器使用各自不同的webdriver

----

##### 知识点：了解 selenium的工作原理

----



### 3. selenium的安装以及简单使用

> 我们以谷歌浏览器的chromedriver为例

#### 3.1 在python虚拟环境中安装selenium模块

`pip/pip3 install selenium`

#### 3.2 下载版本符合的webdriver

> 以chrome谷歌浏览器为例

1. 查看谷歌浏览器的版本

   ![查看chrome版本](D:\hgx笔记\hgxbijiben\4、爬虫知识\课件\04-selenium的使用\images\查看chrome版本.png)

   ​	![查看chrome版本2](D:\hgx笔记\hgxbijiben\4、爬虫知识\课件\04-selenium的使用\images\查看chrome版本2.png)



2. 访问https://npm.taobao.org/mirrors/chromedriver，点击进入不同版本的chromedriver下载页面

   ![下载chromedriver-1](D:\hgx笔记\hgxbijiben\4、爬虫知识\课件\04-selenium的使用\images\下载chromedriver-1.png)


3. 点击notes.txt进入版本说明页面

   ![下载chromedriver-2](D:\hgx笔记\hgxbijiben\4、爬虫知识\课件\04-selenium的使用\images\下载chromedriver-2.png)


4. 查看chrome和chromedriver匹配的版本

   ![下载chromedriver-3](D:\hgx笔记\hgxbijiben\4、爬虫知识\课件\04-selenium的使用\images\下载chromedriver-3.png)


5. 根据操作系统下载正确版本的chromedriver

   ![下载chromedriver-4](D:\hgx笔记\hgxbijiben\4、爬虫知识\课件\04-selenium的使用\images\下载chromedriver-4.png)

6. 解压压缩包后获取python代码可以调用的谷歌浏览器的webdriver可执行文件

   - windows为`chromedriver.exe`

   - linux和macos为`chromedriver`

7. chromedriver环境的配置

   - windows环境下需要将 chromedriver.exe 所在的目录设置为path环境变量中的路径
   - linux/mac环境下，将 chromedriver 所在的目录设置到系统的PATH环境值中

----

##### 知识点：了解 selenium以及chromedriver的安装

----



### 4.  selenium的简单使用

> 接下来我们就通过代码来模拟百度搜索

```python
import time
from selenium import webdriver

# 通过指定chromedriver的路径来实例化driver对象，chromedriver放在当前目录。
# driver = webdriver.Chrome(executable_path='./chromedriver')
# chromedriver已经添加环境变量
driver = webdriver.Chrome()

# 控制浏览器访问url地址
driver.get("https://www.baidu.com/")

# 在百度搜索框中搜索'python'
driver.find_element_by_id('kw').send_keys('python')
# 点击'百度搜索'
driver.find_element_by_id('su').click()

time.sleep(6)
# 退出浏览器
driver.quit()
```

- `webdriver.Chrome(executable_path='./chromedriver')`中executable参数指定的是下载好的chromedriver文件的路径
- `driver.find_element_by_id('kw').send_keys('python')`定位id属性值是'kw'的标签，并向其中输入字符串'python'
- `driver.find_element_by_id('su').click()`定位id属性值是su的标签，并点击
  - click函数作用是：触发标签的js的click事件

----

##### 知识点：掌握 标签对象click点击以及send_keys输入

----

## selenium提取数据

##### 知识点：

- 了解 driver对象的常用属性和方法
- 掌握 driver对象定位标签元素获取标签对象的方法
- 掌握 标签对象提取文本和属性值的方法

----



### 1. driver对象的常用属性和方法

> 在使用selenium过程中，实例化driver对象后，driver对象有一些常用的属性和方法

1. `driver.page_source` 当前标签页浏览器渲染之后的网页源代码
2. `driver.current_url` 当前标签页的url
3. `driver.close()` 关闭当前标签页，如果只有一个标签页则关闭整个浏览器
4. `driver.quit()` 关闭浏览器
5. `driver.forward()` 页面前进
6. `driver.back()` 页面后退
7. `driver.screen_shot(img_name)` 页面截图

----

##### 知识点：了解 driver对象的常用属性和方法

-----



### 2. driver对象定位标签元素获取标签对象的方法

> 在selenium中可以通过多种方式来定位标签，返回标签元素对象

```python
find_element_by_id 						(返回一个元素)
find_element(s)_by_class_name 			(根据类名获取元素列表)
find_element(s)_by_name 				(根据标签的name属性值返回包含标签对象元素的列表)
find_element(s)_by_xpath 				(返回一个包含元素的列表)
find_element(s)_by_link_text 			(根据连接文本获取元素列表)
find_element(s)_by_partial_link_text 	(根据链接包含的文本获取元素列表)
find_element(s)_by_tag_name 			(根据标签名获取元素列表)
find_element(s)_by_css_selector 		(根据css选择器来获取元素列表)
```

- 注意：
  - find_element和find_elements的区别：
    - 多了个s就返回列表，没有s就返回匹配到的第一个标签对象
    - find_element匹配不到就抛出异常，find_elements匹配不到就返回空列表
  - by_link_text和by_partial_link_tex的区别：全部文本和包含某个文本
  - 以上函数的使用方法
    - `driver.find_element_by_id('id_str')`

----

##### 知识点：掌握 driver对象定位标签元素获取标签对象的方法

----



###  3. 标签对象提取文本内容和属性值

> find_element仅仅能够获取元素，不能够直接获取其中的数据，如果需要获取数据需要使用以下方法

- 对元素执行点击操作`element.click()`

  - 对定位到的标签对象进行点击操作

- 向输入框输入数据`element.send_keys(data)`

  - 对定位到的标签对象输入数据

- 获取文本`element.text`

  - 通过定位获取的标签对象的`text`属性，获取文本内容

- 获取属性值`element.get_attribute("属性名")`

  - 通过定位获取的标签对象的`get_attribute`函数，传入属性名，来获取属性的值


​    

- 代码实现，如下：

  ```python
  from selenium import webdriver
  
  driver = webdriver.Chrome()
  
  driver.get('http://www.itcast.cn/')
  
  ret = driver.find_elements_by_tag_name('h2')
  print(ret[0].text) # 
  
  ret = driver.find_elements_by_link_text('黑马程序员')
  print(ret[0].get_attribute('href'))
  
  driver.quit()
  ```

----

##### 知识点：掌握 元素对象的操作方法

----



## selenium的其它使用方法

##### 知识点：

- 掌握 selenium控制标签页的切换
- 掌握 selenium控制iframe的切换
- 掌握 利用selenium获取cookie的方法
- 掌握 手动实现页面等待
- 掌握 selenium控制浏览器执行js代码的方法
- 掌握 selenium开启无界面模式
- 了解 selenium使用代理ip
- 了解 selenium替换user-agent

----



### 1. selenium标签页的切换

> 当selenium控制浏览器打开多个标签页时，如何控制浏览器在不同的标签页中进行切换呢？需要我们做以下两步：

- 获取所有标签页的窗口句柄

- 利用窗口句柄字切换到句柄指向的标签页

  - 这里的窗口句柄是指：指向标签页对象的标识
  - [关于句柄请课后了解更多，本小节不做展开](https://baike.baidu.com/item/%E5%8F%A5%E6%9F%84/3527587?fr=aladdin)

- 具体的方法

  ```
  # 1. 获取当前所有的标签页的句柄构成的列表
  current_windows = driver.window_handles
  
  # 2. 根据标签页句柄列表索引下标进行切换
  driver.switch_to.window(current_windows[0])
  ```

- 参考代码示例：

  ```python
  import time
  from selenium import webdriver
  
  driver = webdriver.Chrome()
  driver.get("https://www.baidu.com/")
  
  time.sleep(1)
  driver.find_element_by_id('kw').send_keys('python')
  time.sleep(1)
  driver.find_element_by_id('su').click()
  time.sleep(1)
  
  # 通过执行js来新开一个标签页
  js = 'window.open("https://www.sogou.com");'
  driver.execute_script(js)
  time.sleep(1)
  
  # 1. 获取当前所有的窗口
  windows = driver.window_handles
  
  time.sleep(2)
  # 2. 根据窗口索引进行切换
  driver.switch_to.window(windows[0])
  time.sleep(2)
  driver.switch_to.window(windows[1])
  
  time.sleep(6)
  driver.quit()
  ```

----

##### 知识点：掌握 selenium控制标签页的切换

----



### 2. switch_to切换frame标签

> ##### iframe是html中常用的一种技术，即一个页面中嵌套了另一个网页，selenium默认是访问不了frame中的内容的，对应的解决思路是`driver.switch_to.frame(frame_element)`。接下来我们通过qq邮箱模拟登陆来学习这个知识点

- 参考代码：

  ```python
  import time
  from selenium import webdriver
  
  driver = webdriver.Chrome()
  
  url = 'https://mail.qq.com/cgi-bin/loginpage'
  driver.get(url)
  time.sleep(2)
  
  login_frame = driver.find_element_by_id('login_frame') # 根据id定位 frame元素
  driver.switch_to.frame(login_frame) # 转向到该frame中
  
  driver.find_element_by_xpath('//*[@id="u"]').send_keys('1596930226@qq.com')
  time.sleep(2)
  
  driver.find_element_by_xpath('//*[@id="p"]').send_keys('hahamimashicuode')
  time.sleep(2)
  
  driver.find_element_by_xpath('//*[@id="login_button"]').click()
  time.sleep(2)
  
  """操作frame外边的元素需要切换出去"""
  windows = driver.window_handles
  driver.switch_to.window(windows[0])
  
  content = driver.find_element_by_class_name('login_pictures_title').text
  print(content)
  
  driver.quit()
  ```



- 总结：

  - 切换到定位的frame标签嵌套的页面中

    - `driver.switch_to.frame(通过find_element_by函数定位的frame、iframe标签对象)`

  - 利用切换标签页的方式切出frame标签

    - ```
      windows = driver.window_handles
      driver.switch_to.window(windows[0])
      ```

------

##### 知识点：掌握 selenium控制frame标签的切换

------



### 3. selenium对cookie的处理

> selenium能够帮助我们处理页面中的cookie，比如获取、删除，接下来我们就学习这部分知识

#### 3.1 获取cookie

> `driver.get_cookies()`返回列表，其中包含的是完整的cookie信息！不光有name、value，还有domain等cookie其他维度的信息。所以如果想要把获取的cookie信息和requests模块配合使用的话，需要转换为name、value作为键值对的cookie字典

```
# 获取当前标签页的全部cookie信息
print(driver.get_cookies())
# 把cookie转化为字典
cookies_dict = {cookie[‘name’]: cookie[‘value’] for cookie in driver.get_cookies()}
```

#### 3.2 删除cookie

```
#删除一条cookie
driver.delete_cookie("CookieName")

# 删除所有的cookie
driver.delete_all_cookies()
```

------

##### 知识点：掌握 利用selenium获取cookie的方法

------



### 4. selenium控制浏览器执行js代码

> selenium可以让浏览器执行我们规定的js代码，运行下列代码查看运行效果

```python
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.itcast.cn/")
time.sleep(1)

js = 'window.scrollTo(0,document.body.scrollHeight)' # js语句
driver.execute_script(js) # 执行js的方法

time.sleep(5)
driver.quit()
```

-  执行js的方法：`driver.execute_script(js)` 

------

##### 知识点：掌握 selenium控制浏览器执行js代码的方法

------



### 5. 页面等待

> 页面在加载的过程中需要花费时间等待网站服务器的响应，在这个过程中标签元素有可能还没有加载出来，是不可见的，如何处理这种情况呢？

1. 页面等待分类
2. 强制等待介绍
3. 显式等待介绍
4. 隐式等待介绍
5. 手动实现页面等待

#### 5.1 页面等待的分类

> 首先我们就来了解以下selenium页面等待的分类

1. 强制等待
2. 隐式等待
3. 显式等待

#### 5.2 强制等待（了解）

- 其实就是time.sleep()
- 缺点时不智能，设置的时间太短，元素还没有加载出来；设置的时间太长，则会浪费时间

#### 5.3 隐式等待

- 隐式等待针对的是元素定位，隐式等待设置了一个时间，在一段时间内判断元素是否定位成功，如果完成了，就进行下一步

- 在设置的时间内没有定位成功，则会报超时加载

- 示例代码

  ```
  from selenium import webdriver
  
  driver = webdriver.Chrome()  
  
  driver.implicitly_wait(10) # 隐式等待，最长等20秒  
  
  driver.get('https://www.baidu.com')
  
  driver.find_element_by_xpath()
  
  ```

#### 5.4 显式等待（了解）

- 每经过多少秒就查看一次等待条件是否达成，如果达成就停止等待，继续执行后续代码

- 如果没有达成就继续等待直到超过规定的时间后，报超时异常

- 示例代码

  ```
  from selenium import webdriver  
  from selenium.webdriver.support.wait import WebDriverWait  
  from selenium.webdriver.support import expected_conditions as EC  
  from selenium.webdriver.common.by import By 
  
  driver = webdriver.Chrome()
  
  driver.get('https://www.baidu.com')
  
  # 显式等待
  WebDriverWait(driver, 20, 0.5).until(
      EC.presence_of_element_located((By.LINK_TEXT, '好123')))  
  # 参数20表示最长等待20秒
  # 参数0.5表示0.5秒检查一次规定的标签是否存在
  # EC.presence_of_element_located((By.LINK_TEXT, '好123')) 表示通过链接文本内容定位标签
  # 每0.5秒一次检查，通过链接文本内容定位标签是否存在，如果存在就向下继续执行；如果不存在，直到20秒上限就抛出异常
  
  print(driver.find_element_by_link_text('好123').get_attribute('href'))
  driver.quit() 
  ```

#### 5.5 手动实现页面等待

> 在了解了隐式等待和显式等待以及强制等待后，我们发现并没有一种通用的方法来解决页面等待的问题，比如“页面需要滑动才能触发ajax异步加载”的场景，那么接下来我们就以[淘宝网首页](https://www.taobao.com)为例，手动实现页面等待

- 原理：
  - 利用强制等待和显式等待的思路来手动实现
  - 不停的判断或有次数限制的判断某一个标签对象是否加载完毕（是否存在）
- 实现代码如下：

```
import time
from selenium import webdriver
driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver')

driver.get('https://www.taobao.com/')
time.sleep(1)

# i = 0
# while True:
for i in range(10):
    i += 1
    try:
        time.sleep(3)
        element = driver.find_element_by_xpath('//div[@class="shop-inner"]/h3[1]/a')
        print(element.get_attribute('href'))
        break
    except:
        js = 'window.scrollTo(0, {})'.format(i*500) # js语句
        driver.execute_script(js) # 执行js的方法
driver.quit()
```

------

##### 知识点：掌握 手动实现页面等待

------



### 6. selenium开启无界面模式

> 绝大多数服务器是没有界面的，selenium控制谷歌浏览器也是存在无界面模式的，这一小节我们就来学习如何开启无界面模式（又称之为无头模式）

- 开启无界面模式的方法
  - 实例化配置对象
    - `options = webdriver.ChromeOptions()`
  - 配置对象添加开启无界面模式的命令
    - `options.add_argument("--headless")`
  - 配置对象添加禁用gpu的命令
    - `options.add_argument("--disable-gpu")`
  - 实例化带有配置对象的driver对象
    - `driver = webdriver.Chrome(chrome_options=options)`
- 注意：macos中chrome浏览器59+版本，Linux中57+版本才能使用无界面模式！
- 参考代码如下：

```python
from selenium import webdriver

options = webdriver.ChromeOptions() # 创建一个配置对象
options.add_argument("--headless") # 开启无界面模式
options.add_argument("--disable-gpu") # 禁用gpu

# options.set_headles() # 无界面模式的另外一种开启方式
driver = webdriver.Chrome(chrome_options=options) # 实例化带有配置的driver对象

driver.get('http://www.itcast.cn')
print(driver.title)
driver.quit()
```

------

##### 知识点：掌握 selenium开启无界面模式

------



### 7. selenium使用代理ip

> selenium控制浏览器也是可以使用代理ip的！

- 使用代理ip的方法

  - 实例化配置对象
    - `options = webdriver.ChromeOptions()`
  - 配置对象添加使用代理ip的命令
    - `options.add_argument('--proxy-server=http://202.20.16.82:9527')`
  - 实例化带有配置对象的driver对象
    - `driver = webdriver.Chrome('./chromedriver', chrome_options=options)`

- 参考代码如下：

  ```python
  from selenium import webdriver
  
  options = webdriver.ChromeOptions() # 创建一个配置对象
  options.add_argument('--proxy-server=http://202.20.16.82:9527') # 使用代理ip
  
  driver = webdriver.Chrome(chrome_options=options) # 实例化带有配置的driver对象
  
  driver.get('http://www.itcast.cn')
  print(driver.title)
  driver.quit()
  ```

------

##### 知识点：了解 selenium使用代理ip

------



### 8. selenium替换user-agent

> selenium控制谷歌浏览器时，User-Agent默认是谷歌浏览器的，这一小节我们就来学习使用不同的User-Agent

- 替换user-agent的方法

  - 实例化配置对象
    - `options = webdriver.ChromeOptions()`
  - 配置对象添加替换UA的命令
    - `options.add_argument('--user-agent=Mozilla/5.0 HAHA')`
  - 实例化带有配置对象的driver对象
    - `driver = webdriver.Chrome('./chromedriver', chrome_options=options)`

- 参考代码如下：

  ```python
  from selenium import webdriver
  
  options = webdriver.ChromeOptions() # 创建一个配置对象
  options.add_argument('--user-agent=Mozilla/5.0 HAHA') # 替换User-Agent
  
  driver = webdriver.Chrome('./chromedriver', chrome_options=options)
  
  driver.get('http://www.itcast.cn')
  print(driver.title)
  driver.quit()
  ```

------

##### 知识点：了解 selenium替换user-agent

------







