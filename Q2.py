#Autor: Gabriel Kleiman
def Questao2(senha):
    if type(senha) != str:
        try:
            senha = str(senha)
        except:
            return False
    setSenha = set(senha)
    faltam = 0
    digitos  = set([str(i) for i in range(10)])
    especiais = set('!@#$%^&*()-+')
    if len(setSenha.intersection(digitos)) == 0:
        faltam += 1
    if len(setSenha.difference(digitos).difference(especiais).intersection(set(senha.upper()))) == 0:
        faltam += 1
    if len(setSenha.difference(digitos).difference(especiais).intersection(set(senha.lower()))) == 0:
        faltam += 1
    if len(setSenha.intersection(especiais)) == 0:
        faltam += 1
    if len(senha) + faltam >= 6:
        return faltam
    else:
        return 6 - len(senha)

print(Questao2(input('Senha = ')))
