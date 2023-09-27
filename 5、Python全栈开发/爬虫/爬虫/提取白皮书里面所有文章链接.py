import requests
from lxml import etree

num=2
# 目标url
url = f'https://aii-alliance.org/index/c145.html?page={num}'

# 向目标url发送get请求
response = requests.get(url)

html = etree.HTML(response.text)





title_list = html.xpath("/html/body/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[2]/a/text()")
href_list = html.xpath("/html/body/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[2]/a/@href")




p = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[3]/p")  # 使用xpath定位到相应节点，返回一个列表

text_list = []  # 新建一个列表，用来存储每一条数据
for i in p:
    data = i.xpath('.//text()')
    text_list.append(data)



print(title_list,href_list)
# /html/body/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[2]/a



