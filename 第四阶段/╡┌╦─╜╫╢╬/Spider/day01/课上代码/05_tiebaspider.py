from urllib import request,parse
import time
import random
from useragents import ua_list

class TiebaSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'

    # 请求
    def get_html(self,url):
        req = request.Request(
            url=url,
            headers={'User-Agent':random.choice(ua_list)}
        )
        res = request.urlopen(req)
        html = res.read().decode('utf-8','ignore')

        return html

    # 解析
    def parse_html(self):
        pass

    # 保存
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    # 入口函数
    def run(self):
        name = input('请输入贴吧名:')
        begin = int(input('请输入起始页:'))
        stop = int(input('请输入终止页:'))
        # 拼接地址,发请求
        for page in range(begin,stop+1):
            pn = (page-1)*50
            params = {
                'kw' : name,
                'pn' : str(pn)
            }
            params = parse.urlencode(params)
            url = self.url.format(params)
            html = self.get_html(url)
            filename = '{}-第{}页.html'.format(name,page)
            self.save_html(filename,html)
            # 提示
            print('第%d页抓取成功' % page)
            # 每爬取1个页面随机休眠1-3秒钟
            time.sleep(random.randint(1,3))
            time.sleep(random.uniform(0,1))

if __name__ == '__main__':
    start = time.time()
    spider = TiebaSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-start))































