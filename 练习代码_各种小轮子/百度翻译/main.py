# -*-coding=utf-8 -*-
from baidu_fanyi import get_url

__author__ = 'piay'
import json,urllib


class main_fanyi(object):
    def __init__(self):
        self._result_data = get_url.get_url()


    def to_query(self):
        '''
        带错误码格式：{u'error_code': u'54001', u'error_msg': u'Invalid Sign'}
        正确返回结果：{u'to': u'zh', u'from': u'zh', u'trans_result': [{u'src': u'1', u'dst': u'1'}]}
        :return:
        '''
        # 获取返回的翻译结果
        result = self._result_data.get_query()
        # json 处理为字典
        result = json.loads(result)
        if result is not None and result != 0:
            # 获取返回的error_code,如果为正确的翻译，error_code为0
            try:
                error_code = result['error_code']
            except:
                error_code = 0
            if error_code == 0:
                # 正常返回翻译结果
                print result
                trans_result=result['trans_result'][0]['dst']
                print trans_result,type(trans_result)
            elif error_code == '52001':
                print '请求超时:请重试'
            elif error_code == '52002':
                print '系统错误:请重试'
            elif error_code == '52003':
                print '未授权用户:检查您的appid是否正确'
            elif error_code == '54000':
                print '必填参数为空:检查是否少传参数'
            elif error_code == '58000':
                print '客户端IP非法：检查您填写的IP地址是否正确可修改您填写的服务器IP地址'
            elif error_code == '54001':
                print '签名错误:请检查您的签名生成方法'
            elif error_code == '54003':
                print '访问频率受限:请降低您的调用频率'
            elif error_code == '58001':
                print '译文语言方向不支持:检查译文语言是否在语言列表里'
            elif error_code == '54004':
                print '账户余额不足:前往管理控制台为账户充值'
            elif error_code == '54005':
                print '长query请求频繁:请降低长query的发送频率，3s后再试'

        else:
            print '获取的结果错误，请检查'


m = main_fanyi()
m.to_query()
