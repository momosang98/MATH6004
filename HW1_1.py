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
    return u' can not generate a convergent sequence '



if __name__ == '__main__':
    print('With initial guess x0=0.1',',',main(0.1,100))
    print('With initial guess x0=0.9',',',main(0.9, 100))
    print('With initial guess x0=0.3',',',main(0.3, 100))
    print('With initial guess x0=-1.01',',',main(-1.01, 100))

#(b) check the convergence of the iteration above accelerated by Aitken’s technique
def f(x):
    return x**2.0 + x -2.0
def phi(f,x):
    return f+x

def y(f,x):
    return phi(f,x)

def z(f,y):
    return phi(f,y)

def roll(x):
    f1=f(x)
    y1=y(f1,x)
    f2=f(y1)
    z1=z(f2,y1)
    xx=(x*z1-y1**2)/(x+z1-2*y1)
    return xx



def main(x,e):
    ans = []
    ans.append(roll(x))
    ans.append(roll(ans[0]))
    for i in range(500):
        if abs(ans[-1] - ans[-2]) < e:
            return  i+1,ans[-1]
        ans.append(roll(ans[-1]))

if __name__ == '__main__':
    print('Through Aitken’s technique,after %s times iteration，we guess x = %s' % (main(0.01,1e-8)))
