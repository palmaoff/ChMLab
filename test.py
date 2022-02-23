from read_and_print import read_mtr, print_mtr, read_f, print_f, accuracy_f
from functools import reduce
from main import alg

VALUE_RANGES = (10, 100, 1000)
MATRIX_SIZES = (10, 100, 1000)


def get_k(mtr):
	n = len(mtr) - 1
	if mtr[n][n] != 0:
		return n
	i = 0
	while mtr[0][i] == 0:
		i += 1
	return i


def main():

	result = open("results", "w")

	for matrix_size in MATRIX_SIZES:
		for value_range in VALUE_RANGES:
			file = f'gen_matrix_{matrix_size}_{value_range}'
			mtr = read_mtr(file)
			f = read_f(file)
			f2 = accuracy_f(mtr)

			print(f2)

			# alg
			if alg(mtr, f, f2, matrix_size - 1, get_k(mtr)):

				p = reduce(lambda a, b: a - 1 if (a - 1 > b - 1) else b - 1, f2)

				print()
				# print(f2)
				print(p)
				result.write(f'{p} with size {matrix_size} and value range {value_range}\n')


if __name__ == "__main__":
	main()