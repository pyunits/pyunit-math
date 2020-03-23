#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/26 17:38
# @Author: Jtyoui@qq.com
from pyunit_math import pi


def pi_test():
    s = ''
    for i in pi(1302):
        print(i, end='')
        s += str(i)
    print('\n', len(s))


if __name__ == '__main__':
    pi_test()
