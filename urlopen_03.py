from urllib import request

# 1、构造请求对象(重构User-Agent)
url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
# 2、发请求获取响应对象(urlopen)
req = request.Request(
    url=url,
    headers=headers)
# 3、获取响应对象内容
res = request.urlopen(req)
html = res.read().decode()
print(html)