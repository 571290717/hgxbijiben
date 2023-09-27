# 1.2.3-response其它常用属性
import requests

# 目标url
url = 'https://aii-alliance.org/index/c317/n4140.html'

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
# print(response.title)					


try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.headers)
    with open('spider2.txt', 'w') as f:
        f.write(r.text)
except:
    print("失败了")