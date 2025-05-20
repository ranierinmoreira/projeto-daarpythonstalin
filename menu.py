def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Dizer olá")
    print("2. Somar dois números")
    print("3. Sair")

def dizer_ola():
    print("Olá, seja bem-vindo!")

def somar_numeros():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"A soma é: {a + b}")
    except ValueError:
        print("Por favor, digite apenas números.")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            dizer_ola()
        elif escolha == '2':
            somar_numeros()
        elif escolha == '3':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
