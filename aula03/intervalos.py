
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=int(input("d= "))

def intersects(a,b,c,d):
	assert a<=b
	assert c<=d
	if d<a:
		print("false")
	elif b<c:
		print("false")
	else:
		print("true")

intersects(a,b,c,d)