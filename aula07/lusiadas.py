lusiadas = open('pg3333.txt','r',encoding="utf8")
d = dict()
l = lusiadas.read()
l = l.strip()

def standard(word):
    word = word.upper()
    word = word.replace('À', 'A').replace('Á', 'A').replace('Ã', 'A').replace('Â', 'A').replace('É', 'E').replace('È', 'E').replace('Ê', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Õ', 'O').replace('Ô', 'O').replace('Ò', 'O').replace('Ú', 'U').replace('Ü', 'U').replace('Ç', 'C')
    word = word.lower()
    return word

for i in l:
    if i.isalpha()==True:
        i1 = standard(i)
        if i1 not in d:
            d[i1]=1
        else:
            d[i1]+=1

d_o = dict(sorted(d.items()))

for i1 in d_o:
    print(i1,d_o[i1])


lusiadas.close()

