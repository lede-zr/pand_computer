#!/usr/bin/env python
# -*- coding: utf-8 -*-
from future_3.common.configrue_msg import ReadConfig
from future_3.common import project_path
import re
config = ReadConfig(project_path.conf_path)

class GetData:
    COOKIE = None
    LOAN_ID = None
    normal_user = config.get_str('EXCEL_DATA','normal_user')
    normal_pwd = config.get_str('EXCEL_DATA','normal_pwd')
    normal_member_id = config.get_str('EXCEL_DATA','normal_member_id')
    loan_id = config.get_str('EXCEL_DATA','loan_id')
def replace(target, p='#(.*?)#'):
    while re.search(p, target):
        m = re.search(p, target)
        key = m.group(1)
        value = getattr(GetData, key)
        target = re.sub(p, value, target, count=1)
    return target
if __name__ == '__main__':

    b = hasattr(GetData,'COOKIE')
    c = setattr(GetData,'COOKIE','123456')
    a = getattr(GetData, 'COOKIE')
    print(a)
    print(b)
    print(getattr(GetData,'COOKIE'))