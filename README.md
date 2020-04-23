# **PyUnit-Math** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 统计学和数学模块
[![](https://img.shields.io/badge/Python-3.7-green.svg)](https://pypi.org/project/pyunit-math/)
[![](https://img.shields.io/badge/统计学-Statistics-black.svg)]()

## 安装
    pip install pyunit-math
    
## 使用
```python
from pyunit_math import ppi, cpi, binary_system, Distance, uuid6


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


def uuid_test():
    print(uuid6())


if __name__ == '__main__':
    # import time
    #
    # start = time.time()
    # pi_test()
    # print(time.time() - start)
    # bs_test()
    # distance_test()
    uuid_test()
```

***
[1]: https://blog.jtyoui.com