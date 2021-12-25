def print_mtr(mtr,str):
	print(str)
	for line in mtr:
		for curr in line:
			print("%.1f" % curr, end="\t")
		print()
