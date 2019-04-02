# -*- coding: utf-8 -*-
# @time : 2019/3/31 17:19
# @Author : zr
# @Email : 429082323@qq.com
# @File : invest_cases.py
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

excel = DoExcel(project_path.cases_path, 'invest')
data_list = excel.read_excel('INVEST')
my_log = MyLog()


@ddt
class Invest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*data_list)
    def test_invest(self, case):
        global TestResult, before_amount
        method = case['Method']
        url = case['Url']
        # param = eval(case['Params'])
        param = eval(get_data.replace(case['Params']))
        # expect = json.loads(case["ExpectedResult"])
        # expect = eval(case["ExpectedResult"])
        my_log.info('=====正在测试{}模块里面第{}条用例：{}'.format(case['Module'], case['CaseId'], case['Description']))
        # 投资前的余额
        if case['sql'] != None:
            case['sql'] = get_data.replace(case['sql'])
            sql = eval(case['sql'])['sql']
            before_amount = DoMysql().mysql(sql)[0]

        resp = HttpRequest().http_request(method, url, param, getattr(GetData, 'COOKIE'))
        if resp.cookies:
            setattr(GetData, 'COOKIE', resp.cookies)

        try:
            self.assertEqual(eval(case["ExpectedResult"]), resp.json())
            # 投资后的余额
            if case['sql'] != None:
                sql = eval(case['sql'])['sql']
                after_amount = DoMysql().mysql(sql)[0]
                invest_amount = param['amount']
                expect_amount = before_amount - after_amount
                self.assertEqual(invest_amount, expect_amount)
            TestResult = 'pass'
        except Exception as e:
            my_log.error(e)
            TestResult = 'Faild'
            my_log.info('实际结果：{}'.format(resp.json()))
            raise e
        finally:
            excel.write_excel(case['CaseId'] + 1, 9, resp.text)
            excel.write_excel(case['CaseId'] + 1, 10, TestResult)
