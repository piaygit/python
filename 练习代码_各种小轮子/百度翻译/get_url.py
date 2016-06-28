# -*-coding=utf-8 -*-
import urllib
from baidu_fanyi import get_word
import md5, random, requests,sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'piay'
'''
http://api.fanyi.baidu.com/api/trans/vip/translate
http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4
'''


class get_url(object):
    def __init__(self):
        self.word = get_word.get_word()
        self.appid = '20160628000024166'
        self.key = 'hEdErWqx5zjTVwoixr3G'
        self.url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        self.q = self.word.getword()

    def get_pargms(self):
        '''
        构造url参数
        :return:
        '''
        random_number = random.randint(1000, 9999)
        # 将翻译的文本处理为utf-8
        q=self.q.encode('utf-8')
        print type(q)
        def get_singed():
            '''
            生成签名
            签名生成方法如下：
            1、将请求参数中的 APPID(appid), 翻译query(q, 注意为UTF-8编码), 随机数(salt), 以及平台分配的密钥
            按照 appid+q+salt+密钥 的顺序拼接得到字符串1。
            2、对字符串1做md5，得到32位小写的sign。
            :return:
            '''
            singed = self.appid + q + str(random_number) + self.key
            m1 = md5.new()
            m1.update(singed)
            # 生成签名
            return m1.hexdigest()

        self.pargms = {}
        self.pargms['q'] = urllib.quote(self.q)
        self.pargms['from'] = 'zh'
        self.pargms['to'] = 'en'
        self.pargms['appid'] = self.appid
        self.pargms['salt'] = random_number
        self.pargms['sign'] = get_singed()
        if self.pargms is not None and len(self.pargms) != 0:
            return self.pargms
        else:
            print '构造url参数失败，请检查程序'


    def get_query(self):
        result = requests.get(self.url, params=self.get_pargms())
        result.encoding='utf-8'
        if result.status_code == 200:
            result = result.text
            return result
        else:
            print '请求链接返回错误为：%s' % (result.status_code)
            return 'error'


