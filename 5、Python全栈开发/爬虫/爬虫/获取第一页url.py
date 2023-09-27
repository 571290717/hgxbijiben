import requests
from lxml import etree


for i in range(1,17):
    # print(i)
    # 目标url
    url = f'https://aii-alliance.org/index/c145.html?page={i}'
    print(url)

    # 向目标url发送get请求
    response = requests.get(url)

    html = etree.HTML(response.text)


    href_list = html.xpath("/html/body/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[2]/a/@href")


    for i in href_list:
        print('https://aii-alliance.org'+i)
        with open('url.txt', 'a') as f:
            f.write('https://aii-alliance.org'+i+'\n')
