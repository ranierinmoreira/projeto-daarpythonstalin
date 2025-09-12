<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Versão simplificada do menu para compatibilidade
Para a versão completa com interface retrô, execute main.py
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🎮 MENU PRINCIPAL - VERSÃO SIMPLES")
    print("="*50)
    print("1. 👋 Dizer olá")
    print("2. ➕ Somar dois números")
    print("3. 🎯 Jogo da adivinhação")
    print("4. 🎲 Jogo de dados")
    print("5. 📊 Calculadora básica")
    print("6. ❌ Sair")
    print("="*50)

def dizer_ola():
    print("\n👋 Olá, seja bem-vindo ao sistema!")
    print("🎮 Para uma experiência completa, execute: python main.py")

def somar_numeros():
    try:
        print("\n➕ CALCULADORA DE SOMA")
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = a + b
        print(f"📊 Resultado: {a} + {b} = {resultado}")
    except ValueError:
        print("❌ Por favor, digite apenas números válidos.")

def jogo_adivinhacao():
    import random
    print("\n🎯 JOGO DA ADIVINHAÇÃO")
    print("Pensei em um número entre 1 e 10!")
    
    numero = random.randint(1, 10)
    tentativas = 0
    
    while tentativas < 3:
        tentativas += 1
        try:
            palpite = int(input(f"Tentativa {tentativas}/3 - Seu palpite: "))
            if palpite == numero:
                print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
                return
            elif palpite < numero:
                print("📈 Muito baixo!")
            else:
                print("📉 Muito alto!")
        except ValueError:
            print("❌ Digite um número válido!")
    
    print(f"💀 Game Over! O número era {numero}")

def jogo_dados():
    import random
    print("\n🎲 JOGO DE DADOS")
    
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    
    print(f"🎲 Dado 1: {dado1}")
    print(f"🎲 Dado 2: {dado2}")
    print(f"📊 Soma: {soma}")
    
    if soma == 7:
        print("🎉 Sorte incrível! Você tirou 7!")
    elif soma >= 10:
        print("😎 Boa sorte! Soma alta!")
    else:
        print("😅 Soma baixa, mas ainda é sorte!")

def calculadora_basica():
    print("\n🧮 CALCULADORA BÁSICA")
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("❌ Divisão por zero!")
                return
            resultado = num1 / num2
        else:
            print("❌ Operação inválida!")
            return
        
        print(f"📊 Resultado: {num1} {operacao} {num2} = {resultado}")
    except ValueError:
        print("❌ Por favor, digite apenas números válidos.")

def main():
    print("🎮 BEM-VINDO AO SISTEMA PYTHON STALIN!")
    print("💡 Dica: Para uma experiência completa com interface retrô, execute: python main.py")
    
    while True:
        mostrar_menu()
        escolha = input("\n🎯 Escolha uma opção: ").strip()
=======



# Lista de usuários e senhas (simulação)
usuarios = {
    "admin": "1234",
    "usuario": "senha"
}

def login():
    print("\n===== TELA DE LOGIN =====")
    tentativas = 5

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
            print(f"✅ Login bem-sucedido. Bem-vindo, {usuario}!\n")
            return True
        else:
            tentativas -= 1
            print(f"❌ Usuário ou senha incorretos. Tentativas restantes: {tentativas}")

    print("🚫 Número máximo de tentativas atingido. Encerrando.")
    return False

def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Dizer olá")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")
>>>>>>> 144d771929d0f9e69ef9ac30bdb95d223d4a677d

        if escolha == '1':
            print("Olá! Você está logado com sucesso.")
        elif escolha == '2':
<<<<<<< HEAD
            somar_numeros()
        elif escolha == '3':
            jogo_adivinhacao()
        elif escolha == '4':
            jogo_dados()
        elif escolha == '5':
            calculadora_basica()
        elif escolha == '6':
            print("\n👋 Obrigado por usar o sistema! Até logo!")
            break
        else:
            print("❌ Opção inválida, tente novamente.")
        
        input("\n⏎ Pressione Enter para continuar...")
=======
            print("Saindo... Até logo! Estaremos aguardando você aqui.")
            break
        else:
            print("Opção inválida.")

def main():
    if login():
        menu_principal()
>>>>>>> 144d771929d0f9e69ef9ac30bdb95d223d4a677d

if __name__ == "__main__":
    main()

