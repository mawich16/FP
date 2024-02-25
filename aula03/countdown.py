N=int(input("introduza um número "))

def countdown(N):
    assert N>0
    
    for n in range(N):

        print(N-n)
        n+=1


countdown(N)