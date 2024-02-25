def tax():
	r = float(input("qual é o valor de r"))
	if r<= 1000:
		r = 0.1 * r
	elif 1000<r<=2000:
		r = 0.2 * r -100
	else:
		r= 0.3 * r - 300
	print(r)
tax()