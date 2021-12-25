def read_f(str):
	mtr = []
	f = open(str)
	line = ' '

	while (line != '\n'):
		line = f.readline()
	line = f.readline()

	while (line != ''):
		mtr.append(int(line))
		line = f.readline()

	return mtr
