# Faça um algoritmo que leia a entrada de dois números inteiros e faça a soma entre eles:

#função somar, retorna a soma de dois valores
def somar(a,b):
    return a + b

print("Programa principal\n")
num1 = int(input("Primeiro valor: "))
num2 = int(input("segundo valor: "))

soma = somar(num1,num2) #injeção da função somar

print(f"Soma: {soma}")

