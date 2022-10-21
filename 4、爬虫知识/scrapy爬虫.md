## scrapy爬虫框架

少量的代码，就能够快速的抓取

<img src="scrapy%E7%88%AC%E8%99%AB.assets/1.3.1.%E7%88%AC%E8%99%AB%E6%B5%81%E7%A8%8B-1.png" width = "80%" />



![image-20221011143037316](scrapy%E7%88%AC%E8%99%AB.assets/image-20221011143037316.png)





<img src="scrapy%E7%88%AC%E8%99%AB.assets/1.3.3.scrapy%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B.png" width = "140%" />

##### 其流程可以描述如下：

1. 爬虫中起始的url构造成request对象-->爬虫中间件-->引擎-->调度器
2. 调度器把request-->引擎-->下载中间件--->下载器
3. 下载器发送请求，获取response响应---->下载中间件---->引擎--->爬虫中间件--->爬虫
4. 爬虫提取url地址，组装成request对象---->爬虫中间件--->引擎--->调度器，重复步骤2
5. 爬虫提取数据--->引擎--->管道处理和保存数据

掌握scrapy中每个模块的作用：
引擎(engine)：负责数据和信号在不同模块间的传递
调度器(scheduler)：实现一个队列，存放引擎发过来的request请求对象
下载器(downloader)：发送引擎发过来的request请求，获取响应，并将响应交给引擎
爬虫(spider)：处理引擎发过来的response，提取数据，提取url，并交给引擎
管道(pipeline)：处理引擎传递过来的数据，比如存储
下载中间件(downloader middleware)：可以自定义的下载扩展，比如设置代理ip
爬虫中间件(spider middleware)：可以自定义request请求和进行response过滤，与下载中间件作用重复



```
pip  install scrapy  

scrapy startproject mySpider
cd mySpider
scrapy genspider itcast itcast.cn

```



![image-20221011143848493](scrapy%E7%88%AC%E8%99%AB.assets/image-20221011143848493.png)



### 5. 完善爬虫

> 在上一步生成出来的爬虫文件中编写指定网站的数据采集操作，实现数据提取

#### 5.1 在/myspider/myspider/spiders/itcast.py中修改内容如下:

```python

import scrapy

class ItcastSpider(scrapy.Spider):
    #爬虫名字
    name = 'xxxx'
	#允许爬取的范围
    allowed_domains = ['xxxxxxx']
    #开始爬取的url地址
    start_urls = ['XXXXXXx']
	 # 数据提取的方法，接受下载中间件传过来的response
    def parse(self, response): 
        XXXXXX

		# scrapy的response对象可以直接进行xpath
    	names = response.xpath('//div[@class="tea_con"]//li/div/h3/text()') 
    	print(names)

    	# 获取具体数据文本的方式如下
        # 分组
    	li_list = response.xpath('//div[@class="tea_con"]//li') 
        for li in li_list:
        	# 创建一个数据字典
            item = {}
            # 利用scrapy封装好的xpath选择器定位元素，并通过extract()或extract_first()来获取结果
            item['name'] = li.xpath('.//h3/text()').extract_first() # 老师的名字
            item['level'] = li.xpath('.//h4/text()').extract_first() # 老师的级别
            item['text'] = li.xpath('.//p/text()').extract_first() # 老师的介绍
            print(item)


- response.url：当前响应的url地址
- response.request.url：当前响应对应的请求的url地址
- response.headers：响应头
- response.requests.headers：当前响应的请求头
- response.body：响应体，也就是html代码，byte类型
- response.status：响应状态码

利用管道pipeline来处理(保存)数据


import json

class ItcastPipeline():
    # 爬虫文件中提取数据的方法每yield一次item，就会运行一次
    # 该方法为固定名称函数
    def process_item(self, item, spider):
        print(item)
        return item







```



#### 6.2 在settings.py配置启用管道

```
ITEM_PIPELINES = {
    'myspider.pipelines.ItcastPipeline': 400
}
```

配置项中键为使用的管道类，管道类使用.进行分割，第一个为项目目录，第二个为文件，第三个为定义的管道类。<br/>
配置项中值为管道的使用顺序，设置的数值约小越优先执行，该值一般设置为1000以内。<br/>



### 7. 运行scrapy

命令：在项目目录下执行scrapy crawl <爬虫名字>

示例：scrapy crawl itcast



#### 2.2 携带cookies登陆github

```python

import scrapy 
import re

class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/NoobPythoner'] # 这是一个需要登陆以后才能访问的页面
	def start_requests(self):
        #重构start_requests方法
        #这个cookies_str是抓包获取
        cookies_str = '...'
        #将 将cookies_str转换为cookies_dict
     	cookies_dict = {i.split('=')[0]:i.split('=')[1] for i in cookies_str.split('; ')}
        
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

### 3. scrapy.Request发送post请求

>我们知道可以通过scrapy.Request()指定method、body参数来发送post请求；但是通常使用scrapy.FormRequest()来发送post请求

```python
import scrapy
import re

class Login2Spider(scrapy.Spider):
   name = 'login2'
   allowed_domains = ['github.com']
   start_urls = ['https://github.com/login']

   def parse(self, response):
       authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
       utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
       commit = response.xpath("//input[@name='commit']/@value").extract_first()
        
        #构造POST请求，传递给引擎
       yield scrapy.FormRequest(
           "https://github.com/session",
           formdata={
               "authenticity_token":authenticity_token,
               "utf8":utf8,
               "commit":commit,
               "login":"noobpythoner",
               "password":"***"
           },
           callback=self.parse_login
       )

   def parse_login(self,response):
       ret = re.findall(r"noobpythoner|NoobPythoner",response.text)
       print(ret)
```



1. start_urls中的url地址是交给start_request处理的，如有必要，可以重写start_request函数
2. 直接携带cookie登陆：cookie只能传递给cookies参数接收
3. scrapy.Request()发送post请求







