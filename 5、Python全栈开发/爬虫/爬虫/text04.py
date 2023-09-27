import requests
from lxml import etree

num=2
# 目标url
url = 'https://aii-alliance.org/index/c317/n4140.html'

# 向目标url发送get请求
response = requests.get(url)

html = etree.HTML(response.text)


# 文件名称
title_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/h2/text()")
text_name = f"/workspace/programming-language-demo/白皮书/{str(title_list[0])}.pdf"


# next_href_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[4]/div[2]/a/@href")
# next_href = 'https://aii-alliance.org'+next_href_list[0]

# pdf链接
pdfhref_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[1]/div[2]/a/@href")
pdfhref = 'https://aii-alliance.org'+pdfhref_list[0]

print(text_name)
print(pdfhref)



def pdfload(text_name,pdfhref):
    import requests

    # 目标url
    url = pdfhref

    # 向目标url发送get请求
    response = requests.get(url)


    with open(text_name, 'wb') as f:
        f.write(response.content)



pdfload(text_name, pdfhref)