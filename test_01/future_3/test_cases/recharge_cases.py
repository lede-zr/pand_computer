#!/usr/bin/env python
# -*- coding: utf-8 -*-
from future_3.common.do_excel import DoExcel
from future_3.common.http_request import HttpRequest
from future_3.common.log_msg import MyLog
from future_3.common import project_path
from future_3.common.get_data import GetData
from future_3.common import get_data
from future_3.common.do_mysql import DoMysql
import unittest
import json
from ddt import ddt, data, unpack

excel = DoExcel(project_path.cases_path, 'recharge')
data_list = excel.read_excel('RECHARGE')
my_log = MyLog()
# COOKIES=None
@ddt
class Recharge(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*data_list)
    def test_recharge(self, case):
        global TestResult, expect, before_amount, expect_amount
        # global COOKIES
        method = case['Method']
        url = case['Url']
        # param = eval(case['Params'])
        param = eval(get_data.replace(case['Params']))
        # expect = eval(case['ExpectedResult'])#excel 里面的data是null，python没有null
        my_log.info('=====正在测试{}模块里面第{}条用例：{}'.format(case['Module'], case['CaseId'], case['Description']))
        # 充值前的余额
        if case['sql'] != None:
            case['sql'] = get_data.replace(case['sql'])
            sql = eval(case['sql'])['sql']
            before_amount = DoMysql().mysql(sql)[0]
        resp = HttpRequest().http_request(method, url, param,getattr(GetData,'COOKIE'))
        if resp.cookies:
            # COOKIES = resp.cookies
            setattr(GetData,'COOKIE',resp.cookies)
        try:
            # 充值后的余额
            if case['sql'] != None:
                sql = eval(case['sql'])['sql']
                after_amount = DoMysql().mysql(sql)[0]
                recharge_amount = int(param['amount'])
                expect_amount = before_amount + recharge_amount
                self.assertEqual(after_amount, expect_amount)
            if case['ExpectedResult'].find('expect_amount')>-1:
                case['ExpectedResult'] = case['ExpectedResult'].replace('expect_amount',str(expect_amount))
            # expect = json.loads(case['ExpectedResult'])
            # expect = eval(case['ExpectedResult'])
            self.assertEqual(eval(case['ExpectedResult']), resp.json())
            TestResult = 'pass'
        except Exception as e:
            # print('用例失败，原因是：{}'.format(e))
            my_log.error(e)
            TestResult = 'Faild'
            raise e
        finally:
            excel.write_excel(case['CaseId'] + 1, 9, resp.text)
            excel.write_excel(case['CaseId'] + 1, 10, TestResult)
            my_log.info('实际结果：{}'.format(resp.json()))