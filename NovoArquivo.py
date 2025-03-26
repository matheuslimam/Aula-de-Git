# Calculadora de IMC (Índice de Massa Corporal)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    try:
        idade = int(input("Digite sua idade: "))
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
        
        if imc < 18.5:
            print("Você está abaixo do peso.")
        elif 18.5 <= imc < 24.9:
            print("Você está com peso normal.")
        elif 25 <= imc < 29.9:
            print("Você está com sobrepeso.")
        else:
            print("Você está com obesidade.")
    except ValueError:
        print("Por favor, insira valores válidos.")

if __name__ == "__main__":
    main()