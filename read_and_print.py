def read_f(str):
	mtr = []
	f = open(str)
	line = ' '

	while (line != '\n'):
		line = f.readline()
	line = f.readline()

	while (line):
		mtr.append(int(line))
		line = f.readline()

	return mtr


def read_mtr(str):
	mtr = []
	f = open(str)
	line_str = f.readline()

	while (line_str != '\n'):
		line = list(map(int, line_str.split()))
		mtr.append(line)
		line_str = f.readline()

	return mtr


def print_f(f, str):
	print('\n' + str)
	for i in f:
		print("%.1f" % i, end="\t")


def print_mtr(mtr,str):
	print(str)
	for line in mtr:
		for curr in line:
			print("%.1f" % curr, end="\t")
		print()
