# Criar um programa que leia a altura e o peso de N pessoas e mostre
# seu IMC com a respectiva classificação. O cálculo do IMC deverá ser
# realizado através de uma função que receberá os valores de entrada
# necessários para o cálculo.
# Fórmula --> IMC = PESO / (ALTURA * ALTURA)

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def classificar_imc(imc):
    if imc < 16.9:
        return "Muito abaixo do peso"
    elif 17 <= imc <= 18.4:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Acima do peso"
    elif 30<= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 40:
        return "Obesidade grau 2"
    else:
        return"Obesidade grau 3"
    
print("-- Cálculo do IMC --")
quant = int(input("Quantas pessoas deseja calcular: "))

for i in range(quant):
    print(f"Pessoa {i}")
    peso = float(input("Entre com o peso em (Kg): ").replace(",","."))
    altura = float(input("Entre com o a altura em (M): ").replace(",","."))

    imc = calcular_imc(peso,altura)
    classificacao = classificar_imc(imc)

    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

print("-- Fim do programa --")




