class ProxyMiddleware(object):
    def process_request(self,request,spider):
        # proxies可以在settings.py中，也可以来源于代理ip的webapi
        # proxy = random.choice(proxies) 

        # 免费的会失效，报 111 connection refused 信息！重找一个代理ip再试
        proxy = 'https://1.71.188.37:3128' 
    
        request.meta['proxy'] = proxy
        return None # 可以不写return

# 爬虫代码总结（自己敲）

````mysql
#爬虫：模拟浏览器，发送请求，获取响应


流程： 
1、获取一个url
2、向url发送请求、并获取响应（需要http协议）
3、如果从响应中提取url，则继续发送请求获取响应
4、如果从响应中提取数据，则将数据进行保存



HTTP:超文本传输协议，默认端口号80 
    超文本：是指超过文本，不仅限于文本;还包括图片、音频、视频等文件
    传输协议：是指使用共用待定的固定格式来传递转换成字符串的超文本内容
HTTPS：HTTP+SSl(安全套接字层)，即带有安全套接字层的超文本传输协议，默认端口号443
	SSL对传输的内容(超文本，也就是请求体或者响应体)进步加密
  
content—type 文本类型
Host
Connection
Upgrade-Insecure-Requests  |HTTPS
user-Agent
Referer
Cookie
Authorization


200 
302
303
307
403
404
500
503

http请求的过程：
	1、浏览器在拿到域名对应的ip后，先向地址栏中的url发送请求，并获取响应
    2、在返回的响应内容（html）中，会带有css、js、图片等url地址，以及ajax代码，浏览器按照响应内容中的顺序依次发送其他的请求，并获取相应的响应
    3、浏览器每获取一个响应就对展出的结果进行添加（加载），js，css等内容会修改页面的内容，js也可以重新发送请求，获取响应
    4、从获取第一个响应并在浏览器，中展示，直到最终获取全部响应，并在展示的结果中添加内容或修改————渲染
    
##### 浏览器展示的结果可以由多次请求对应的多次响应共同渲染出来，而爬虫是一次请求对应一个响应


request模块
发送http请求，获取响应

pip install requests

import requests

url = "xxxx "
response = requests.get(url)
print(response.text)

print(response.content.decode())
response.text = response.content.decode('推测出的编码字符集')

response.url
response.status_code
response.request.headers
response.headers
response.request._cookies
response.cookies
response.json()

# 打印响应内容
# print(response.text)
# print(response.content.decode()) 			# 注意这里！
print(response.url)							# 打印响应的url
print(response.status_code)					# 打印响应的状态码
print(response.request.headers)				# 打印响应对象的请求头
print(response.headers)						# 打印响应头
print(response.request._cookies)			# 打印请求携带的cookies
print(response.cookies)						# 打印响应中携带的cookies



import resquests
url='https://www.baidu,com'
header={ "User-Agent": "xxxx",
       	"Cookie":'xxxcookie'
       }
kw={'xx1':'xx2'}
response = resquest.get(url,headers = headers,params=kw)
print(response.content)
print(response.request.headers)

cookies = {"cookies_name":"cookies_value"}

cookies_str = "复制的cookiesxxxxx"
cookies_dict = {cookie.split('=')[0]:cookie.split('=')[-1] for cookie in cookies_str.split("; ")}
resp = requests.get(url,headers=headers,cookies=cookies_dict)


cookies_dict = resquest.utils.dict_form_cookiejar(response.cookies)
==> 返回cookies字典


response = resquests.get(url.timeout=3)

代理
Transparent Proxy
Anonymous Proxy
Elite proxy or High Anonymity Proxy

proxies = {
    "http":"xxxxxxx",
    "https": "xxxxxx",
}

response = request.get(url,proxies=proxies)#!!!!!!!!



##项目百度翻译
import requests
import json



class King(object):
    
    def __init__(self,word):
        self.url = "http://fy.iciba.com/ajax.php?a=fy"
        self.word = word
        self.headers = {
            
            "User-Agent":'xxxxx'
        }
		self.post_data = {
            "f" : "auto",
            "t" : "auto",
            "w" : self.word
        }

	def get_data(self):
        response = requests.post(self.url,headers=self.headers,data=self.post_data)
        return response.content
    
    def parse_data(self,data):
        dict_data = json.loads(data)
        
        try:
            print(dict_data['content']['out'])
		except:
            print(dict_data['content']['word_mean'][0])
   
	def run(self):
        data = self.get_data()
        self.parse_data(data)
        
if __name__ == '__main__':
    king=King("china")
	king.run()
    
    
    ## 利用requests.session进行状态保持

> requests模块中的Session类能够自动处理发送请求获取响应过程中产生的cookie，进而达到状态保持的目的。接下来我们就来学习它
- requests.session的作用
  - 自动处理cookie，即 **下一次请求会带上前一次的cookie**
- requests.session的应用场景
  - 自动处理连续的多次请求过程中产生的cookie
    
    session = requests.session()
    response = session.get(url,header,...)
    response = session.post(url,data,...)
    
    
import requests
import re


# 构造请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

# 实例化session对象
session = requests.session()

# 访问登陆页获取登陆请求所需参数
response = session.get('https://github.com/login', headers=headers)
authenticity_token = re.search('name="authenticity_token" value="(.*?)" />', response.text).group(1) # 使用正则获取登陆请求所需参数

# 构造登陆请求参数字典
data = {
    'commit': 'Sign in', # 固定值
    'utf8': '✓', # 固定值
    'authenticity_token': authenticity_token, # 该参数在登陆页的响应内容中
    'login': input('输入github账号：'),
    'password': input('输入github账号：')
}

# 发送登陆请求（无需关注本次请求的响应）
session.post('https://github.com/session', headers=headers, data=data)

# 打印需要登陆后才能访问的页面
response = session.get('https://github.com/1596930226', headers=headers)
print(response.text)



#######数据提取概要#####


- html：
  - 超文本标记语言
  - 为了更好的显示数据，侧重点是为了显示
- xml：
  - 可扩展标记语言
  - 为了传输和存储数据，侧重点是在于数据内容本身


#jsonpath
pip install jsonpath

from jsonpath import jsonpath
 ret = jsonpath(a,'jsonpath语法规则字符串')
     
 
#jsonpath语法规则
 $  
 @
 . or[]
 n/a
..
*
n/a
[]
[,]
?()
()
n/a


eg:
    $.store.book[*].author
    $..author
    $.store.*
    $.store..price
    $..book[2]
    $..book[(@.length-1)] | $..book[-1:]
    $..book[0,1] | $..book[:2]
    $..book[?(@.isbn)]
    $..book[?(@.price<10)]
    $..*
##拉勾网

import requests
import jsonpath
import json

url = "xxxxx"
headers = {"User-Agent": "xxxxx"}
response = request.get(url,header=headers)
html_str = response.content.decode()

jsonobj = json.loads(html_str)
citylist = jsonpath.jsonpath(jsonobj,"$..name")

with open('city_name.txt','w') as f:
    content = json.dumps(citylist,ensure_ascii=False)
    f.write(content)


###数据提取-lxml模块

XPATH （参考selenium）
pip install lxml

W3School官方文档：<http://www.w3school.com.cn/xpath/index.asp>
    
html = etree.HTML(text)
ret_list=html.xpath('XPATH语法规则')



from lxml import etree

text = ''' 
<div> 
  <ul> 
    <li class="item-1">
      <a href="link1.html">first item</a>
    </li> 
    <li class="item-1">
      <a href="link2.html">second item</a>
    </li> 
    <li class="item-inactive">
      <a href="link3.html">third item</a>
    </li> 
    <li class="item-1">
      <a href="link4.html">fourth item</a>
    </li> 
    <li class="item-0">
      a href="link5.html">fifth item</a>
  </ul> 
</div>
'''
#利用etree.HTML，将html字符串（bytes类型或str类型）转化为Element对象，Element对象具有xpath的方法，返回结果的列表
html = etree.HTML(text)

#获取href的列表和title的列表
href_list = html.xpath("//li[@class='item-1']/a/@href")
titlr_list = html.xpath("//li[@class='item-1']/a/text()")

#组装成字典
for href in href_list:
    item = {}
    item["href"] = href
    item["title"] = title_list[href_list.index(href)]
	print(item)
    
  
- lxml.etree.HTML(html_str)可以自动补全标签
- `lxml.etree.tostring`函数可以将转换为Element对象再转换回html字符串
- 爬虫如果使用lxml来提取数据，应该以`lxml.etree.tostring`的返回结果作为提取数据的依据
    



from lxml import etree

html = etree.HTML(html_str)

handeled_html_str = etree.tostring(html).decode()




###selenium


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.itcast.cn/")
print(driver.title)
driver.quit()

##无界 PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript。下载地址：<http://phantomjs.org/download.html>
driver = webdriver.PhantomJS(executable_path = '/home/worker/Desktop/driver/phantomjs')
driver.get("http://www.itcast.cn/")
driver.save_screenshot("itcast.png")
driver.quit()



driver.page_source
driver.current_url
driver.screen_shot(img_name)


#手动实现页面等待

import time
from selenium import webdriver 
driver = webdriver.Chome("XXXX")

driver.get("XXXX")
time.sleep(1)

for i in range(10):
    i +=1
    try :
        time.sleep(3)
        element = driver .find_element_by_xpath('XXXX')
        print(element.get_attribute("href"))
        break
    except:
        js = "window.scrollTo(1,{})".format(i*500)
        driver.execute_script(js)
 
driver.quit()





 #selenium开启无界面模式

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_option=options)



from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(chrome_options=options)
driver.get("http://ww.itcast.cn")
print(driver.title)
driver.quit()


## 使用代理 ip
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://202.20.16.82:9527')
driver = webdriver.Chrome(chrome_options=options)

#selenium替换user—agent
options=webdriver.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 HAHA")
driver = webdriver.Chrome("./chromedriver",chrome_options=options)

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('XXXXX')

driver = webdriver.Chrome('./chromedriver',chrome_options=options)

driver.get('http://www.itcast.cn')
print(driver.title)
driver.quit()



#####反爬与反反爬


反爬的三个方向：
基于身份识别
''' 加请求头，防止被屏蔽，搞代理'''
基于爬虫行为
''' 分析爬取的资料，多爬取几次'''
基于数据加密
''' 进行数据反加密，页面数据js了，你也js，偏移了，你也偏移'''

掌握 常见的反爬手段、原理以及应对思路

文字性内容参照大总结



###图片验证码
### .图片识别引擎

> OCR（Optical Character Recognition）是指使用扫描仪或数码相机对文本资料进行扫描成图像文件，然后对图像文件进行分析处理，自动识别获取文字信息及版面信息的软件。

#### 2.1 什么是tesseract

- Tesseract，一款由HP实验室开发由Google维护的开源OCR引擎，特点是开源，免费，支持多语言，多平台。
- 项目地址：https://github.com/tesseract-ocr/tesseract   

pip install pillow
pip/pip3 install pytesseract

通过pytesseract模块的 image_to_string 方法就能将打开的图片文件中的数据提取成字符串数据

from PIL import Image
import pytesseract

im = Image.open()

result = pytessseract.image_to_string(im)

print(result)

'''图片验证码就是 先自己截屏然后再解读'''


#### 2.4 图片识别引擎的使用扩展

- [tesseract简单使用与训练](https://www.cnblogs.com/cnlian/p/5765871.html)
- 其他ocr平台

```
    微软Azure 图像识别：https://azure.microsoft.com/zh-cn/services/cognitive-services/computer-vision/
    有道智云文字识别：http://aidemo.youdao.com/ocrdemo
    阿里云图文识别：https://www.aliyun.com/product/cdi/
    腾讯OCR文字识别：https://cloud.tencent.com/product/ocr
```

### 
现在很多网站都会使用验证码来进行反爬，所以为了能够更好的获取数据，需要了解如何使用打码平台爬虫中的验证码

###例如云打码平台
云打码：http://www.yundama.com/

能够解决通用的验证码识别
###Chrome 隐身窗口
1. 使用隐身窗口的主要目的是为了避免首次打开网站携带cookie的问题
2. chrome的network中，perserve log选项能够在页面发生跳转之后任然能够观察之前的请求
3. 确定登录的地址有两种方法：
   - 寻找from表单action的url地址
   - 通过抓包获取

####JS的解析

1. 了解 定位js的方法
2. 了解 添加断点观察js的执行过程的方法
3. 应用 js2py获取js的方法

js2py是一个js的翻译工具，也是一个通过纯python实现的js的解释器，[github上源码与示例](https://github.com/PiotrDabkowski/Js2Py)

定位进行登录js代码

```js
formSubmit: function() {
        var e, t = {};
        $(".login").addEventListener("click", function() {
            t.phoneNum = $(".phonenum").value,
            t.password = $(".password").value,
            e = loginValidate(t),
            t.c1 = c1 || 0,
            e.flag ? ajaxFunc("get", "http://activity.renren.com/livecell/rKey", "", function(e) {
                var n = JSON.parse(e).data;
                if (0 == n.code) {
                    t.password = t.password.split("").reverse().join(""),
                    setMaxDigits(130);
                    var o = new RSAKeyPair(n.e,"",n.n)
                      , r = encryptedString(o, t.password);
                    t.password = r,
                    t.rKey = n.rkey
                } else
                    toast("公钥获取失败"),
                    t.rKey = "";
                ajaxFunc("post", "http://activity.renren.com/livecell/ajax/clog", t, function(e) {
                    var e = JSON.parse(e).logInfo;
                    0 == e.code ? location.href = localStorage.getItem("url") || "" : toast(e.msg || "登录出错")
                })
            }) : toast(e.msg)
        })
    }
```

##### 从代码中我们知道:

1. 我们要登录需要对密码进行加密和获取rkey字段的值
2. rkey字段的值我们直接发送请求rkey请求就可以获得
3. 密码是先反转然后使用RSA进行加密, js代码很复杂, 我们希望能通过在python中
执行js来实现
##实现思路:
1. 使用session发送rKey获取登录需要信息

   - url: http://activity.renren.com/livecell/rKey
   - 方法: get

2. 根据获取信息对密码进行加密
   2.1 准备用户名和密码

   2.2 使用js2py生成js的执行环境:context

   2.3 拷贝使用到js文件的内容到本项目中

   2.4 读取js文件的内容,使用context来执行它们

   2.5 向context环境中添加需要数据

   2.6 使用context执行加密密码的js字符串

   2.7 通过context获取加密后密码信息

3. 使用session发送登录请求

   - URL: http://activity.renren.com/livecell/ajax/clog

   - 请求方法: POST

   - 数据: 

     ```
     phoneNum: xxxxxxx
     password: (加密后生产的)
     c1: 0
     rKey: rkey请求获取的
     ```

##### 具体代码
''' 这个就是使用JS2py在post请求前对数据进行js加密 （用来加密的js代码可以通过get XX.js包来实现）'''
import requests
import json
import js2py

session = request.session()
header = {
    "User-Agent":"XXXx"
}
session.header = headers

response = session.get("XXX")
n = json.load(response.content)['data']
'''(1)json.loads
将JSON字符串转化为 Python 字段的数据类型。

loads：针对内存对象，将string转换为dict (将string转换为dict)'''
phoneNum = " 133XXX.."
password = "****"

context = js2py.EvalJs()
with opne("BigInt.js",'r',encoding='utf8') as f :
    context.execute(f.read())
with open('RSA.js','r',encoding='utf8')as f:
    context.execute(f.read())
with open("Barrett.js",'r',encoding='utf8')as f :
    context.execute(f.read())
    
context.t = {'password':password}
context.n=n
js = '''
       t.password = t.password.split("").reverse().join(""),
       setMaxDigits(130);
       var o = new RSAKeyPair(n.e,"",n.n)
        , r = encryptedString(o, t.password);
'''  
context.execute(js)
password= context.r
data={
     'phoneNum': '131....',
    'password': password,
    'c1':0,
    'rKey':n['rkey']
}
response = session.post("XXXX",data=data)
print(response.content.decode())

response = session.get("XXXX")
print(response.content.decode())

'''1. 通过在chrome中观察元素的绑定事件可以确定js
2. 通过在chrome中search all file 搜索关键字可以确定js的位置
3. 观察js的数据生成过程可以使用添加断点的方式观察
4. js2py的使用
   - 需要准备js的内容
   - 生成js的执行环境
   - 在执行环境中执行js的字符串，传入数据，获取结果'''








?################---Mongodb数据库---##############!!!!!!!!!

非关系性数据库mongodb


1. 了解 非关系型数据库的优势
   - 易扩展
   - 高性能
   - 灵活的数据字段
2. 了解 mongodb的安装
   - sudo apt-get install -y mongodb-org

- 默认端口：27017
- 默认配置文件的位置：/etc/mongod.conf
- 默认日志的位置：/var/log/mongodb/mongod.log


mongodb服务端启动分别两种方式：

- 本地测试方式的启动（只具有本地数据增删改查的功能）
- 生产环境启动（具有完整的全部功能）

#### 1.1 测试方式启动

- 启动: sudo service mongod start (sudo service mongod start)
- 停止: sudo service mongod stop
- 重启: sudo service mongod restart

#### 1.2 生产环境正式的启动方式

> 启动: sudo mongod [--auth --dbpath=dbpath --logpath=logpath --append --fork] [-–f logfile ]

- 只以 sudo mongod 命令启动时，默认将数据存放在了 /data/db 目录下，需要手动创建
- --dbpath: 指定数据库的存放路径
- --logpath: 指定日志的存放路径
- --append: 或--logappend 设置日志的写入形式为追加模式
- --fork: 或-fork 开启新的进程运行mongodb服务
- --f: 或-f 配置文件路径(可以将上述配置信息写入文件然后通过该文件中的参数进行加载启动)
- --auth: 以权限认证的方式启动，我们会在后边的课程中学习该内容

#### 1.3 查看是否启动成功

> ps aux | grep mongod

### 2. 启动mongodb的客户端：进入mongo shell

- 启动本地客户端: mongo
- 查看帮助：mongo –help
- 退出：exit或者ctrl+c

（'等自己下载一个mongodb实战后再回来写'））



Window 下装mongodb


mongDB命令
查看当前数据库： db
查看所有数据库： show dbs /show databases
切换数据库 ： use db_name 
删除当前数据库： db.dropDatabase()

无需手动创建集合：
向不存在的集合中第一次添加数据时，集合会自动被创建出来
手动创建集合
db.createCollection(name,options)
db.createCollection("stu")
db.createCollection("sub",{capped:true,size:10})
参数capped：默认值为false表示不设置上限，值true表示设置上限
参数size：集合所占用的字节数。当capped值为true时，需要指定此参数，表示上限大小，当文档达到上限时， 会将之前的数据覆盖，单位为字节
查看集合 ： show collections
删除集合 ： db.集合名称.drop()
检查集合是否设定上限：db.集合名.isCapped()


show dbs
use test
show collections
db
db.stu.insert({'name':'郭靖', 'age':22})
show dbs
show collections
db.stu.find()
db.stu.drop()
show collections
db.dropDatabase()
show dbs
exit

1. 服务端的启动
   - sudo mongod --dbpath=数据库路径
2. 进入mongo shell客户端
   - mongo
3. mongodb的数据库和集合命令
   - show dbs
   - use db_name
   - show collections
   - db
   - db.集合名.drop()
   - db.dropDatabase()
   - exit


插入数据 db.集合名称.insert(document)
保持数据 db.集合名称.save(document)
查询数据 db.集合名称.find()

	condition		条件; 状态; 状况;
	db.xx_name.find({condition})
	db.xx_name.findOne({condition})
	db.xx_name.find({condition}).pretty()
	
< $lt
<= $lte
> $gt
>= $gte
!= $ne

 eg:db.stu.find({age:{$gte:18}})
 
and : 在json中写多个条件即可
db.stu.find({age:{$gte:18},gender:true})
db.stu.find({$or:[{age:{$gt:18}},{gender:false}]})
db.stu.find({$or:[{age:{$gte:18}},{gender:true}],name:'gj'})

db.stu.find({name:{$regex:'^黄'}})

!#mongo shell 是一个js的执行环境
!#使用$where 写一个函数， 返回满足条件的数据

db.stu.find({
            $where:function(){
            	return this.age>30;
            }
            })

skip and limit

db.集合名称.find().limit(number)  查询number条信息
db.集合名称.find().skip(number)   跳过number条信息

db.stu.find().skip(5).limit(4)

投影
db.集合名称.find({},{字段名称：1，...})

- 对于_id列默认是显示的， 如果不显示需要明确设置为0
- 对于其他不显示的字段不能设置为0

`db.stu.find({},{_id:0,name:1,gender:1})`



#### 3.9 排序

方法sort()， 用于对查询结果按照指定的字段进行排序

命令：`db.集合名称.find().sort({字段:1,...})`

参数1为升序排列
参数-1为降序排列
根据性别降序， 再根据年龄升序
db.stu.find().sort({gender:-1,age:1})

#### 3.10 统计个数

方法count()用于统计结果集中文档条数

命令：`db.集合名称.find({条件}).count()`
命令：`db.集合名称.count({条件})
db.stu.find({gender:true}).count()
db.stu.conunt({age:{$gt:20},gender:true})



### 4 mongodb的更新

```
db.集合名称.update({query}, {update}, {multi: boolean})
```

- 参数query:查询条件
- 参数update:更新操作符
- 参数multi:可选，默认是false，表示只更新找到的第一条数据，值为true表示把满足条件的数据全部更

db.stu.update({name:'hr'},{name:'mnc'})           # 全文档进行覆盖更新
db.stu.update({name:'hr'},{$set:{name:'hys'}})    # 指定键值更新操作
db.stu.update({},{$set:{gender:0}},{multi:true})  # 更新全部

- 参数query:可选，删除的⽂档的条件

###5 mongodb的删除
db.集合名称.remove({query}, {justOne: boolean})
- 参数query:可选，删除的⽂档的条件
- 参数justOne:可选， 如果设为true或1，则只删除一条，默认false，表示删除全部


### 1 mongodb的聚合是什么

聚合(aggregate)是基于数据处理的聚合管道，每个文档通过一个由多个阶段（stage）组成的管道，可以对每个阶段的管道进行分组、过滤等功能，然后经过一系列的处理，输出相应的结果。

语法：`db.集合名称.aggregate({管道:{表达式}})`

aggregate  adj.	总数的; 总计的;
n.	合计; 总数; (可成混凝土或修路等用的)骨料，集料;
vt.	合计; 总计;

db.Collection.aggregate([{$match:{xxx:"xxx"}},{$group:{ _id:"$xxx",total:{$sum:"$xxxx"}}}])
 常用管道命令如下：

 - `$group`： 将集合中的⽂档分组， 可⽤于统计结果
 - `$match`： 过滤数据， 只输出符合条件的⽂档
 - `$project`： 修改输⼊⽂档的结构， 如重命名、 增加、 删除字段、 创建计算结果
 - `$sort`： 将输⼊⽂档排序后输出
 - `$limit`： 限制聚合管道返回的⽂档数
 - `$skip`： 跳过指定数量的⽂档， 并返回余下的⽂档
 常⽤表达式:

 - `$sum`： 计算总和， $sum:1 表示以⼀倍计数
 - `$avg`： 计算平均值
 - `$min`： 获取最⼩值
 - `$max`： 获取最⼤值
 - `$push`： 在结果⽂档中插⼊值到⼀个数组中


db.stu.aggregate(
    {$group:
        {
            _id:"$gender",
            counter:{$sum:1}
        }
    }
)
- `db.db_name.aggregate`是语法，所有的管道命令都需要写在其中
- `_id` 表示分组的依据，按照哪个字段进行分组，需要使用`$gender`表示选择这个字段进行分组
- `$sum:1` 表示把每条数据作为1进行统计，统计的是该分组下面数据的条数

db.stu.aggregate(
    {$group:
        {
            _id:null,
            counter:{$sum:1}
        }
    }
)
`_id:null` 表示不指定分组的字段，即统计整个文档，此时获取的`counter`表示整个文档的个数


db.stu.aggregate(
    {$group:
        {
            _id:null,
            name:{$push:"$$ROOT"}
        }
    }
)
使用`$$ROOT`可以将整个文档放入数组中


###Mongodb的索引操作
- 加快查询速度
- 进行数据的去重

语法：`db.集合名.ensureIndex({属性:1})`，1表示升序， -1表示降序


测试：插入10万条数据到数据库中

for(i=0;i<100000;i++){db.t1.insert({name:'test'+i,age:i})}

db.t1.find({name:'test10000'})db.t1.find({name:'test10000'}).explain('executionStats') # 显示查询操作的详细信息

db.t1.ensureIndex({name:1})

db.t1.find({name:'test10000'}).explain('executionStats')
默认情况下_id是集合的索引
查看方式：`db.集合名.getIndexes()`
语法：`db.集合名.dropIndex({'索引名称':1})` 删

db.集合名.ensureIndex({"字段名":1}, {"unique":true})

db.t1.ensureIndex({"name":1}, {"unique":true})
db.t1.insert({name: 'test10000'})

### 3. mongodb超级管理员账号的创建

#### 3.1 创建超级用户

进入mongo shell

```
sudo mongod
```

使用admin数据库(超级管理员账号必须创建在该数据库上)

```
use admin
```

创建超级用户

```
db.createUser({"user":"python","pwd":"python","roles":["root"]})
```

创建成功会显示如下信息

```
Successfully added user: { "user" : "python", "roles" : [ "root" ] }
```

退出mongo shell

```
exit
```

#### 3.2 以权限认证的方式启动mongodb数据库

```
sudo mongod --auth
```

启动之后在启动信息中会有如下信息，说明mongodb以权限认证的方式启动成功

```
[initandlisten] options: { security: { authorization: "enabled" } }
```


#### 3.3 登录验证

此时再使用数据库各命令的时候会报权限错误，需要认证才能执行相应操作、

```
use admin
db.auth('python','python')
```

- python用户是创建在admin数据库上的所以必须来到admin数据库上进行认证
- 认证成功会返回1，失败返回0

### 4. 创建普通用户

#### 4.1 在使用的数据库上创建普通用户

1.选择需要创建用户的数据库

```
use test1
```

2. 创建用户

```
db.createUser("user":"user1", "pwd":"pwd1", roles:["read"])
创建普通用户user1,该用户在test1上的权限是只读
db.createUser("user":"user1", "pwd":"pwd1", roles:["readWrite"])
创建普通用户user1,该用户在test1上的权限是读写
```

#### 4.2 在admin用户数据库上创建普通用户

```
use admin
db.createUser({"user":"python1", "pwd":"python1", roles:[{"role":"read","db":"dbname1"},{"role":"readWrite","db":"dbname2"}
]})
```

在admin上创建python1用户，python1用户的权限有两个，一个再dbname1上的只读，另一个是在dbname2上的读写

### 5. 查看创建的用户

```
show users
{
	"_id" : "admin.python",
	"user" : "python",
	"db" : "admin",
	"roles" : [
		{
			"role" : "root",
			"db" : "admin"
		}
	]
}
```

### 6. 删除用户

#### 6.1 进入账号数据所在的数据库

```
use db_name
```

#### 6.2 删除用户

```
db.dropUser('python')
```

## 小结

1. 了解mongodb的权限管理
2. 熟悉创建用户的相应流程

----

## mongodb和python交互

##### 学习目标

1. 掌握 mongdb和python交互的增删改查的方法
2. 掌握 权限认证的方式使用pymongo模块

----

### 1. mongdb和python交互的模块

`pymongo` 提供了mongdb和python交互的所有方法
安装方式: `pip install pymongo`

### 2. 使用pymongo

#### 2.1 导入pymongo并选择要操作的集合

> 数据库和集合能够自动创建

##### 2.1.1 无需权限认证的方式创建连接对象以及集合操作对象

```python
from pymongo import MongoClient

client = MongoClient(host,port) # 如果是本地连接host,port参数可以省略

collection = client[db名][集合名]
# collection = client.db名.集合名 # 与上边用法相同
```

##### 2.1.2 需要权限认证的方式创建连接对象以及集合操作对象

```python
from pymongo import MongoClient
from urllib.parse import quote_plus

user = 'python' # 账号
password = 'python' # 密码
host = '127.0.0.1' # host
port = 27017 # port
uri = "mongodb://%s:%s@%s" % (quote_plus(user),
                              quote_plus(password),
                              host)
# quote_plus函数：对url进行编码
# uri = mongodb://python:python@127.0.0.1
client = MongoClient(uri, port=port)
collection = client.db名.集合名
```

#### 2.2 insert()添加数据

> insert可以批量的插入数据列表，也可以插入一条数据

```python
collection.insert({一条数据})
collection.insert([{数据一},{数据二}])
```

##### 2.2.1 添加一条数据

> 返回插入数据的_id

```python
ret = collection.insert({"name":"test10010","age":33})
print(ret)
```

##### 2.2.2 添加多条数据

> 返回ObjectId对象构成的列表

```python
item_list = [{"name":"test1000{}".format(i)} for i in range(10)]
rets = collection.insert(item_list)
print(rets)
for ret in rets:
    print(ret)
```

#### 2.3 find_one()查找一条数据

> 接收一个字典形式的条件，返回字典形式的整条数据
> 如果条件为空，则返回第一条

```python
ret = client.test.test.find_one({'name': 'test10001'})
print(ret) # 包含mongodb的ObjectId对象的字典
_ = ret.pop('_id') # 清除mongodb的ObjectId对象的k,v
print(ret) 
```

#### 2.4 find()查找全部数据

> 返回所有满足条件的结果，如果条件为空，则返回全部
> 结果是一个Cursor游标对象，是一个可迭代对象，可以类似读文件的指针，但是只能够进行一次读取

```python
rets = collection.find({"name":"test10005"})，
for ret in rets:
    print(ret)
for ret in rets: #此时rets中没有内容
    print(ret)
```

#### 2.5 update()更新数据(全文档覆盖或指定键值，更新一条或多条)

- 语法：collection.update({条件}, {'$set':{指定的kv或完整的一条数据}}, multi=False/True, upsert=False/True)
- multi参数：默认为False,表示更新一条; multi=True则更新多条; multi参数必须和$set一起使用
- upsert参数：默认为False; upsert=True则先查询是否存在,存在则更新;不存在就插入
- $set表示指定字段进行更新

##### 2.5.1 更新一条数据；全文档覆盖；存在就更新，不存在就插入

```python
data = {'msg':'这是一条完整的数据1','name':'哈哈'}
client.test.test.update({'haha': 'heihei'}, {'$set':data}, upsert=True)
```

##### 2.5.2 更新多条数据；全文档覆盖；存在就更新，不存在就插入

```python
data = {'msg':'这是一条完整的数据2','name':'哈哈'} # 该完整数据是先查询后获取的
client.test.test.update({}, {'$set':data}, multi=True, upsert=True)
```

##### 2.5.3 更新一条数据；指定键值；存在就更新，不存在就插入

```python
data = {'msg':'指定只更新msg___1'}
client.test.test.update({}, {'$set':data}, upsert=True)
```

##### 2.5.4 更新多条数据；指定键值；存在就更新，不存在就插入

```python
data = {'msg':'指定只更新msg___2'}
client.test.test.update({}, {'$set':data}, multi=True, upsert=True)
```

#### 2.6 delete_one()删除一条数据

```python
collection.delete_one({"name":"test10010"})
```

#### 2.7 delete_many()删除全部数据

```python
collection.delete_many({"name":"test10010"})
```

### 3. pymongo模块其他api

> 查看pymongo官方文档或源代码 http://api.mongodb.com/python/current/

## 小结

1. 掌握pymongo的增删改查的使用
2. 掌握权限认证的方式使用pymongo模块

----



<img src="爬虫知识大总结.assets/7.mongodb总结.png" width = "100%" />

# scrapy爬虫框架







````

![image-20220926155515004](C:\Users\GREE\AppData\Roaming\Typora\typora-user-images\image-20220926155515004.png)

![image-20220926162547152](C:\Users\GREE\AppData\Roaming\Typora\typora-user-images\image-20220926162547152.png)

![image-20220926162559277](C:\Users\GREE\AppData\Roaming\Typora\typora-user-images\image-20220926162559277.png)

W3School官方文档：<http://www.w3school.com.cn/xpath/index.asp>

**PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript。下载地址：<http://phantomjs.org/download.html>**



#### 2.1 什么是tesseract

- Tesseract，一款由HP实验室开发由Google维护的开源OCR引擎，特点是开源，免费，支持多语言，多平台。
- 项目地址：https://github.com/tesseract-ocr/tesseract   

#### 2.4 图片识别引擎的使用扩展

- [tesseract简单使用与训练](https://www.cnblogs.com/cnlian/p/5765871.html)
- 

### 3 打码平台

#### 1.为什么需要了解打码平台的使用

现在很多网站都会使用验证码来进行反爬，所以为了能够更好的获取数据，需要了解如何使用打码平台爬虫中的验证码

#### 2 常见的打码平台

1. 云打码：http://www.yundama.com/

   能够解决通用的验证码识别

2. 极验验证码智能识别辅助：http://jiyandoc.c2567.com/

   能够解决复杂验证码的识别

<img src="./images/7.mongodb总结.png" width = "100%" />

![image-20221109110132405](%E7%88%AC%E8%99%AB%E4%BB%A3%E7%A0%81%E6%80%BB%E7%BB%93-mongdb.assets/image-20221109110132405.png)





# scrapy爬虫框架

- scrapy的概念作用和工作流程
- scrapy的入门使用
- scrapy构造并发送请求
- scrapy模拟登陆
- scrapy管道的使用
- scrapy中间件的使用	
- scrapy_redis概念作用和流程
- scrapy_redis原理分析并实现断点续爬以及分布式爬虫
- scrapy_splash组件的使用
- scrapy的日志信息与配置
- scrapyd部署scrapy项目



![image-20221109110431815](%E7%88%AC%E8%99%AB%E4%BB%A3%E7%A0%81%E6%80%BB%E7%BB%93-mongdb.assets/image-20221109110431815.png)



![image-20221109110522433](%E7%88%AC%E8%99%AB%E4%BB%A3%E7%A0%81%E6%80%BB%E7%BB%93-mongdb.assets/image-20221109110522433.png)

# scrapy的入门使用

### 1 掌握 scrapy的安装

​	pip install scrapy

### 2 scrapy项目开发流程

1. 创建项目:<br/>
   &ensp;&ensp;&ensp;&ensp;scrapy startproject mySpider
2. 生成一个爬虫:<br/>
   &ensp;&ensp;&ensp;&ensp;scrapy genspider itcast itcast.cn
3. 提取数据:<br/>
   &ensp;&ensp;&ensp;&ensp;根据网站结构在spider中实现数据采集相关内容
4. 保存数据:<br/>
   &ensp;&ensp;&ensp;&ensp;使用pipeline进行数据后续处理和保存



![image-20221109110954384](%E7%88%AC%E8%99%AB%E4%BB%A3%E7%A0%81%E6%80%BB%E7%BB%93-mongdb.assets/image-20221109110954384.png)

```python
#安装
pip install scrapy
#创建scrapy项目
scrapy startproject mySpider
#进入创建的项目目录
cd mySpider
#创建一个爬虫文件 scrapy genspider 《爬虫名字》 《允许爬取的域名》
scrapy genspider itcast itcast.cn


#开始完善爬虫提取数据
import scrapy

class ItcastSpider(scrapy.Spider):
    #爬虫名字
    name = 'itcast'
	#允许爬取的范围
	allowed_domains = ['itcast.cn']
    #开始爬取的url地址
    start_urls = ['http://xxxxx.itcast.cn/xxxxx']
	
    #数据提取的方法，接受下载中间件传过来的response
    def parse(self,response):
        #scrapy的response对象可以直接进行xpath
        names = response.xpath(' xxx/text()')
        print(names)
        
        #获取具体数据文本的方式如下
        #分组
        li_list= response.xpath('//xxx')
        for li in li_list:
            #创建一个数据字典
            item = {}
            #利用scrapy封装好的xpath选择器定位元素，并通过extract()或extract_frist()来获取结果
            item['name'] = li.xpath('./xx/text()').extract_first()#老师的名字
            item['level'] = li.xpath('./xx/text()').extract_first()#老师的级别
            print(item)
    '''
    注意：
    必须有名为parse的解析
    解析函数中提取的url地址如果要发送请求，则必须属于allowed_domains范围内
    项目路径下启动
    解析函数中的yield能够传递的对象只能是：BaseItem, Request, dict, None
    extract() -- >list
    extract_first()  -->第一个string

response响应对象的常用属性

1. response.url：当前响应的url地址
2. response.request.url：当前响应对应的请求的url地址
3. response.headers：响应头
4. response.requests.headers：当前响应的请求头
5. response.body：响应体，也就是html代码，byte类型
6. response.status：响应状态码
    
    
    '''        
    
    
    
    
    
    
    #保存数据 --》 pipeline
        
    import json
    
      #定义一个管道类
    class ItcastPipeline():
        #爬虫文件中提取数据的方法每yiled一次item，就会运行一次
        #该方法为固定名称函数
      #重写管道类方法的process_item
        def process_item(self,item,spider):
            print(item)
            
      #process_item方法处理完item之后必须返回给引擎
    		return item
 

# 注意：setting中需要配置启用管道
ITEM_PIPELINES = {
    'myspider.pipelines.ItcastPipeline': 400
}


'''
项目目录下执行scrapy crawl 《爬虫名字》

'''

   #### scrapy模拟登陆        
      #直接携带cookies
        #找到url地址，发送post请求储存cookie
            
#应用场景：如果start_url地址中的url是需要登录后才能访问的url地址，则需要重写start_request方法并在其中手动添加上cookie
        
import scrapy
import re

class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/NoobPythoner'] # 这是一个需要登陆以后才能访问的页面       
    #重写start_request方法并手动添加cookies
    def start_request(self):
        #这个cookies_str是抓包获取的
        cookies_str = "..." #抓包获取
        #将cookies_str 转换为cookies_dict
        cookies_dict = {i.split("=")[0]:i.split('=')[1] for i in cookies_str.split(";")}
        yield scrapy.Request(
        	self.start_urls[0],
            callback=self.parse,
            cookies=cookies_dict
        )
        
        
   def parse(self, response): # 通过正则表达式匹配用户名来验证是否登陆成功
        # 正则匹配的是github的用户名
        result_list = re.findall(r'noobpythoner|NoobPythoner', response.body.decode()) 
        print(result_list)
        pass     
        
     
```

```python
#####通常使用scrapy.FormRequest()来发送post请求

import scrapy
import re

class Login2Spider(scrapy.Spider):
   name = 'login2'
   allowed_domains = ['github.com']
   start_urls = ['https://github.com/login']

##1. 找到post的url地址：点击登录按钮进行抓包，然后定位url地址为https://github.com /session

#2. 找到请求体的规律：分析post请求的请求体，其中包含的参数均在前一次的响应中

#3. 否登录成功：通过请求个人主页，观察是否包含用户名
	
    def parse(self,response):
       authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
       utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
       commit = response.xpath("//input[@name='commit']/@value").extract_first()
       #构造POST请求，返回引擎
        yield scrapy.FormRequest(
        "https://github.com/session",
        formdata = {
            "authenticity_token":authenticity_token,
            "utf8":utf8,
            "commit":commit,
            "login":"noobpythoner",
            "password":"***"
            
            
        },
        callback = self.parse_login
        )
     
    def parse_login(self,response):
       ret = re.findall(r"noobpythoner|NoobPythoner",response.text)
       print(ret) 

#在settings.py中通过设置COOKIES_DEBUG=TRUE 能够在终端看到cookie的传递传递过程





```

```python
#scrapy管道
#pipeline
'''
### 1. pipeline中常用的方法：

1. process_item(self,item,spider): 
   - 管道类中必须有的函数
   - 实现对item数据的处理
   - 必须return item
2. open_spider(self, spider): 在爬虫开启的时候仅执行一次
3. close_spider(self, spider): 在爬虫关闭的时候仅执行一次
'''

import json
from pymongo import MongoClient

class WangyiFilePipeline(object):
    def opne_spider(self,spider): #爬虫开启的时候执行一次
        if spider.name == 'itcast':
            self.f = open('json.txt','a',encoding = 'utf-8')
            
    def close_spider(self,spider): #爬虫关闭的时候仅执行一次
        if spider.name == 'itcast':
            self.f.close()
    def process_item(self,item,spider):
        if spider.name == 'itcast':
            self.f.write(json.dumps(dict(item),ensure_assii = False , indent=2) + ",\n")
        # 不return的情况下，另一个权重较低的pipeline将不会获得item  
         return item

class WangyiMongoPipeline(object):
    def open_spider (self,spider):
        if spider.name == "itcast":
            con = MongoClient(host='127.0.0.1',port=27017)# 实例化mongoclient
            self.collection = con.itcast.teachers# 创建数据库名为itcast,集合名为teachers的集合操作对象
    def process_item(self,item,spider):
        if spider.name =='itcast':
            self.collection.insert(item)
            # 此时item对象必须是一个字典,再插入
            # 如果此时item是BaseItem则需要先转换为字典：dict(BaseItem)
        # 不return的情况下，另一个权重较低的pipeline将不会获得item
        return item  

    
###在settings.py设置开启pipeline
......
ITEM_PIPELINES = {
    'myspider.pipelines.ItcastFilePipeline': 400, # 400表示权重
    'myspider.pipelines.ItcastMongoPipeline': 500, # 权重值越小，越优先执行！
}
......
**别忘了开启mongodb数据库 ```sudo service mongodb start```**
**并在mongodb数据库中查看 ```mongo```**



```

```python
###scrapy中间件
##### 学习目标：

1. 应用 scrapy中使用间件使用随机UA的方法
2. 应用 scrapy中使用代理ip的的方法
3. 应用 scrapy与selenium配合使用

1、下载中间件
2、爬虫中间件
#####  scrapy中间的作用：预处理request和response对象

1. 对header以及cookie进行更换和处理
2. 使用代理ip等
3. 对请求进行定制化操作，

但在scrapy默认的情况下 两种中间件都在middlewares.py一个文件中

爬虫中间件使用方法和下载中间件相同，且功能重复，通常使用下载中间件



##> 编写一个Downloader Middlewares和我们编写一个pipeline一样，定义一个类，然后在setting中开启

#Downloader Middlewares默认的方法：


process_request(self, request, spider)：
      1. 当每个request通过下载中间件时，该方法被调用。
       2. 返回None值：没有return也是返回None，该request对象传递给下载器，或通过引擎传递给其他权重低的process_request方法
       3. 返回Response对象：不再请求，把response返回给引擎
       4. 返回Request对象：把request对象通过引擎交给调度器，此时将不通过其他权重低的process_request方法

process_response(self, request, response, spider)：
    1. 当下载器完成http请求，传递响应给引擎的时候调用
       2. 返回Resposne：通过引擎交给爬虫处理或交给权重更低的其他下载中间件的process_response方法
       3. 返回Request对象：通过引擎交给调取器继续请求，此时将不通过其他权重低的process_request方法

  - 在settings.py中配置开启中间件，权重值越小越优先执行

### 3. 定义实现随机User-Agent的下载中间件

#### 3.1 在middlewares.py中完善代码
'''
3.1 在middlewares.py中完善代码
3.2 在settings中设置开启自定义的下载中间件，设置方法同管道
3.3 在settings中添加UA的列表
'''
import random 
from Tencent.settngs import USER_AGENTS_LIST

class UserAgentMiddleware(object):
    def process_request(self,request,spider):
        user_agent = random.chice(USER_AGENTS_LIST)
        request.headers['User-Agent'] = user_agent
		#不写return
class CheckUA:
    def process_response(self,request,response,spider):
        print(request.header['User_Agent'])
        return response

##  settings中设置开启自定义的下载中间件  
DOWNLOADER_MIDDLEWARES = {
   'Tencent.middlewares.UserAgentMiddleware': 543, # 543是权重值
   'Tencent.middlewares.CheckUA': 600, # 先执行543权重的中间件，再执行600的中间件
}
##在settings中添加UA的列表
USER_AGENTS_LIST = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
]







```

```python
0#代理IP

1. 代理添加的位置：request.meta中增加`proxy`字段
2. 获取一个代理ip，赋值给`request.meta['proxy']`
   - 代理池中随机选择代理ip
   - 代理ip的webapi发送请求获取一个代理ip

class ProxyMiddleware(object):
    def process_request(self,request,spider):
        # proxies可以在settings.py中，也可以来源于代理ip的webapi
        # proxy = random.choice(proxies) 

        # 免费的会失效，报 111 connection refused 信息！重找一个代理ip再试
        proxy = 'https://1.71.188.37:3128' 

        request.meta['proxy'] = proxy
        return None # 可以不写return

    
    
# 人民币玩家的代码(使用abuyun提供的代理ip)
import base64

# 代理隧道验证信息  这个是在那个网站上申请的
proxyServer = 'http://proxy.abuyun.com:9010' # 收费的代理ip服务器地址，这里是abuyun
proxyUser = 用户名
proxyPass = 密码
proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # 设置代理
        request.meta["proxy"] = proxyServer
        # 设置认证
        request.headers["Proxy-Authorization"] = proxyAuth
    
    
class ProxyMiddleware(object):
    ......
    def process_response(self, request, response, spider):
        if response.status != '200':
            request.dont_filter = True # 重新发送的请求对象能够再次进入队列
            return requst   


在settings.py中开启该中间件

### 5. 在中间件中使用selenium

##> 以github登陆为例

import scrapy

class Login4Spider(scrapy.Spider):
    name = 'login4'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/1596930226'] # 直接对验证的url发送请求

    def parse(self, response):
        with open('check.html', 'w') as f:
            f.write(response.body.decode())
            
  ####中间件中使用selenium
import time
from selenium import webdriver


def getCookies():
    # 使用selenium模拟登陆，获取并返回cookie
    username = input('输入github账号:')
    password = input('输入github密码:')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver',
                              chrome_options=options)
    driver.get('https://github.com/login')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[3]').click()
    time.sleep(2)
    cookies_dict = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
    driver.quit()
    return cookies_dict

class LoginDownloaderMiddleware(object):

    def process_request(self, request, spider):
        cookies_dict = getCookies()
        print(cookies_dict)
        request.cookies = cookies_dict # 对请求对象的cookies属性进行替换         
            
            
```

# scrapy_redis概念作用和流程
