#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/26 17:38
# @Author: Jtyoui@qq.com
from pyunit_math import ppi, cpi, binary_system, Distance


def pi_test():
    ppi(100_0000)
    print(cpi(100_0000))


def bs_test():
    print(binary_system('11011001000011010', 2, 36))  # 将2进制转为36进制
    print(binary_system('2dqy', 36, 2))  # 将36进制转为2进制


def distance_test():
    distance = Distance(x=[1, 2, 3], y=[2, 3, 4], w=None)
    print(distance.cosine())
    print(distance.hamming())


if __name__ == '__main__':
    import time

    start = time.time()
    pi_test()
    print(time.time() - start)
    # bs_test()
    # distance_test()
