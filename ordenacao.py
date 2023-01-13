num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 < num2 and num1 < num3 and num2 > num1 and num3 > num2:
    print("crescente")
else:
    print("não está em ordem crescente")