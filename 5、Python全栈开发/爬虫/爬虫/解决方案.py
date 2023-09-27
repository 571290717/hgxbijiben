import requests
from lxml import etree
import time



def pdfload(text_name,pdfhref):
    import requests

    # 目标url
    url = pdfhref

    # 向目标url发送get请求
    response = requests.get(url)

    try:
        with open(text_name, 'wb') as f:
            f.write(response.content)
    except:
        with open('/workspace/programming-language-demo/解决方案/111111报错了请手动输入名字.pdf', 'wb') as f:
            f.write(response.content)

    print('成功1个')
    time.sleep(1)


for i in range(1,5):
    # print(i)
    # 目标url
    url = f'https://aii-alliance.org/index/c156.html?page={i}'
    print(url)

    # 向目标url发送get请求
    response = requests.get(url)

    html = etree.HTML(response.text)


    href_list = html.xpath("/html/body/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[2]/a/@href")


    for i in href_list:
        text_url= 'https://aii-alliance.org'+i
        print(text_url)
        # with open('url.txt', 'a') as f:
        #     f.write('https://aii-alliance.org'+i+'\n')
        # 目标url
        # url = 'https://aii-alliance.org/index/c317/n4140.html'

        # 向目标url发送get请求
        response2 = requests.get(text_url)

        html = etree.HTML(response2.text)


        # 文件名称
        title_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/h2/text()")
        text_name = f"/workspace/programming-language-demo/解决方案/{str(title_list[0])}.pdf"
        # text_name2 = f"/workspace/programming-language-demo/解决方案/'{str(title_list[0])}'.pdf"

        # next_href_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[4]/div[2]/a/@href")
        # next_href = 'https://aii-alliance.org'+next_href_list[0]

        # pdf链接
        pdfhref_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[1]/div[2]/a/@href")
        print(pdfhref_list)
        try:
            pdfhref = 'https://aii-alliance.org'+pdfhref_list[0]
        except:
            continue

        print(text_name)
        print(pdfhref)
        pdfload(text_name, pdfhref)







