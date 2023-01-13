largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

contL = 0
contA = 0

while contL < largura:
    contL = contL + 1
    while contL == largura and contA < altura:
        rashA = "#"
        print(rashA * largura, end="\n")
        contA = contA + 1