# Complete o programa!

# a)
def loadFile(fname, lst):
    file=open(fname)
    lines=file.readlines()
    for line in lines:
        tp = tuple()
        words=line.split()
        for word in words:
            try:
                word=float(word)
            except:
                word=word
            tp = tp + (word,)
        print(tp)
        lst.append(tp)
    print(lst)



    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):

# c) Crie a função printPauta aqui...
    ...

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    ...
    
    # mostrar a pauta
    ...


# Call main function
if __name__ == "__main__":
    main()


