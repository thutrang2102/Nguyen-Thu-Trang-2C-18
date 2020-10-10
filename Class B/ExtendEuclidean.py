
def gcd(a, b, n):
    quotient = []
    while ( a != 0):
        r = n % a
        q = int(n / a)
        quotient.append(q)
        n = a
        a = r
    return quotient, n

def extendEuclidean(n, q):
    p = []
    p.append(0)
    print('step 1. p0 = 0')
    p.append(1)
    print('step 2. p1 = 1')
    for i in range(2, len(q)+1):
        print('step {}. p{}= '.format(i, i), end='')
        p[i] = p[i-2] -p[i-1]*q[i-2]
        # print(p[x-2], end = '')
        print('{} - {}.({}) mod {} = '.format(p[i-2], p[i-1], q[i-2], n), end='')
        while(p[i] < 0):
            p[i] = p[i] + n
        print(p[i])
        p.append(p[i])
    return p[len(q)]
def findx0 (r, a, b, n, gcd):
    x0 = r * b / gcd % (n/gcd)
    return int(x0)
def main():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    n = int(input('Enter n: '))
    x = gcd(a, b, n)
    r = extendEuclidean(n, x[0])
    print('x = ', end='')
    print(findx0(r, a, b, n, x[1]))


main()

