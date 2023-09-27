from lxml import etree




with open('spider2.txt', 'r') as f:
    text = f.read()

html = etree.HTML(text)
#获取title的列表和text的列表
title_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/h2/text()")
next_href_list = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[4]/div[2]/a/@href")


p = html.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[3]/p")  # 使用xpath定位到相应节点，返回一个列表

text_list = []  # 新建一个列表，用来存储每一条数据
for i in p:
    data = i.xpath('.//text()')
    text_list.append(data)

text_name = f"/workspace/programming-language-demo/白皮书/{str(title_list[0])}.txt"

next_href = 'https://aii-alliance.org'+next_href_list[0]
print(next_href)


with open(text_name, 'a') as f:
    for i in title_list:
        f.write(i)
        f.write('\n')
        f.write('\n')
        f.write(f"原文地址：{next_href}\n")

    for i in text_list:
        for j in i:
            f.write('\n')
            f.write(str(j))