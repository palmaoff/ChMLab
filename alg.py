import sys
from read_and_print import read_mtr, print_mtr, read_f, print_f, accuracy_f


def main():
	file = sys.argv[1]
	# file = 'tests\gen_matrix_10_100'

	mtr = read_mtr(file)
	f = read_f(file)
	f2 = accuracy_f(mtr)

	# print_mtr(mtr, "\nmatrix:")
	# print_f(f2, 'f2:')

	n = len(mtr)

	# alg
	alg(mtr, f, f2, n, int(sys.argv[2]) - 1)
	# alg(mtr, f, f2, n, 3 - 1)

	print(f'f2: {f2}')


def alg(mtr, f, f2, n, k):
	# data
	a = []
	b = []
	c = []
	p = []
	q = []

	for i in range(0, n):
		j = n - i - 1

		b.append(mtr[i][j])

		if i == 0:
			c.append(0)
		else:
			c.append(mtr[i][j + 1])
		
		if i == n - 1:
			a.append(0)
		else:
			a.append(mtr[i][j - 1])

		p.append(mtr[i][k])
	
	for i in range(0, n):
		q.append(mtr[k][i])

	# alg
	for i in range(0, k):
		j = n - i - 1

		r = 1 / b[i]
		b[i] = 1
		if j == k:
			r = 1 / p[i]
			p[i] = 1
		else:
			p[i] *= r
		a[i] *= r
		f[i] *= r
		f2[i] *= r

		r = q[j]
		q[j] = 0
		if j != k:
			q[k] -= r * p[i]
			p[k] -= r * p[i]
		if j - 1 != k:
			q[j - 1] -= r * a[i]
		f[k] -= r * f[i]
		f2[k] -= r * f2[i]

		if i + 1 != k:
			r = c[i + 1]
			c[i + 1] = 0
			p[i + 1] -= r * p[i]
			b[i + 1] -= r * a[i]
			f[i + 1] -= r * f[i]
			f2[i + 1] -= r * f2[i]
		
	for i in range(n - 1, k, -1):
		j = n - i - 1

		r = 1 / b[i]
		b[i] = 1
		if j == k:
			r = 1 / p[i]
			p[i] = 1
		else:
			p[i] *= r
		c[i] *= r
		f[i] *= r
		f2[i] *= r

		r = q[j]
		q[j] = 0
		if j != k:
			q[k] -= r * p[i]
			p[k] -= r * p[i]
		if j + 1 != k:
			q[j + 1] -= r * c[i]
		f[k] -= r * f[i]
		f2[k] -= r * f2[i]

		if i - 1 != k:
			r = a[i - 1]
			a[i - 1] = 0
			b[i - 1] -= r * c[i]
			p[i - 1] -= r * p[i]
			f[i - 1] -= r * f[i]
			f2[i - 1] -= r * f2[i]

	r = 1 / q[n - k - 1]
	q[n - k - 1] = 1
	if n - k - 1 != k:
		q[k] *= r 
		p[k] *= r
	f[k] *= r
	f2[k] *= r

	if k - 1 > 0:
		r = a[k - 1]
		a[k - 1] = 0
		p[k - 1] -= r * q[k]
		f[k - 1] -= r * f[k]
		f2[k - 1] -= r * f2[k]

	if k + 1 != n:
		r = c[k + 1]
		c[k + 1] = 0
		p[k + 1] -= r * q[k]
		f[k + 1] -= r * f[k]
		f2[k + 1] -= r * f2[k]

	for i in range(k + 1, n - 1):
		j = n - i - 1

		r = c[i + 1]
		c[i + 1] = 0
		p[i + 1] -= r * p[i]
		f[i + 1] -= r * f[i]
		f2[i + 1] -= r * f2[i]

	for i in range(k - 1, 0, -1):
		j = n - i - 1

		r = a[i - 1]
		a[i - 1] = 0
		p[i - 1] -= r * p[i]
		f[i - 1] -= r * f[i]
		f2[i - 1] -= r * f2[i]

	for i in range(0, n):
		if i != n - k - 1 and i != k:
			r = p[i]
			p[i] = 0
			f[i] -= r * f[n - k - 1]
			f2[i] -= r * f2[n - k - 1]

	if k != n - k - 1:	
		r = q[k]
		q[k] = 0
		f[k] -= r * f[n - k - 1]
		f2[k] -= r * f2[n - k - 1]

	# test print
	# print()
	# print(f'f2: {f2}')
	# print(f'a: {a}')
	# print(f'b: {b}')
	# print(f'c: {c}')
	# print(f'p: {p}')
	# print(f'q: {q}')


if __name__ == "__main__":
	main()
