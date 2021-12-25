def read_mtr(str):
	mtr = []
	f = open(str)
	line_str = f.readline()

	while (line_str != '\n'):
		line = list(map(int, line_str.split()))
		mtr.append(line)
		line_str = f.readline()

	return mtr
