#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de menus para o Console Retrô
"""

import time
import os

class MenuSystem:
    """Classe responsável pelos menus e interface do usuário"""
    
    def __init__(self):
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'bold': '\033[1m',
            'end': '\033[0m'
        }
    
    def print_colored(self, text, color='white'):
        """Imprime texto colorido"""
        print(f"{self.colors.get(color, self.colors['white'])}{text}{self.colors['end']}")
    
    def print_header(self, title, width=60):
        """Imprime cabeçalho estilizado"""
        print("\n" + "="*width)
        self.print_colored(f"🎮 {title}", 'cyan')
        print("="*width)
    
    def print_option(self, number, text, color='white'):
        """Imprime opção do menu"""
        self.print_colored(f"{number}. {text}", color)
    
    def print_success(self, message):
        """Imprime mensagem de sucesso"""
        self.print_colored(f"✅ {message}", 'green')
    
    def print_error(self, message):
        """Imprime mensagem de erro"""
        self.print_colored(f"❌ {message}", 'red')
    
    def print_warning(self, message):
        """Imprime mensagem de aviso"""
        self.print_colored(f"⚠️  {message}", 'yellow')
    
    def print_info(self, message):
        """Imprime mensagem informativa"""
        self.print_colored(f"ℹ️  {message}", 'blue')
    
    def print_separator(self, char="─", width=60):
        """Imprime separador"""
        print(char * width)
    
    def animate_text(self, text, delay=0.05):
        """Anima texto letra por letra"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def countdown(self, seconds=3, message="Iniciando"):
        """Contagem regressiva"""
        for i in range(seconds, 0, -1):
            print(f"\r{message} em {i}...", end='', flush=True)
            time.sleep(1)
        print(f"\r{message} agora!     ")
    
    def loading_bar(self, duration=3, message="Carregando"):
        """Barra de carregamento animada"""
        print(f"\n{message}")
        for i in range(20):
            bar = "█" * i + "░" * (20 - i)
            print(f"\r[{bar}] {i*5}%", end='', flush=True)
            time.sleep(duration / 20)
        print(f"\r[{'█' * 20}] 100% ✓")
    
    def clear_screen(self):
        """Limpa a tela"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pause(self, message="Pressione Enter para continuar..."):
        """Pausa e aguarda input do usuário"""
        input(f"\n⏎ {message}")
    
    def get_user_input(self, prompt, input_type=str, valid_options=None):
        """Obtém input do usuário com validação"""
        while True:
            try:
                user_input = input(f"\n{prompt}: ").strip()
                
                if not user_input:
                    self.print_error("Entrada vazia! Tente novamente.")
                    continue
                
                if valid_options and user_input not in valid_options:
                    self.print_error(f"Opção inválida! Escolha entre: {', '.join(valid_options)}")
                    continue
                
                if input_type == int:
                    return int(user_input)
                elif input_type == float:
                    return float(user_input)
                else:
                    return user_input
                    
            except ValueError:
                self.print_error("Formato inválido! Tente novamente.")
            except KeyboardInterrupt:
                self.print_warning("Operação cancelada pelo usuário.")
                return None
    
    def confirm_action(self, message):
        """Confirma uma ação com o usuário"""
        while True:
            response = input(f"\n{message} (s/n): ").strip().lower()
            if response in ['s', 'sim', 'y', 'yes']:
                return True
            elif response in ['n', 'não', 'nao', 'no']:
                return False
            else:
                self.print_error("Resposta inválida! Digite 's' para sim ou 'n' para não.")
    
    def display_ascii_art(self, art_name):
        """Exibe arte ASCII específica"""
        arts = {
            'game_over': """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗ ║
    ║   ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║ ║
    ║   ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║ ║
    ║   ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝ ║
    ║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝  ║
    ║    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝   ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
            """,
            'victory': """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗  ║
    ║    ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝  ║
    ║    ██║   ██║██║██║        ██║   ██║   ██║██████╔╝  ╚████╔╝   ║
    ║    ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗   ╚██╔╝    ║
    ║     ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║    ██║     ║
    ║      ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
            """,
            'loading': """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    ██╗     ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗    ║
    ║    ██║    ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝    ║
    ║    ██║    ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗   ║
    ║    ██║    ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║   ║
    ║    ██║    ╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝   ║
    ║    ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝    ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
            """
        }
        
        if art_name in arts:
            self.print_colored(arts[art_name], 'cyan')
