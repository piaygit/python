# -*-coding=utf-8 -*-
__author__ = 'piay'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''
http://fanyi.youdao.com/openapi.do?keyfrom=<keyfrom>&key=<key>&type=data&doctype=<doctype>&version=1.1&q=要翻译的文本
版本：1.1，请求方式：get，编码方式：utf-8
主要功能：中英互译，同时获得有道翻译结果和有道词典结果（可能没有）
参数说明：
　type - 返回结果的类型，固定为data
　doctype - 返回结果的数据格式，xml或json或jsonp
　version - 版本，当前最新版本为1.1
　q - 要翻译的文本，必须是UTF-8编码，字符长度不能超过200个字符，需要进行urlencode编码
　only - 可选参数，dict表示只获取词典数据，translate表示只获取翻译数据，默认为都获取
　注： 词典结果只支持中英互译，翻译结果支持英日韩法俄西到中文的翻译以及中文到英语的翻译
errorCode：
　0 - 正常
　20 - 要翻译的文本过长
　30 - 无法进行有效的翻译
　40 - 不支持的语言类型
　50 - 无效的key
　60 - 无词典结果，仅在获取词典结果生效
'''

import requests


class youdao_fanyi(object):
    def __init__(self, appkey):
        if isinstance(appkey, dict):
            self.version = 1.1  # 版本号
            self.errorCode = None  # 状态码
            self.keyfrom = appkey['keyfrom']
            self.key = appkey['key']
            self.doctype = ['xml', 'json', 'jsonp']  # 返回数据格式
            self.url = 'http://fanyi.youdao.com/openapi.do'  # 接口
            self.type = 'data'
            self.q = ''  # 翻译的文本
        else:
            print 'error'


    def _pargmas_data(self, i=1):
        '''

        :param i: 返回数据格式，默认为json格式
        :return:pargmas 返回构建数据
        '''
        pargmas = {}
        pargmas['version'] = self.version
        pargmas['keyfrom'] = self.keyfrom
        pargmas['key'] = self.key
        pargmas['doctype'] = self.doctype[i]  # 获取什么格式的数据，0：xml，1:json 2:jsonp
        pargmas['type'] = self.type
        return pargmas

    def _get_fanyi_json(self):
        dict_data = self._pargmas_data()
        text = raw_input("请输入需要翻译的单词：")
        dict_data['q'] = text
        result = requests.get(self.url, params=dict_data)
        self.errorCode = result.status_code
        if self.errorCode == 0:
            pass
        elif self.errorCode == 20:
            print ('要翻译的文本过长')
            return self._get_fanyi_json()
        elif self.errorCode == 30:
            print ('无法进行有效的翻译')
            return self._get_fanyi_json()
        elif self.errorCode == 40:
            print ('不支持的语言类型')
            return self._get_fanyi_json()
        elif self.errorCode == 50:
            print ('无效的key')
            return self._get_fanyi_json()
        elif self.errorCode == 60:
            print ('无词典结果，仅在获取词典结果生效')
            return self._get_fanyi_json()
        result = result.text
        return result

    def analysis_json(self):
        result_json_data=self._get_fanyi_json()
        import json
        result=json.loads(result_json_data)
        print result['translation']


app_key_data = {'key': '61555165', 'keyfrom': 'pythoncontent1111'}
m = youdao_fanyi(app_key_data)
m.analysis_json()



