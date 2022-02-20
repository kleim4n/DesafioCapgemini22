#Autor: Gabriel Kleiman
def Questao1(n):
    if type(n) != int:
        try:
            n = int(n)
        except:
            return False
    text = ''
    for i in range(n):
        line = ''
        for j in range(n -1 -i):
            line = ' ' + line
        while len(line) < n:
            line += '*'
        if i < n - 1:
            line += '\n'
        text += line
    return text

print(Questao1(input('n = ')))
