# Funcao Soma
def soma_elementos(lista):
    soma = 0
    for x in lista:
        soma = soma + x
    return soma

lista = [1, 2, 3]
resultado = soma_elementos(lista)
print(resultado)
