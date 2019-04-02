#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from future_3.common.configrue_msg import ReadConfig
from future_3.common import project_path


class MyLog:
    def __init__(self):
        res = ReadConfig(project_path.conf_path)
        section = 'LOG'
        self.logger = res.get_str(section, 'logger_name')
        # self.file_name = res.get_str(section, 'file_name')#配置文件
        self.file_name = project_path.log_path
        self.logger_level = res.get_str(section, 'logger_level')
        self.formatter = res.get_str(section, 'formatter')

    def my_log(self, level, msg):
        my_logger = logging.getLogger(self.logger)
        my_logger.setLevel(self.logger_level)
        formatter = logging.Formatter(self.formatter)
        fh = logging.FileHandler(self.file_name, encoding='utf-8')
        fh.setLevel(self.logger_level)
        fh.setFormatter(formatter)
        ch = logging.StreamHandler()  # 输出渠道为控制台
        ch.setLevel(self.logger_level)
        ch.setFormatter(formatter)
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if level.lower() == 'debug':
            my_logger.debug(msg)
        elif level.lower() == 'info':
            my_logger.info(msg)
        elif level.lower() == 'warning':
            my_logger.warning(msg)
        elif level.lower() == 'error':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)


    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)


if __name__ == '__main__':
    myLog = MyLog()
    myLog.error('this is error')
