nomes = open('names.txt','r')
d = {}

for line in nomes:
    n=line.strip().split()
    #print(n)
    if n[-1] not in d:
        d[n[-1]] = n[0]
    else:
        if n[0] not in d[n[-1]]:
            d[n[-1]] += ' ' + n[0] 
    

print(d)



nomes.close()