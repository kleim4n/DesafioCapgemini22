#Autor: Gabriel Kleiman
from itertools import combinations
def Questao3(text):
    text = str(text)
    anagramasSort = []
    for i in range(len(text) - 1):
        pTeste = [list(j) for j in combinations(text, i + 1)]
        pTesteSort = [j.copy() for j in pTeste]
        [i.sort() for i in pTesteSort]
        pTesteSort = [''.join(j) for j in pTesteSort]
        countTeste = [pTesteSort.count(j) for j in pTesteSort]
        for j in range(len(pTesteSort)):
            if pTesteSort.count(pTesteSort[j]) > 1 and pTesteSort[j] not in anagramasSort:
                anagramasSort.append(pTesteSort[j])
    return len(anagramasSort)
print(Questao3(input('Palavra = ')))
