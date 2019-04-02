#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1,正则表达式：编写一些规范查找需要的字符串
2，组成：原义字符和元字符
3，如何python解析
4，使用场景
--参数化
--查找一些特殊的字符：邮箱，手机号，身份证号
'''
import re
from future_3.common.configrue_msg import ConfigParser
from future_3.common.get_data import GetData


class Re:
    '''正则表达式函数'''

    def re(self, target, p='#(.*?)#'):
        while re.search(p, target):
            m = re.search(p, target)
            key = m.group(1)
            value = getattr(GetData, key)
            target = re.sub(p, value, target, count=1)
        return target


if __name__ == '__main__':
    target = "{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
    # p = '#(.*?)#'
    t = Re().re(target)
    print(t)
