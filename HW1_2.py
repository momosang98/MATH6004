# -*- coding= utf-8 -*-
"""from sympy import *
x = Symbol("x")
print(diff(10.0 * x *(1-x)*(x-0.25)-0.25))
#求fx 的一阶导数
#10.0*x*(1 - x) - 10.0*x*(x - 0.25) + (10.0 - 10.0*x)*(x - 0.25)"""

# Q2: find by iteration a solution accurate to within the tolerance ǫ = 10−8 to the equation

#(a) Solve by the Newton method
def f(x):
    # f的方程
    return 10.0 * x *(1-x)*(x-0.25)-0.25


def f_first_order(x):
    # f的一阶导数

    return 10.0*x*(1 - x) - 10.0*x*(x - 0.25) + (10.0 - 10.0*x)*(x - 0.25)
    #此处需直接输入一阶导数否则会报错！？


def get_root(x0, max_iter=50, tol=1.0e-8):
    # 将初始值浮点化
    p0 = x0 * 1.0
    for i in range(max_iter):

        # f的一阶导数不能为0，最普遍的说法是不能非正定
        p = p0 - f(p0) / f_first_order(p0)
        c = f(p)

        # 如果小于精度值则退出迭代
        if abs(c) < tol:  # tol是判断迭代更新的阈值

            return u'(a):Through Newton method,after %s times iteration，we guess x = %s,f(x) = %s' % (i+1 , p, c)

        p0 = p

    print(u'已达到最大迭代次数， 但是仍然无法收敛')


if __name__ == '__main__':
    print(get_root(0))  # x0=0

#(b)
def f(x):
    # f的方程
    return 10.0 * x *(1-x)*(x-0.25)-0.25


def f_first_order(x):
    # f的一阶导数

    return 10.0*x*(1 - x) - 10.0*x*(x - 0.25) + (10.0 - 10.0*x)*(x - 0.25)
    #此处需直接输入一阶导数否则会报错！？


def get_root(x0, y,max_iter=50, tol=1.0e-8):
    # 将初始值浮点化
    p0 = x0 * 1.0
    for i in range(max_iter):

        # f的一阶导数不能为0，最普遍的说法是不能非正定
        p = p0 - y*f(p0) / f_first_order(p0)
        c = f(p)

        # 如果小于精度值则退出迭代
        if abs(c) < tol:  # tol是判断迭代更新的阈值

            return u'(b):Through Newton method,after %s times iteration，we guess x = %s, f(x) = %s' % (i+1 , p, c)

        p0 = p

    print(u'已达到最大迭代次数， 但是仍然无法收敛')


if __name__ == '__main__':
    print(get_root(0,0.5))  # x0=0

#(c):Accelerate the iteration above by Aitken’s technique:
def f(x):
    return 10.0 * x *(1-x)*(x-0.25)-0.25
def phi(f,x):
    return f+x

def roll(x):
    y1 = phi(f(x),x)
    y2 = phi(f(y1),y1)
    xx = (x*y2-y1**2)/(x+y2-2*y1)
    return xx

def main(x0,e):
    for i in range(500):
        c = f(roll(x0))
        x = roll(x0)
        if abs(c) < e:
            return u'(c):Through Aitken’s technique,after %s times iteration，we guess x = %s, f(x) = %s' % (i+1 , x, c)
        x0 = x

if __name__ == '__main__':

    print(main(0.0,1.0e-8))  # x0=0
