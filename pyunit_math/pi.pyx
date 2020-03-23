# cython: language_level=3
cimport cython
from libc.stdlib cimport malloc

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef cpi(int length):
    """计算无限长的Π"""
    cdef long lengths = (length * 14) // 3
    cdef long e = 0, pre = 10000
    cdef int *f = <int*> malloc(lengths * sizeof(int))
    cdef int *result = <int*> malloc((length // 3) * sizeof(int))
    cdef unsigned long flag = 0
    cdef long s = 0
    cdef long c = lengths
    cdef long b = 0
    cdef long surplus = length
    cdef long pi = 0
    cdef string
    cdef long move = 0

    for i in range(lengths):
        f[i] = pre // 5
    while c > 0:
        flag = 0
        b = c
        while b > 0:
            s = 2 * b - 1
            flag = flag * b + f[b] * pre
            f[b] = flag % s
            flag = flag // s
            b -= 1
        pi = e + flag // pre
        if surplus > 0:
            string = str(pi)
            len_p = len(string)
            if surplus < len_p:
                pi = int(string[:surplus])
            result[move] = pi
            move += 1
            surplus -= len_p
        if surplus <= 0:
            return [i for i in result[:move]]
        e = flag % pre
        c -= 14
    return [i for i in result[:move]]

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef ppi(int length):
    cdef long lengths = (length * 14) // 3
    cdef long e = 0, pre = 10000
    cdef int *f = <int*> malloc(lengths * sizeof(int))
    cdef unsigned long flag = 0
    cdef long s = 0
    cdef long c = lengths
    cdef long b = 0
    cdef long surplus = length
    cdef long pi = 0
    cdef string

    for i in range(lengths):
        f[i] = 2000
    while c > 0:
        flag = 0
        b = c
        while b > 0:
            s = 2 * b - 1
            flag = flag * b + f[b] * pre
            f[b] = flag % s
            flag = flag // s
            b -= 1
        pi = e + flag // pre
        if surplus > 0:
            string = str(pi)
            len_p = len(string)
            if surplus < len_p:
                pi = int(string[:surplus])
            print(pi)
            surplus -= len_p
        if surplus <= 0:
            return
        e = flag % pre
        c -= 14
