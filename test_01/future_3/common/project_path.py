# -*- coding: utf-8 -*-
# @time : 2019/3/14 21:40
# @Author : zr
# @Email : 429082323@qq.com
# @File : project_path.py.py

import os
#获取相对路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#获取用例的绝对路径
cases_path = os.path.join(project_path, 'test_cases', 'futurecase.xlsx')
#获取测试报告的绝对路径
result_path = os.path.join(project_path, 'result', 'test_report', 'futurereport.html')
#获取日志的绝对路径
log_path = os.path.join(project_path, 'result', 'test_log','future_log')
#获取配置文件的绝对路径
conf_path = os.path.join(project_path, 'conf', 'config.conf')
# print(cases_path)
