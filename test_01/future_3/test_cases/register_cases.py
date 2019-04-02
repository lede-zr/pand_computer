#!/usr/bin/env python
# -*- coding: utf-8 -*-

from future_3.common.do_excel import DoExcel
from future_3.common.http_request import HttpRequest
from future_3.common.log_msg import MyLog
from future_3.common import project_path
import unittest
import json
from ddt import ddt, data, unpack

excel = DoExcel(project_path.cases_path, 'register')
data_list = excel.read_excel('REGISTER')
my_log = MyLog()

@ddt
class Register(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*data_list)
    def test_register(self, case):
        global TestResult
        # print(case)
        method = case['Method']
        url = case['Url']
        param = eval(case['Params'])
        expect = json.loads(case['ExpectedResult'])
        # expect = eval(case['ExpectedResult'])#excel 里面的data是null，python没有null
        my_log.info('=====正在测试{}模块里面第{}条用例：{}'.format(case['Module'], case['CaseId'], case['Description']))
        resp = HttpRequest().http_request(method, url, param)
        try:
            self.assertEqual(expect, resp.json())
            TestResult = 'pass'
            # excel.write_excel(case['CaseId']+1,9,'Pass')
        except Exception as e:
            # print('用例失败，原因是：{}'.format(e))
            my_log.error(e)
            TestResult = 'Faild'
            # excel.write_excel(case['CaseId']+1,9,'Faild')
            raise e
        finally:
            excel.write_excel(case['CaseId'] + 1, 9, resp.text)
            excel.write_excel(case['CaseId'] + 1, 10, TestResult)
            my_log.info('实际结果：{}'.format(resp.json()))
