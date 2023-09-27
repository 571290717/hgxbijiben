import requests
from lxml import etree

url = 'http://admi.hnu.edu.cn/info/1026/2993.htm'  # url:统一资源定位符=协议部分+网址+文件地址部分
headers = {  # 请求头
    # 告诉HTTP服务器， 客户端使用的操作系统和浏览器的名称和版本.
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92'
                  ' Safari/537.36',
}

# 发送请求并解析HTML对象
response = requests.get(url, headers=headers)  # 请求获取获取html
html = etree.HTML(response.content.decode('utf-8'))  # 解析对象

p = html.xpath("//div[4]/div/p")  # 使用xpath定位到相应节点

dep = []
for i in p:
    data = {
        ''.join(i.xpath('.//strong//text()')),  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        ''.join(i.xpath('.//text()'))
    }
    print(data)
    dep.append(data)

# 数据存储
with open('湖南大学招生章程.txt', 'w', encoding='utf-8') as f:  # 使用with open()创建对象f
    for i in dep:
        f.write(str(i)+'\n')
