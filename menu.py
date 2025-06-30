


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

        if escolha == '1':
            print("Olá! Você está logado com sucesso.")
        elif escolha == '2':
            print("Saindo... Até logo! Estaremos aguardando você aqui.")
            break
        else:
            print("Opção inválida.")

def main():
    if login():
        menu_principal()

if __name__ == "__main__":
    main()

