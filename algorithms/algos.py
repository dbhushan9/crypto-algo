def eucledian(a,b):
	if b == 0:
		return a
	return eucledian(b,a%b)