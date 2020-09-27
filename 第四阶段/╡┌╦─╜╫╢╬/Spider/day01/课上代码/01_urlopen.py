'''向百度发请求,并得到响应'''
import urllib.request

# 得到: 响应对象
res = urllib.request.urlopen('http://httpbin.org/get')
# 获取响应内容
html = res.read().decode()
url = res.geturl()
code = res.getcode()
print(html)












