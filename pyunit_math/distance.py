#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/26 16:39
# @Author: Jtyoui@qq.com
from scipy.spatial import distance
from scipy.stats import entropy, wasserstein_distance
import numpy as np


# 文章：https://zhuanlan.zhihu.com/p/101277851

class Distance:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    def braycurtis(self, x=None, y=None, w=None):
        """
        Bray-Curtis 相异度（Bray-Curtis dissimilarity）是生态学中用来衡量不同样地物种组成差异的测度。
        由J. Roger Bray and John T. Curtis 提出。其计算基于样本中不同物种组成的数量特征（多度，盖度，重要值等）。
        计算公式为：

        x = [1, 2, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.braycurtis(x, y, w)

    def canberra(self, x=None, y=None, w=None):
        """
        Canberra distance是用来衡量两个向量空间的居间，1966年被提出，1977年被G. N. Lance和
        W. T. Williams重新提出。是Manhattan distance的加权版本，Canberra distance
        已被用作比较排名列表和计算机安全中的入侵检测的测量。

        x = [1, 2, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.canberra(x, y, w)

    def chebyshev(self, x=None, y=None, w=None):
        """
        切比雪夫距离（Chebyshev distance）是向量空间中的一种度量，二个点之间的距离定义是其各坐标数值差绝对值的最大值。
        以数学的观点来看，切比雪夫距离是由一致范数（uniform norm）（或称为上确界范数）所衍生的度量，
        也是超凸度量（injective metric space）的一种。计算公式为

        x = [1, 2, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.chebyshev(x, y, w)

    def manhattan(self, x=None, y=None, w=None):
        """
        曼哈顿距离（Manhattan Distance）是由十九世纪的赫尔曼·闵可夫斯基所创词汇，是种使用在几何度量空间的几何学用语，
        用以标明两个点在标准坐标系上的绝对轴距总和。曼哈顿距离的命名原因是从规划为方型建筑区块的城市（如曼哈顿）
        间，最短的行车路径而来（忽略曼哈顿的单向车道以及只存在于3、14大道的斜向车道）。
        任何往东三区块、往北六区块的的路径一定最少要走九区块，没有其他捷径。

        x = [1, 2, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.cityblock(x, y, w)

    def correlation(self, x=None, y=None, w=None, centered=True):
        """
        相关系数距离是1与相关系数的差

        x = [1, 2, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.correlation(x, y, w, centered)

    def cosine(self, x=None, y=None, w=None):
        """
        余弦相似性通过测量两个向量的夹角的余弦值来度量它们之间的相似性。0度角的余弦值是1，
        而其他任何角度的余弦值都不大于1；并且其最小值是-1。从而两个向量之间的角度的余弦值确定两个向量是否大致指向相同的方向。
        两个向量有相同的指向时，余弦相似度的值为1；两个向量夹角为90°时，余弦相似度的值为0；
        两个向量指向完全相反的方向时，余弦相似度的值为-1。这结果是与向量的长度无关的，仅仅与向量的指向方向相关。
        余弦相似度通常用于正空间，因此给出的值为0到1之间。

        x = [1, 2, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.cosine(x, y, w)

    def euclidean(self, x=None, y=None, w=None):
        """
        在数学中，欧几里得距离或欧几里得度量是欧几里得空间中两点间“普通”（即直线）距离。
        使用这个距离，欧氏空间成为度量空间。相关联的范数称为欧几里得范数。

        x = [1, 2, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.euclidean(x, y, w)

    def jensen_shannon(self, x=None, y=None):
        """
        JS散度度量了两个概率分布的相似度，基于KL散度的变体，解决了KL散度非对称的问题。
        一般地，JS散度是对称的，其取值是0到1之间。

        x = [1, 2, 0]
        y = [0, 1, 0]
        """

        x = x or self.x
        y = y or self.y

        def js(p, q):
            m = (p + q) / 2
            return 0.5 * entropy(p, m) + 0.5 * entropy(q, m)

        return js(np.asarray(x), np.asarray(y))

    def mahalanobis(self, v, x=None, y=None):
        """
        马氏距离是由印度统计学家马哈拉诺比斯提出的，
        表示数据的协方差距离。它是一种有效的计算两个未知样本集的相似度的方法。与欧氏距离不同的是，
        它考虑到各种特性之间的联系（例如：一条关于身高的信息会带来一条关于体重的信息，因为两者是有关联的），
        并且是尺度无关的(scale-invariant)，即独立于测量尺度。对于一个均值为μ，协方差矩阵为Σ的多变量向量，
        其马氏距离为sqrt( (x-μ)'Σ^(-1)(x-μ) )。

        v = [[1, 0.5, 0.5], [0.5, 1, 0.5], [0.5, 0.5, 1]]
        x = [2, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        return distance.mahalanobis(x, y, v)

    def minkowski(self, x=None, y=None, p=2, w=None):
        """
        闵氏距离不是一种距离，而是一组距离的定义
        当 p=1 时，就是曼哈顿距离
        当 p=2 时，就是欧氏距离
        当 p=无穷 时，就是切比雪夫距离

        x = [2, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.minkowski(x, y, p, w)

    def standardized_euclidean(self, v, x=None, y=None):
        """
        标准化欧氏距离是针对简单欧氏距离的缺点（量纲差异）而作的一种改进方案

        x = [2, 0, 0]
        y = [0, 1, 0]
        v = [0.1, 0.1, 0.1]
        """
        x = x or self.x
        y = y or self.y
        return distance.seuclidean(x, y, v)

    def squared_euclidean(self, x=None, y=None, w=None):
        """
        平方欧式距离是简单欧式距离每一项的平方

        x = [2, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.sqeuclidean(x, y, w)

    def wminkowski(self, x=None, y=None, p=2, w=np.ones(3)):
        """
        加权闵可夫斯基距离

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.wminkowski(x, y, p, w)

    def earth_mover(self, x, x_w, y, y_w):
        """
        Earth Mover distance，是基于运输问题的效率提出的一种直方图相似度量。
        它是归一化的从一个分布变为另一个分布的最小代价,
        可以用来测量两个分布(multi-dimensional distributions)之间的距离。
        EMD运算复杂度较高，平均而言至少是二次方级别。但是它作为距离函数，有一个非常好的特点是存在下界，
        两个分布的质心之间的距离，因此在粗略计算时，可以考虑用分布质心之间的距离代替EMD。

        x = [3.4, 3.9, 7.5, 7.8]
        x_w = [1.4, 0.9, 3.1, 7.2]
        y = [4.5, 1.4]
        y_w = [3.2, 3.5]
        """
        return wasserstein_distance(x, y, x_w, y_w)

    def dice(self, x=None, y=None, w=None):
        """
        Dice系数是一种集合相似度度量函数，通常用于计算两个样本的相似度

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.dice(x, y, w)

    def hamming(self, x=None, y=None, w=None):
        """
        两个等长字符串s1与s2之间的汉明距离定义为将其中一个变为另外一个所需要作的最小替换次数。

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.hamming(x, y, w)

    def jaccard(self, x=None, y=None, w=None):
        """
        两个集合A和B的交集元素在A，B的并集中所占的比例，称为两个集合的杰卡德相似系数。

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.jaccard(x, y, w)

    def kulsinski(self, x=None, y=None, w=None):
        """
        库尔辛斯基差异

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.kulsinski(x, y, w)

    def rogerstanimoto(self, x=None, y=None, w=None):
        """
        田本罗杰斯差异

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.rogerstanimoto(x, y, w)

    def russellrao(self, x=None, y=None, w=None):
        """
        拉塞尔差异

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.russellrao(x, y, w)

    def sokalmichener(self, x=None, y=None, w=None):
        """
        索卡尔米切纳差异

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.sokalmichener(x, y, w)

    def sokalsneath(self, x=None, y=None, w=None):
        """
        索卡尔雪差异

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.sokalsneath(x, y, w)

    def yule(self, x=None, y=None, w=None):
        """
        Yule差异

        x = [1, 0, 0]
        y = [0, 1, 0]
        """
        x = x or self.x
        y = y or self.y
        w = w or self.w
        return distance.yule(x, y, w)
