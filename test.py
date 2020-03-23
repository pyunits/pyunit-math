#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/26 17:38
# @Author: Jtyoui@qq.com
from pyunit_math import pi, binary_system


def pi_test():
    s = ''
    for i in pi(1302):
        print(i, end='')
        s += str(i)
    print('\n', len(s))


def bs_test():
    print(binary_system('11011001000011010', 2, 36))  # 将2进制转为36进制
    print(binary_system('2dqy', 36, 2))  # 将36进制转为2进制


if __name__ == '__main__':
    # pi_test()
    bs_test()
