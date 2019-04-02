#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

class ReadConfig:
    '''读取配置文件信息'''

    def __init__(self, file_name):
        self.cf = ConfigParser()
        self.cf.read(file_name, encoding='utf-8')

    def get_int(self, section, option):
        value = self.cf.getint(section, option)
        return value

    def get_float(self, section, option):
        value = self.cf.getfloat(section, option)
        return value

    def get_bool(self, section, option):
        value = self.cf.getboolean(section, option)
        return value

    def get_str(self, section, option):
        value = self.cf.get(section, option)
        return value

    def get_data(self, section, option):
        value = self.cf.get(section, option)
        return eval(value)


if __name__ == '__main__':
    t = ReadConfig('config.conf')
    print(t.get_data('Test', 'dict'))
