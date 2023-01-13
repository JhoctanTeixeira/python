largura = int(input("Digite um numero para largura: "))
altura = int(input("Digite um numero para altura: "))

contA = 0
nul = " "
vaz = nul * (largura - 4)
rashA = "#"

a = altura - 2

if  largura == 2 and altura == 2:
    print(rashA * largura)
    print(rashA * largura)

while contA < (altura - 2):
    contA = contA + 1

    if contA == 1:     
        print(rashA * largura)
    
    print(rashA, vaz ,rashA)
    
    if contA == a:
        print(rashA * largura)