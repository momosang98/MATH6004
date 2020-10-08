#Q1
# (a)check whether the iteration generates a convergent sequence with different initial guess x0 = 1, −2, 0, −1.

def f(x):
    return x**2.0 + x -2.0
def main(p0,n):

    for i in range(n):
        p = p0 + f(p0)
        if abs(p-p0) < 1.0e-8:
            return u'after %s times iteration，we get x = %s' % (i+1 , p)
        p0 = p
        print('x = ',p0,',','fx = ',f(p0))
    return u' can not generate a convergent sequence '

if __name__ == '__main__':
    x0 = float(input('Please input initial guess x0 except 1, −2, 0, −1'))
    print('With initial guess x0 = ',x0,'\n',main(x0,10))


#(b) check the convergence of the iteration above accelerated by Aitken’s technique
def f(x):
    return x**2.0 + x -2.0
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
            return u'Through Aitken’s technique,after %s times iteration，we guess x = %s, f(x) = %s' % (i+1 , x, c)
        x0 = x
    print('can not generate a convergent sequence' )


if __name__ == '__main__':
    x0 = float(input('Please input initial guess x0'))
    print('With initial guess x0= ',x0,'\n',main(x0,1.0e-8))
