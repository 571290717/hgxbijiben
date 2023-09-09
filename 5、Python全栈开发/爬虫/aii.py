# 1.2.3-response其它常用属性
import requests

# 目标url
url = 'https://www.baidu.com'

# 向目标url发送get请求
response = requests.get(url)

# 打印响应内容
# print(response.text)
# print(response.content.decode()) 			# 注意这里！
print(response.url)							# 打印响应的url
print(response.status_code)					# 打印响应的状态码
print(response.request.headers)				# 打印响应对象的请求头
print(response.headers)						# 打印响应头
print(response.request._cookies)			# 打印请求携带的cookies
print(response.cookies)						# 打印响应中携带的cookies

import requests
import json


class King(object):

    def __init__(self, word):
        self.url = "http://fy.iciba.com/ajax.php?a=fy"
        self.word = word
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.post_data = {
            "f": "auto",
            "t": "auto",
            "w": self.word
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.post_data)
        # 默认返回bytes类型，除非确定外部调用使用str才进行解码操作
        return response.content

    def parse_data(self, data):

        # 将json数据转换成python字典
        dict_data = json.loads(data)

        # 从字典中抽取翻译结果
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])

    def run(self):
        # url
        # headers
        # post——data
        # 发送请求
        data = self.get_data()
        # 解析
        self.parse_data(data)

if __name__ == '__main__':
    # king = King("人生苦短，及时行乐")
    king = King("China")
    king.run()
    # python标准库有很多有用的方法，每天看一个标准库的使用





import requests
import jsonpath
import json

# 获取拉勾网城市json字符串
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
response =requests.get(url, headers=headers)
html_str = response.content.decode()

# 把json格式字符串转换成python对象
jsonobj = json.loads(html_str)

# 从根节点开始，获取所有key为name的值
citylist = jsonpath.jsonpath(jsonobj,'$..name')

# 写入文件
with open('city_name.txt','w') as f:
    content = json.dumps(citylist, ensure_ascii=False)
    f.write(content)


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

find_element_by_id 						(返回一个元素)
find_element(s)_by_class_name 			(根据类名获取元素列表)
find_element(s)_by_name 				(根据标签的name属性值返回包含标签对象元素的列表)
find_element(s)_by_xpath 				(返回一个包含元素的列表)
find_element(s)_by_link_text 			(根据连接文本获取元素列表)
find_element(s)_by_partial_link_text 	(根据链接包含的文本获取元素列表)
find_element(s)_by_tag_name 			(根据标签名获取元素列表)
find_element(s)_by_css_selector 		(根据css选择器来获取元素列表)
1. `driver.page_source` 当前标签页浏览器渲染之后的网页源代码
2. `driver.current_url` 当前标签页的url
3. `driver.close()` 关闭当前标签页，如果只有一个标签页则关闭整个浏览器
4. `driver.quit()` 关闭浏览器
5. `driver.forward()` 页面前进
6. `driver.back()` 页面后退
7. `driver.screen_shot(img_name)` 页面截图
- by_link_text和by_partial_link_tex的区别：全部文本和包含某个文本
- 以上函数的使用方法
  - `driver.find_element_by_id('id_str')`




> find_element仅仅能够获取元素，不能够直接获取其中的数据，如果需要获取数据需要使用以下方法

- 对元素执行点击操作
`element.click()`

- 对定位到的标签对象进行点击操作

- 向输入框输入数据
`element.send_keys(data)`

- 对定位到的标签对象输入数据

- 获取文本
`element.text`

- 通过定位获取的标签对象的
`text`
属性，获取文本内容

- 获取属性值
`element.get_attribute("属性名")`

- 通过定位获取的标签对象的
`get_attribute`
函数，传入属性名，来获取属性的值


​

- 代码实现，如下：

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.itcast.cn/')

ret = driver.find_elements_by_tag_name('h2')
print(ret[0].text)  #

ret = driver.find_elements_by_link_text('黑马程序员')
print(ret[0].get_attribute('href'))

driver.quit()
```

----

##### 知识点：掌握 元素对象的操作方法




"""操作frame外边的元素需要切换出去"""
windows = driver.window_handles
driver.switch_to.window(windows[0])



js = 'window.scrollTo(0,document.body.scrollHeight)' # js语句
driver.execute_script(js) # 执行js的方法