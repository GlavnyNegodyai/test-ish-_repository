from numpy import *
m = array([[1, 9, 8],
           [3, 5, 7],
           [2, 7, 4]])

def f(n):
    if len(m[0]) == 3:
        opr1 = m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[1][0] * m[0][2] * m[2][1]
        opr2 = m[2][0] * m[1][1] * m[0][2] + m[1][0] * m[0][1] * m[2][2] + m[0][0] * m[1][2] * m[2][1]
        opr = opr1 - opr2
    else:
        z = m[0]
        q = delete(m, [0], 1)
        for i in range(len(m[0])):
            w = delete(q, [i], 0)

    return opr
