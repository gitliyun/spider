from urllib import request,parse

# 1.拼url地址
# 'http://www.baidu.com/s?wd=??'
def get_url(word):
    baseurl = 'http://www.baidu.com/s?wd='
    #编码＋拼接
    params = parse.quote(word)
    url = baseurl + params
    print(url)
    return url
# 2.发请求保存到本地
# 1.创建请求对象-Request
# 2.获取响应对象-urlopen
# 3.获取响应内容-readxxxx
def write_html(url,word):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    # 保存到本地文件
    filename = word + '.html'
    with open(filename,'w') as f:
        f.write(html)
#主程序入口
if __name__=='__main__':
    word = input('请输入要搜索的内容：')
    url = get_url(word)
    write_html(url,word)










