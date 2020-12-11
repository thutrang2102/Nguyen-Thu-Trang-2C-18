
def binary(x):
    bin = []
    while (x>=1):
        bin.append(x%2)
        x = x // 2
        binary(x)
    str = [i for i in bin]
    bin = str[::-1]
    return bin
def powMod(a, b, m):
	x = []
	while (b != 0):
		x.append(binary(b))
		b = b >> 1
	po = [a % m]
	for i in range(1, len(x)):
		p = (po[i-1]*po[i-1]) % m
		po.append(p)
	r = 1
	for i in range(len(x)):
		if(x[i] != 0):
			r *= po[i]
			r %= m
	return r
def main():
    a = int(input('a ='))
    b = int(input('b ='))
    m = int(input('m ='))
    print('x =', powMod(a, b, m))


main()
