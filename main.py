from read_and_print import read_mtr, print_mtr, read_f, print_f, accuracy_f
from functools import reduce
import sys


def main():
	file = sys.argv[1]
	# file = "matrix2.txt"
	mtr = read_mtr(file)
	f = read_f(file)
	f2 = accuracy_f(mtr)
	print_mtr(mtr, "\nmatrix:")
	print(f)
	print(f2)

	n = len(mtr)
	m = len(mtr[0])

	# check matrix
	for line in mtr:
		if m != len(line):
			print("Invalid matrix!")
			return

	# alg
	alg(mtr, f, f2, n - 1, int(sys.argv[2]) - 1)
	# alg(mtr, f, f2, n - 1, 4)

	print_f(f, 'f:')
	print_f(f2, 'f:')

	p = reduce(lambda a, b: a - 1 if (a - 1 > b - 1) else b - 1, f2)

	print()
	print(p)


def alg(mtr, f, f2, n, k):
	for i in range(0, k):
		j = n - i

		r = 1 / mtr[i][j]
		mtr[i][j] = 1
		mtr[i][j - 1] *= r
		if j != k and j != k + 1:
			mtr[i][k] *= r
		f[i] *= r
		f2[i] *= r

		r = mtr[k][j]
		mtr[k][j] = 0
		mtr[k][j - 1] -= r * mtr[i][j - 1]
		if j != k and j != k + 1:
			mtr[k][k] -= r * mtr[i][k]
		f[k] -= r * f[i]
		f2[k] -= r * f2[i]

		if i + 1 != k:
			r = mtr[i + 1][j]
			mtr[i + 1][j] = 0
			mtr[i + 1][j - 1] -= r * mtr[i][j - 1]
			if k != j - 1 and k != j:
				mtr[i + 1][k] -= r * mtr[i][k]
			f[i + 1] -= r * f[i]
			f2[i + 1] -= r * f2[i]
	
	for i in range(n, k, -1):
		j = n - i

		r = 1 / mtr[i][j]
		mtr[i][j] = 1
		mtr[i][j + 1] *= r
		if j != k and j + 1 != k:
			mtr[i][k] *= r
		f[i] *= r
		f2[i] *= r

		r = mtr[k][j]
		mtr[k][j] = 0
		mtr[k][j + 1] -= r * mtr[i][j + 1]
		if k != j and k != j + 1:
			mtr[k][k] -= r * mtr[i][k]
		f[k] -= r * f[i]
		f2[k] -= r * f2[i]

		if i - 1 != k:
			r = mtr[i - 1][j]
			mtr[i - 1][j] = 0
			mtr[i - 1][j + 1] -= r * mtr[i][j + 1]
			if k != j and k != j + 1:
				mtr[i - 1][k] -= r * mtr[i][k]
			f[i - 1] -= r * f[i]
			f2[i - 1] -= r * f2[i]

	f[k] /= mtr[k][n - k]
	f2[k] /= mtr[k][n - k]
	mtr[k][n - k] = 1

	r = mtr[k - 1][n - k]
	mtr[k - 1][n - k] = 0
	f[k - 1] -= r * f[k]
	f2[k - 1] -= r * f2[k]

	r = mtr[k + 1][n - k]
	mtr[k + 1][n - k] = 0
	f[k + 1] -= r * f[k]
	f2[k + 1] -= r * f2[k]

	if k < n - k:
		for i in range(k, n - k):
			j = n - i
			r = mtr[i + 1][j]
			mtr[i + 1][j] = 0
			f[i + 1] -= r * f[i]
			f2[i + 1] -= r * f2[i]
	elif k > n - k: # to do
		for i in range(n - k, k, -1):
			j = n - i
			r = mtr[i - 1][j]
			mtr[i - 1][j] = 0
			f[i - 1] -= r * f[i]
			f2[i - 1] -= r * f2[i]

	for i in range(0, n + 1):
		if i != n - k:
			r = mtr[i][k]
			mtr[i][k] = 0
			f[i] -= r * f[n - k]
			f2[i] -= r * f2[n - k]
	
	for i in range(n - k, n):
		j = n - i
		r = mtr[i + 1][j]
		mtr[i + 1][j] = 0
		f[i + 1] -= r * f[i]
		f2[i + 1] -= r * f2[i]

	for i in range(k, 0, -1):
		j = n - i
		r = mtr[i - 1][j]
		mtr[i - 1][j] = 0
		f[i - 1] -= r * f[i]
		f2[i - 1] -= r * f2[i]

if __name__ == "__main__":
	main()

