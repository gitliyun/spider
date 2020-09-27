import urllib.request

url = 'http://httpbin.org/get'
# 1.创建请求对象
req = urllib.request.Request(
    url=url,
    headers={'User-Agent':'Mozilla/5.0'}
)
# 2.发请求获取响应对象
res = urllib.request.urlopen(req)
# 3.提取响应对象内容
html = res.read().decode()

print(html)














