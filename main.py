#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎮 PROJETO DAAR PYTHON STALIN 🐍
Painel de menu em Python com estilo inspirado nos videogames clássicos
Desenvolvido com amor e nostalgia pelos consoles retrô
"""

import os
import sys
import time
import json
from datetime import datetime
from menu_system import MenuSystem
from user_manager import UserManager
from game_engine import GameEngine

class RetroGameConsole:
    """Classe principal que simula um console de videogame retrô"""
    
    def __init__(self):
        self.user_manager = UserManager()
        self.menu_system = MenuSystem()
        self.game_engine = GameEngine()
        self.current_user = None
        self.running = True
        
    def clear_screen(self):
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_ascii_art(self):
        """Exibe arte ASCII do título do jogo"""
        ascii_art = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    ██████╗  █████╗ ██████╗     ██████╗ ██╗   ██╗████████╗   ║
    ║    ██╔══██╗██╔══██╗██╔══██╗   ██╔═══██╗╚██╗ ██╔╝╚══██╔══╝   ║
    ║    ██████╔╝███████║██████╔╝   ██║   ██║ ╚████╔╝    ██║      ║
    ║    ██╔══██╗██╔══██║██╔══██╗   ██║   ██║  ╚██╔╝     ██║      ║
    ║    ██║  ██║██║  ██║██║  ██║   ╚██████╔╝   ██║      ██║      ║
    ║    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝    ╚═╝      ╚═╝      ║
    ║                                                              ║
    ║              🐍 PYTHON STALIN GAME CONSOLE 🎮                ║
    ║                                                              ║
    ║                    Estilo Retrô PS1/N64                     ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
        """
        print(ascii_art)
    
    def loading_animation(self, message="Carregando", duration=3):
        """Animação de loading retrô"""
        print(f"\n{message}", end="")
        for i in range(duration * 4):
            time.sleep(0.25)
            print(".", end="", flush=True)
        print(" ✓")
        time.sleep(0.5)
    
    def startup_sequence(self):
        """Sequência de inicialização do console"""
        self.clear_screen()
        self.print_ascii_art()
        
        print("\n" + "="*60)
        print("🎮 INICIANDO CONSOLE RETRÔ...")
        print("="*60)
        
        self.loading_animation("Inicializando sistema", 2)
        self.loading_animation("Carregando jogos", 2)
        self.loading_animation("Preparando interface", 1)
        
        print("\n✅ Console pronto! Bem-vindo ao mundo retrô!")
        time.sleep(1)
    
    def login_screen(self):
        """Tela de login com estilo retrô"""
        while True:
            self.clear_screen()
            self.print_ascii_art()
            
            print("\n" + "="*50)
            print("🔐 SISTEMA DE LOGIN")
            print("="*50)
            print("\n1. Fazer Login")
            print("2. Criar Conta")
            print("3. Entrar como Visitante")
            print("4. Sair do Sistema")
            
            choice = input("\n🎯 Escolha uma opção: ").strip()
            
            if choice == '1':
                username = input("\n👤 Digite seu nome de usuário: ").strip()
                password = input("🔒 Digite sua senha: ").strip()
                
                if self.user_manager.login(username, password):
                    self.current_user = username
                    print(f"\n✅ Login realizado com sucesso! Bem-vindo, {username}!")
                    time.sleep(2)
                    return True
                else:
                    print("\n❌ Usuário ou senha incorretos!")
                    time.sleep(2)
            
            elif choice == '2':
                username = input("\n👤 Digite um nome de usuário: ").strip()
                password = input("🔒 Digite uma senha: ").strip()
                
                if self.user_manager.create_user(username, password):
                    print(f"\n✅ Conta criada com sucesso! Bem-vindo, {username}!")
                    self.current_user = username
                    time.sleep(2)
                    return True
                else:
                    print("\n❌ Erro ao criar conta. Usuário já existe!")
                    time.sleep(2)
            
            elif choice == '3':
                self.current_user = "Visitante"
                print("\n👋 Entrando como visitante...")
                time.sleep(1)
                return True
            
            elif choice == '4':
                print("\n👋 Obrigado por usar o Console Retrô! Até logo!")
                return False
            
            else:
                print("\n❌ Opção inválida! Tente novamente.")
                time.sleep(1)
    
    def main_menu(self):
        """Menu principal do jogo"""
        while self.running:
            self.clear_screen()
            self.print_ascii_art()
            
            print(f"\n👤 Usuário: {self.current_user}")
            print("="*60)
            print("🎮 MENU PRINCIPAL")
            print("="*60)
            
            print("\n1. 🎯 Minijogos")
            print("2. 🧮 Calculadora Avançada")
            print("3. 📊 Estatísticas")
            print("4. ⚙️  Configurações")
            print("5. 👤 Perfil do Usuário")
            print("6. 🏆 Ranking")
            print("7. ❌ Sair")
            
            choice = input("\n🎯 Escolha uma opção: ").strip()
            
            if choice == '1':
                self.game_engine.minigames_menu()
            elif choice == '2':
                self.game_engine.calculator_menu()
            elif choice == '3':
                self.show_statistics()
            elif choice == '4':
                self.settings_menu()
            elif choice == '5':
                self.user_profile_menu()
            elif choice == '6':
                self.ranking_menu()
            elif choice == '7':
                self.exit_game()
            else:
                print("\n❌ Opção inválida! Tente novamente.")
                time.sleep(1)
    
    def show_statistics(self):
        """Mostra estatísticas do usuário"""
        self.clear_screen()
        print("\n" + "="*50)
        print("📊 ESTATÍSTICAS DO USUÁRIO")
        print("="*50)
        
        stats = self.user_manager.get_user_stats(self.current_user)
        print(f"\n👤 Usuário: {self.current_user}")
        print(f"🎮 Jogos jogados: {stats.get('games_played', 0)}")
        print(f"🏆 Pontuação total: {stats.get('total_score', 0)}")
        print(f"📅 Último acesso: {stats.get('last_access', 'Nunca')}")
        
        input("\n⏎ Pressione Enter para voltar...")
    
    def settings_menu(self):
        """Menu de configurações"""
        while True:
            self.clear_screen()
            print("\n" + "="*50)
            print("⚙️  CONFIGURAÇÕES")
            print("="*50)
            print("\n1. 🎨 Alterar tema")
            print("2. 🔊 Configurar som")
            print("3. 📱 Informações do sistema")
            print("4. ⬅️  Voltar")
            
            choice = input("\n🎯 Escolha uma opção: ").strip()
            
            if choice == '1':
                print("\n🎨 Tema alterado para: Retrô Clássico")
                time.sleep(1)
            elif choice == '2':
                print("\n🔊 Configurações de som salvas!")
                time.sleep(1)
            elif choice == '3':
                print(f"\n📱 Sistema: Python {sys.version.split()[0]}")
                print(f"🖥️  Plataforma: {sys.platform}")
                print(f"📁 Diretório: {os.getcwd()}")
                input("\n⏎ Pressione Enter para continuar...")
            elif choice == '4':
                break
            else:
                print("\n❌ Opção inválida!")
                time.sleep(1)
    
    def user_profile_menu(self):
        """Menu do perfil do usuário"""
        self.clear_screen()
        print("\n" + "="*50)
        print("👤 PERFIL DO USUÁRIO")
        print("="*50)
        
        print(f"\n👤 Nome: {self.current_user}")
        print(f"📅 Membro desde: {datetime.now().strftime('%d/%m/%Y')}")
        print(f"🎮 Nível: Iniciante")
        print(f"⭐ Experiência: 0 XP")
        
        input("\n⏎ Pressione Enter para voltar...")
    
    def ranking_menu(self):
        """Menu de ranking"""
        self.clear_screen()
        print("\n" + "="*50)
        print("🏆 RANKING DE JOGADORES")
        print("="*50)
        
        rankings = self.user_manager.get_rankings()
        if rankings:
            for i, (user, score) in enumerate(rankings[:10], 1):
                medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
                print(f"{medal} {user}: {score} pontos")
        else:
            print("\n📊 Nenhum jogador no ranking ainda!")
        
        input("\n⏎ Pressione Enter para voltar...")
    
    def exit_game(self):
        """Sai do jogo com animação"""
        self.clear_screen()
        print("\n" + "="*50)
        print("👋 SAINDO DO CONSOLE RETRÔ...")
        print("="*50)
        
        self.loading_animation("Salvando progresso", 2)
        print("\n✅ Progresso salvo com sucesso!")
        print("🎮 Obrigado por jogar! Até a próxima!")
        time.sleep(2)
        
        self.running = False
    
    def run(self):
        """Executa o jogo principal"""
        try:
            self.startup_sequence()
            
            if self.login_screen():
                self.main_menu()
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Jogo interrompido pelo usuário!")
            print("👋 Até logo!")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("🔄 Reiniciando o sistema...")
            time.sleep(3)
            self.run()

if __name__ == "__main__":
    console = RetroGameConsole()
    console.run()
