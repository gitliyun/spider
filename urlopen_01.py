# 向百度发请求，得到响应内容

import urllib.request
# res为对象
res = urllib.request.urlopen('http://www.baidu.com/')
html = res.read().decode()
#返回HTTP响应码

