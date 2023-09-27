import requests

# 目标url
url = 'https://aii-alliance.org/uploads/1/20230815/d6424c1b0508b0d97856432c659569c3.pdf'

# 向目标url发送get请求
response = requests.get(url)


with open('metadata.pdf', 'wb') as f:
    f.write(response.content)