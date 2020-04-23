#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/17 14:43
# @Author: Jtyoui@qq.com
import math
import random
import time


def tetrahedron_volume(r1, r2, r3, r4, r5, r6):
    """知道四面体的边求体积，r1-r6都是边"""
    R1, R2, R3, R4, R5, R6 = r1 ** 2, r2 ** 2, r3 ** 2, r4 ** 2, r5 ** 2, r6 ** 2
    one = R1 * R2 * R4 + R1 * R3 * R6 + R2 * R3 * R5 + R4 * R5 * R6
    two = R1 * R2 * R5 + R1 * R2 * R6 + R1 * R3 * R4 + R1 * R3 * R5 + R1 * R4 * R5 + R1 * R5 * R6 + R2 * R3 * R4 + R2 * R3 * R6 + R2 * R4 * R6 + R2 * R5 * R6 + R3 * R4 * R5 + R3 * R4 * R6
    three = R1 * R1 * R5 + R1 * R5 * R5 + R2 * R2 * R6 + R2 * R6 * R6 + R3 * R3 * R4 + R3 * R4 * R4
    s = two - one - three
    v = math.sqrt(s / 144)
    return v


def tetrahedron_volume2(a, b, c, m, n, l):
    """知道四面体的边求体积，a, b, c, m, n, l都是边"""
    v = math.sqrt((4.0 * a * a * b * b * c * c - a * a * (b * b + c * c - m * m) * (b * b + c * c - m * m) - b * b * (
            c * c + a * a - n * n) * (c * c + a * a - n * n) - c * c * (a * a + b * b - l * l) * (
                           a * a + b * b - l * l) + (a * a + b * b - l * l) * (b * b + c * c - m * m) * (
                           c * c + a * a - n * n))) / 12.0
    return v


def helen_formula(a, b, c):
    """海伦公式，知道三边求面积

    a、b、c是三角形的三条边
    """
    if all([a > 0, b > 0, c > 0]):
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s
    raise TypeError('类型错误,三角形三边必须是大于0的数字类型')


def __successive_division(n, x):  # 辗转相除法
    while n:
        yield n % x  # 将余数返回
        n //= x  # 剩下余数


def binary_system(x: [int, str], base_x: int, base_y: int) -> str:
    """转化进制

    >>> print(binary_system(2542, 7, 12))

    :param x: 字符串非负整数
    :param base_x: 字符串的进制
    :param base_y: 转化的进制
    :return: 被转化的进制
    """
    if base_y <= 1 or base_x <= 1:  # 进制不可能小于1
        raise ValueError('进制不可能小于1')
    if not isinstance(x, (int, str)):
        raise ValueError('x值应该是int类型或者字符串类型')
    if isinstance(x, int):
        if x < 1:
            raise ValueError('x的值不可能小于1')
        x = str(x)
    y = int(x, base_x)  # 将其他进制先转为十进制
    # 在将十进制转为其他进制,并且将大于10的数字用ASCII值来表示,第一个ASCII是97小写的a
    m = map(lambda b: chr(b + 87) if b >= 10 else str(b), __successive_division(y, base_y))
    bs = ''.join(m)[::-1]  # 返回字符串并且反转
    if int(bs, base_y) == y:  # 检验进制是否正确
        return bs
    raise ValueError('验证进制错误!')  # 如果检验失败,返回错误


def uuid6():
    """生成64位的超大UUID，每一位有62种状态

    前12位是时间序列,只有在同一飞秒(1飞秒等于一亿分之一秒)的时间中生成 62**52 种状态才会相同。这个数字比宇宙中的所有原子数量还要大。

    :return: 生成的uuid的大小写敏感的
    """
    status = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
              'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z')
    t = time.time() * 1_0000_0000
    u = binary_system(int(t), 10, 36)
    while True:
        u += random.choice(status)
        if len(u) >= 64:
            break
    return u
