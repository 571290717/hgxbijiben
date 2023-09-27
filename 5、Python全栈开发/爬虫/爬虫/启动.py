import requests
import time
from lxml import etree
#逻辑： 进入白皮书首页： 点击下载pdf 休息10s 进入下一篇   。。。点击下载pdf 休息10s 进入下一篇


def start(next_href):
    # 1.2.3-response其它常用属性
    import requests

    # 目标url
    url = next_href

    # 向目标url发送get请求
    response = requests.get(url)

    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.headers)
        with open('spider2.txt', 'w') as f:
            f.write(r.text)
    except:
        print("失败了")


# def getpdfhref():
#     with open('spider.txt', 'r') as f:
#         text = f.read()
#     html = etree.HTML(text)
#     title_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/h2/text()")
#     text_name = f"/workspace/programming-language-demo/白皮书/{str(title_list[0])}.pdf"
#     next_href_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[4]/div[2]/a/@href")
#     next_href = 'https://aii-alliance.org'+next_href_list[0]
#     pdfhref_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[1]/div[2]/a/@href")
#     pdfhref = 'https://aii-alliance.org'+pdfhref_list[0]
#     return pdf_href,text_name,next_href



def loadpdf(pdf_href,text_name):
    # 目标url
    print(pdf_href)
    url = str(pdf_href)

    # 向目标url发送get请求
    response = requests.get(url)


    with open(text_name, 'wb') as f:
        f.write(response.content)
    
    time.sleep(10)




if __name__ =="__main__":
    try:
        while True:
            with open('spider2.txt', 'r') as f:
                text = f.read()
            html = etree.HTML(text)
            title_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/h2/text()")
            text_name = f"/workspace/programming-language-demo/白皮书/{str(title_list[0])}.pdf"
            next_href_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[4]/div[2]/a/@href")
            next_href = 'https://aii-alliance.org'+next_href_list[0]
            pdfhref_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[1]/div[2]/a/@href")
            pdfhref = 'https://aii-alliance.org'+pdfhref_list[0]
            print(next_href)
            start(next_href)
            print(pdfhref,text_name)

            with open('pdfhref.txt', 'a') as f:

                f.write(text_name+'\n')
                f.write(pdfhref+'\n')
            time.sleep(1)
            # url = pdf_href
            # # 向目标url发送get请求
            # response = requests.get(url)
            # with open(text_name, 'wb') as f:
            #     f.write(response.content)
            # time.sleep(10)

    except:
        print("请检查~")
