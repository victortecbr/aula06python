# Com base no exemplo, implemente as funções de subtração, multiplicação, divisão e a média
# entre eles:

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b != 0:
        return a / b
    else:
        return "Divisão inválida por zero"

def media(a,b):
        return (a + b) / 2

print("Programa principal\n")
num1 = int(input("Primeiro valor: "))
num2 = int(input("segundo valor: "))

soma = somar(num1,num2) #injeção da função somar
sub = subtrair(num1,num2) #injeção da função subtrair
mult = multiplicar(num1,num2) #injeção da função multiplicar
div = dividir(num1,num2) #injeção da função dividir
med = media(num1,num2) #injeção da função media

print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")
print(f"Média: {med}")