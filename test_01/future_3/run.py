# -*- coding: utf-8 -*-
# @time : 2019/3/14 21:30
# @Author : zr
# @Email : 429082323@qq.com
# @File : run.py.py

import unittest
import HTMLTestRunnerNew
from future_3.test_cases import register_cases,recharge_cases,loan_cases,invest_cases
from future_3.common import project_path

suite = unittest.TestSuite()  # 新建测试集
loader = unittest.TestLoader()  # 用例收集器

suite.addTest(loader.loadTestsFromModule(register_cases))  # 添加用例
suite.addTest(loader.loadTestsFromModule(recharge_cases))
suite.addTest(loader.loadTestsFromModule(loan_cases))
suite.addTest(loader.loadTestsFromModule(invest_cases))
# suite.addTest(loader.loadTestsFromModule(future_cases))
with open(project_path.result_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='FutureIoan测试报告', description='login',
                                              tester='zr')
    runner.run(suite)
