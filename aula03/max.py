def max3():
	max1 = float(input("Qual é ao primeiro número?"))
	max2 = float(input("Qual é o segundo número?"))
	m=max1
	if max1<max2:
		m=max2
	max3 = float(input("Qual é o terceiro número?"))
	if max2<max3:
		m=max3
	print("o maior número foi ",m)
max3()

