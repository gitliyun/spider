from urllib import request,parse

# 1.拼url地址
# 'http://www.baidu.com/s?wd=??'
url = 'http://www.baidu.com/s?{}'
word = input('请输入搜索内容:')
params = parse.urlencode({'wd':word})
full_url = url.format(params)
# 2.发请求保存到本地
# 1.创建请求对象-Request
# 2.获取响应对象-urlopen
# 3.获取响应内容-readxxxx
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
req = request.Request(url=full_url,headers=headers)
res = request.urlopen(req)
html = res.read().decode()
# 保存到本地文件
filename = word + '.html'
with open(filename,'w') as f:
    f.write(html)












