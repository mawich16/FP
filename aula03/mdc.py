a=int(input("introduza o numero maior "))
b=int(input("introduza o outro numero "))

def mdc(a,b):
    assert a>b
    assert a>0
    r=a%b
    if r==0:
        mdc=b
    else:
        while r!=0:
            r=b%r
            