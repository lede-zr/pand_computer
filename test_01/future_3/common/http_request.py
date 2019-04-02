#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class HttpRequest:
    '''该类完成http的get或post请求，并返回结果'''

    def http_request(self, method, url, param,cookie=''):
        '''根据请求方法来决定发起的请求方式
        method：get post，http请求方式
        url：发送请求的接口地址
        param：随接口发送的请求参数
        rtype：有返回值
        '''
        global resp
        if method.upper() == 'GET':
            try:
                resp = requests.get(url, params=param,cookies = cookie)
            except Exception as e:
                print('get请求出错了：{}'.format(e))
        elif method.upper() == 'POST':
            try:
                resp = requests.post(url, data=param,cookies = cookie)
            except Exception as e:
                print('post请求出错了：{}'.format(e))
        else:
            print('不支持该种方式')
            resp = None
        return resp


if __name__ == '__main__':
    t = HttpRequest()
    param = {'mobilephone': '13312345678', 'pwd': '123456'}
    res_1 = t.http_request('get', 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', param)
    # cookie = res_1.cookies
    # param_1 = {'memberId':1116206,'title':'zr的标','amount':'1000','loanRate':'10','loanTerm':'6','loanDateType':0,'repaymemtWay':4,'biddingDays':10}
    # res = t.http_request('get', 'http://47.107.168.87:8080/futureloan/mvc/api/loan/add', param_1,cookie)
    # param ={'mobilephone':'13321345684','amount':'100'}
    # res = t.http_request('post', 'http://120.78.128.25:8080/futureloan/mvc/api/member/recharge', param)
    print(res_1.json())
