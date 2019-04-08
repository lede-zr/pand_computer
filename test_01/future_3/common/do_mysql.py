# -*- coding: utf-8 -*-
#@time : 2019/3/21 22:22
#@Author : zr
#@Email : 429082323@qq.com
#@File : do_mysql.py.py

from mysql import connector
from future_3.common.configrue_msg import ReadConfig
from future_3.common import project_path
class DoMysql:
    def mysql(self,query,falg=1):
        '''
        :param query:sql查询语句
        :param falg:标志，1获取一条数据；2获取多条语句
        :return:
        '''
        db_config = ReadConfig(project_path.conf_path).get_data('DB','db_config')
        cnn = connector.connect(**db_config)#建立连接
        cursor = cnn.cursor()#获取游标，获取操作数据库的权限
        cursor.execute(query)#操作数据表
        if falg==1:
            res = cursor.fetchone()#返回元组，一条数据
        else:
            res = cursor.fetchall()#返回列表嵌套元组，可返回多条数据
        return res
if __name__ == '__main__':
    query = 'select max(Id) from loan where MemberID = 1116206'
    t = DoMysql()
    print(t.mysql(query))