# -*- coding: utf-8 -*-
#@time : 2019/3/30 15:11
#@Author : zr
#@Email : 429082323@qq.com
#@File : loan_cases.py
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

excel = DoExcel(project_path.cases_path, 'loan')
data_list = excel.read_excel('LOAN')
my_log = MyLog()
# COOKIES=None
@ddt
class Loan(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*data_list)
    def test_loan(self, case):
        global TestResult
        # global COOKIES
        method = case['Method']
        url = case['Url']
        # param = eval(case['Params'])
        expect = json.loads(case['ExpectedResult'])

        #替换loan_id,mobilephone,pwd
        # if case['Params'].find('loanid')!=-1:
        #     param = eval(case['Params'].replace('loanid',str(getattr(GetData,'LOAN_ID'))))
        # else:
        #     param = eval(case['Params'])
        param = eval(get_data.replace(case['Params']))


        # expect = eval(case['ExpectedResult'])#excel 里面的data是null，python没有null
        my_log.info('=====正在测试{}模块里面第{}条用例：{}'.format(case['Module'], case['CaseId'], case['Description']))
        resp = HttpRequest().http_request(method, url, param,getattr(GetData,'COOKIE'))
        if case['sql']!=None:
            case['sql'] = get_data.replace(case['sql'])
            loan_id = DoMysql().mysql(eval(case['sql'])['sql'])
            setattr(GetData,'loanid',str(loan_id[0]))
        if resp.cookies:
            # COOKIES = resp.cookies
            setattr(GetData,'COOKIE',resp.cookies)
        try:
            self.assertEqual(expect, resp.json())
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