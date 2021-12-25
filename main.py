from print_mtr import print_mtr
from read_mtr import read_mtr
from read_f import read_f

def main():
	mtr = read_mtr("matrix.txt")
	f = read_f("matrix.txt")
	print_mtr(mtr, "\nmatrix:")
	print(f)

	n = len(mtr)
	m = len(mtr[0])

	# check mtr
	for line in mtr:
		if m != len(line):
			print("Invalid matrix!")
			return

	# alg
	alg(mtr, f, n - 1, 4)

	print_mtr(mtr, "\nmatrix:")
	print(f)

def alg(mtr, f, n, k):
	for i in range(0, k):
		j = n - i
	
		r = 1 / mtr[i][j]
		mtr[i][j] = 1
		mtr[i][j - 1] *= r
		if j != k:
			mtr[i][k] *= r
		f[i] *= r

		r = mtr[k][j]
		mtr[k][j] = 0
		mtr[k][j - 1] -= r * mtr[i][j - 1]
		if j != k:
			mtr[k][k] -= r * mtr[i][k]
		f[k] -= r * f[i]

		if i + 1 != k:
			r = mtr[i + 1][j]
			mtr[i + 1][j] = 0
			mtr[i + 1][j - 1] -= r * mtr[i][j - 1]
			mtr[i + 1][k] -= r * mtr[i][k]
			f[i + 1] -= r * f[i]
	
	for i in range(n, k, -1):
		j = n - i
		print(i, j)

		r = 1 / mtr[i][j]
		mtr[i][j] = 1
		mtr[i][j + 1] *= r
		if j != k:
			mtr[i][k] *= r
		f[i] *= r

		r = mtr[k][j]
		mtr[k][j] = 0
		mtr[k][j + 1] -= r * mtr[i][j + 1]
		if j != k:
			mtr[k][k] -= r * mtr[i][k]
		f[k] -= r * f[i]

		if i - 1 != k:
			r = mtr[i - 1][j]
			mtr[i - 1][j] = 0
			mtr[i - 1][j + 1] -= r * mtr[i][j + 1]
			mtr[i - 1][k] -= r * mtr[i][k]
			f[i - 1] -= r * f[i]
			
	f[k] /= mtr[k][n - k]
	mtr[k][n - k] = 1
 
	r = mtr[k - 1][n - k]
	mtr[k - 1][n - k] = 0
	f[k - 1] -= r * f[k]

	r = mtr[k + 1][n - k]
	mtr[k + 1][n - k] = 0
	f[k + 1] -= r * f[k]

	for i in range(0, n + 1):
		if i != n - k:
			r = mtr[i][k]
			mtr[i][k] = 0
			f[i] -= r * f[n - k]

	for i in range(n - k + 1, n + 1):
		j = n - i + 1
		r = mtr[i][j]
		mtr[i][j] = 0
		f[i] -= r * f[i - 1]

	for i in range(n - k - 1, -1, -1):
		j = n - i - 1
		r = mtr[i][j]
		mtr[i][j] = 0
		f[i] -= r * f[i + 1]

if __name__ == "__main__":
	main()
