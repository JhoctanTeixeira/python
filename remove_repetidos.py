def remove_repetidos(lista):
    lista3 = []
    
    for x in lista:
        if x not in lista3:
            lista3.append(x)
            
    lista3_ordenada = sorted(lista3)
    return lista3_ordenada     
    
valor_retornado = remove_repetidos([])

print(valor_retornado)
