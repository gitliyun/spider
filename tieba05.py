from urllib import request,parse
import time
import random
from useragents import ua_list
from fake_useragent import UserAgent

class TiebaSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
    # 生成随机的User_Agent
    def get_headers(self):
        ua = UserAgent()
        headers = {'user_Agent':ua.random}
        return headers
    # 请求取响应内容
    def get_html(self,url):
        headers = self.get_headers()
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        return html

    # 解析
    def parse_html(self):
        pass

    # 保存数据
    def write_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    # 入口函数
    def run(self):
        name = input('请输入贴吧名:')
        begin = int(input('请输入起始页:'))
        stop = int(input('请输入终止页:'))
        kw = parse.quote(name)
        # 拼接地址,发请求，保存内容
        for i in range(begin,stop+1):
            pn = (i-1)*50
            # params = {'kw' : name,'pn' : str(pn)}
            # params = parse.urlencode(params)
            url = self.url.format(kw,pn)
            html = self.get_html(url)
            filename = '{}-第{}页.html'.format(name,i)
            self.write_html(filename,html)
            # 提示
            print('第%d页抓取成功' % i)
            # 每爬取1个页面随机休眠1-3秒钟
            time.sleep(random.randint(1,3))
            # time.sleep(random.uniform(0,1))

if __name__ == '__main__':
    start = time.time()
    spider = TiebaSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-start))































