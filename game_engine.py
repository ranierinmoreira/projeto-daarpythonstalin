#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de jogos para o Console Retrô
Contém minijogos e funcionalidades de entretenimento
"""

import random
import time
import math
from menu_system import MenuSystem

class GameEngine:
    """Classe responsável pelos jogos e funcionalidades de entretenimento"""
    
    def __init__(self):
        self.menu = MenuSystem()
        self.score = 0
        self.games_played = 0
    
    def minigames_menu(self):
        """Menu de minijogos"""
        while True:
            self.menu.clear_screen()
            self.menu.print_header("MINIJOGOS RETRÔ")
            
            self.menu.print_option("1", "🎯 Jogo da Adivinhação", 'green')
            self.menu.print_option("2", "🎲 Dados da Sorte", 'blue')
            self.menu.print_option("3", "🔢 Calculadora de Idade", 'yellow')
            self.menu.print_option("4", "🎨 Gerador de Arte ASCII", 'purple')
            self.menu.print_option("5", "🧠 Teste de Memória", 'cyan')
            self.menu.print_option("6", "🎵 Simulador de Piano", 'red')
            self.menu.print_option("7", "⬅️  Voltar ao Menu Principal", 'white')
            
            choice = self.menu.get_user_input("🎯 Escolha um minijogo", valid_options=['1', '2', '3', '4', '5', '6', '7'])
            
            if choice == '1':
                self.guessing_game()
            elif choice == '2':
                self.dice_game()
            elif choice == '3':
                self.age_calculator()
            elif choice == '4':
                self.ascii_art_generator()
            elif choice == '5':
                self.memory_test()
            elif choice == '6':
                self.piano_simulator()
            elif choice == '7':
                break
            else:
                self.menu.print_error("Opção inválida!")
                time.sleep(1)
    
    def guessing_game(self):
        """Jogo da adivinhação"""
        self.menu.clear_screen()
        self.menu.print_header("JOGO DA ADIVINHAÇÃO")
        
        self.menu.print_info("Pensei em um número entre 1 e 100!")
        self.menu.print_info("Você tem 7 tentativas para adivinhar!")
        
        number = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        while attempts < max_attempts:
            attempts += 1
            remaining = max_attempts - attempts + 1
            
            guess = self.menu.get_user_input(f"Tentativa {attempts}/{max_attempts} - Digite seu palpite", int)
            if guess is None:
                return
            
            if guess == number:
                self.menu.print_success(f"🎉 Parabéns! Você acertou em {attempts} tentativas!")
                self.score += (max_attempts - attempts + 1) * 10
                self.games_played += 1
                break
            elif guess < number:
                self.menu.print_warning(f"📈 Muito baixo! Restam {remaining-1} tentativas.")
            else:
                self.menu.print_warning(f"📉 Muito alto! Restam {remaining-1} tentativas.")
        
        if attempts >= max_attempts:
            self.menu.print_error(f"💀 Game Over! O número era {number}")
        
        self.menu.pause()
    
    def dice_game(self):
        """Jogo de dados"""
        self.menu.clear_screen()
        self.menu.print_header("DADOS DA SORTE")
        
        self.menu.print_info("Role os dados e tente acertar a soma!")
        
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        
        guess = self.menu.get_user_input("Qual será a soma dos dois dados? (2-12)", int)
        if guess is None:
            return
        
        self.menu.print_info("Rolando os dados...")
        time.sleep(1)
        
        # Animação dos dados
        for _ in range(3):
            print("🎲", end="", flush=True)
            time.sleep(0.3)
        
        print(f"\n\n🎲 Dado 1: {dice1}")
        print(f"🎲 Dado 2: {dice2}")
        print(f"📊 Soma: {total}")
        
        if guess == total:
            self.menu.print_success("🎉 Sorte incrível! Você acertou!")
            self.score += 50
        else:
            self.menu.print_warning(f"😅 Quase! A soma era {total}")
            self.score += 10
        
        self.games_played += 1
        self.menu.pause()
    
    def age_calculator(self):
        """Calculadora de idade"""
        self.menu.clear_screen()
        self.menu.print_header("CALCULADORA DE IDADE")
        
        birth_year = self.menu.get_user_input("Digite seu ano de nascimento", int)
        if birth_year is None:
            return
        
        current_year = time.localtime().tm_year
        age = current_year - birth_year
        
        if age < 0:
            self.menu.print_error("Ano de nascimento inválido!")
        else:
            self.menu.print_success(f"Você tem {age} anos!")
            
            # Informações extras
            days_old = age * 365
            hours_old = days_old * 24
            minutes_old = hours_old * 60
            
            print(f"\n📊 Estatísticas da sua idade:")
            print(f"📅 Dias vividos: {days_old:,}")
            print(f"⏰ Horas vividas: {hours_old:,}")
            print(f"⏱️  Minutos vividos: {minutes_old:,}")
            
            if age >= 18:
                print(f"🍺 Você pode beber legalmente há {age-18} anos!")
            else:
                print(f"👶 Você ainda é menor de idade!")
        
        self.menu.pause()
    
    def ascii_art_generator(self):
        """Gerador de arte ASCII"""
        self.menu.clear_screen()
        self.menu.print_header("GERADOR DE ARTE ASCII")
        
        arts = {
            '1': ('Coração', '❤️', '    ♥♥♥     ♥♥♥\n  ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥\n ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\n  ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\n   ♥♥♥♥♥♥♥♥♥♥♥♥♥\n    ♥♥♥♥♥♥♥♥♥♥♥\n     ♥♥♥♥♥♥♥♥♥\n      ♥♥♥♥♥♥♥\n       ♥♥♥♥♥\n        ♥♥♥\n         ♥'),
            '2': ('Casa', '🏠', '    /\\\n   /  \\\n  /____\\\n  |    |\n  |    |\n  |____|'),
            '3': ('Estrela', '⭐', '    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *'),
            '4': ('Smiley', '😊', '  ********\n *        *\n*  O    O  *\n*    ^     *\n*  \\___/   *\n *        *\n  ********'),
            '5': ('Árvore', '🌲', '    *\n   ***\n  *****\n *******\n*********\n   |||\n   |||\n   |||')
        }
        
        print("\nEscolha uma arte ASCII para gerar:")
        for key, (name, emoji, art) in arts.items():
            self.menu.print_option(key, f"{emoji} {name}")
        
        choice = self.menu.get_user_input("Escolha uma opção", valid_options=list(arts.keys()))
        if choice is None:
            return
        
        name, emoji, art = arts[choice]
        print(f"\n{emoji} {name}:")
        print(art)
        
        self.menu.pause()
    
    def memory_test(self):
        """Teste de memória"""
        self.menu.clear_screen()
        self.menu.print_header("TESTE DE MEMÓRIA")
        
        self.menu.print_info("Memorize a sequência de números que aparecerá!")
        self.menu.pause("Pressione Enter quando estiver pronto...")
        
        # Gera sequência aleatória
        sequence_length = 4
        sequence = [random.randint(1, 9) for _ in range(sequence_length)]
        
        # Mostra a sequência
        self.menu.clear_screen()
        print("\n🔢 Memorize esta sequência:")
        for num in sequence:
            print(f"  {num}", end="", flush=True)
            time.sleep(1)
        
        print("\n\n" + "="*50)
        self.menu.countdown(3, "Agora digite a sequência")
        
        # Pede para o usuário repetir
        user_sequence = []
        for i in range(sequence_length):
            num = self.menu.get_user_input(f"Digite o {i+1}º número", int)
            if num is None:
                return
            user_sequence.append(num)
        
        # Verifica se está correto
        if user_sequence == sequence:
            self.menu.print_success("🎉 Excelente memória! Sequência correta!")
            self.score += 30
        else:
            self.menu.print_error("😞 Sequência incorreta!")
            print(f"Sequência correta: {sequence}")
            print(f"Sua sequência: {user_sequence}")
        
        self.games_played += 1
        self.menu.pause()
    
    def piano_simulator(self):
        """Simulador de piano"""
        self.menu.clear_screen()
        self.menu.print_header("SIMULADOR DE PIANO")
        
        self.menu.print_info("Digite as teclas do piano (1-7) ou 'q' para sair")
        print("\n🎹 Teclas do piano:")
        print("1 = Dó    2 = Ré    3 = Mi    4 = Fá")
        print("5 = Sol   6 = Lá    7 = Si    q = Sair")
        
        notes = {
            '1': ('Dó', '🎵'),
            '2': ('Ré', '🎶'),
            '3': ('Mi', '🎼'),
            '4': ('Fá', '🎹'),
            '5': ('Sol', '🎺'),
            '6': ('Lá', '🎻'),
            '7': ('Si', '🎸')
        }
        
        melody = []
        
        while True:
            key = input("\n🎹 Digite uma tecla: ").strip()
            
            if key.lower() == 'q':
                break
            elif key in notes:
                note_name, emoji = notes[key]
                print(f"{emoji} {note_name}")
                melody.append(note_name)
            else:
                self.menu.print_error("Tecla inválida!")
        
        if melody:
            print(f"\n🎼 Sua melodia: {' - '.join(melody)}")
            self.score += len(melody) * 2
        
        self.games_played += 1
        self.menu.pause()
    
    def calculator_menu(self):
        """Menu da calculadora avançada"""
        while True:
            self.menu.clear_screen()
            self.menu.print_header("CALCULADORA AVANÇADA")
            
            self.menu.print_option("1", "➕ Operações Básicas", 'green')
            self.menu.print_option("2", "📐 Funções Matemáticas", 'blue')
            self.menu.print_option("3", "🔢 Conversor de Bases", 'yellow')
            self.menu.print_option("4", "📊 Estatísticas", 'purple')
            self.menu.print_option("5", "⬅️  Voltar", 'white')
            
            choice = self.menu.get_user_input("Escolha uma opção", valid_options=['1', '2', '3', '4', '5'])
            
            if choice == '1':
                self.basic_calculator()
            elif choice == '2':
                self.math_functions()
            elif choice == '3':
                self.base_converter()
            elif choice == '4':
                self.statistics_calculator()
            elif choice == '5':
                break
    
    def basic_calculator(self):
        """Calculadora básica"""
        self.menu.clear_screen()
        self.menu.print_header("CALCULADORA BÁSICA")
        
        try:
            num1 = self.menu.get_user_input("Digite o primeiro número", float)
            if num1 is None:
                return
            
            operation = self.menu.get_user_input("Digite a operação (+, -, *, /, **)", valid_options=['+', '-', '*', '/', '**'])
            if operation is None:
                return
            
            num2 = self.menu.get_user_input("Digite o segundo número", float)
            if num2 is None:
                return
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    self.menu.print_error("Divisão por zero!")
                    return
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            
            self.menu.print_success(f"Resultado: {num1} {operation} {num2} = {result}")
            
        except Exception as e:
            self.menu.print_error(f"Erro no cálculo: {e}")
        
        self.menu.pause()
    
    def math_functions(self):
        """Funções matemáticas"""
        self.menu.clear_screen()
        self.menu.print_header("FUNÇÕES MATEMÁTICAS")
        
        num = self.menu.get_user_input("Digite um número", float)
        if num is None:
            return
        
        print(f"\n📊 Funções matemáticas para {num}:")
        print(f"√ Raiz quadrada: {math.sqrt(abs(num)):.2f}")
        print(f"² Quadrado: {num**2}")
        print(f"³ Cubo: {num**3}")
        print(f"sin Seno: {math.sin(math.radians(num)):.4f}")
        print(f"cos Cosseno: {math.cos(math.radians(num)):.4f}")
        print(f"tan Tangente: {math.tan(math.radians(num)):.4f}")
        print(f"log Logaritmo: {math.log10(abs(num)) if num != 0 else 'Indefinido'}")
        print(f"ln Logaritmo natural: {math.log(abs(num)) if num != 0 else 'Indefinido'}")
        
        self.menu.pause()
    
    def base_converter(self):
        """Conversor de bases numéricas"""
        self.menu.clear_screen()
        self.menu.print_header("CONVERSOR DE BASES")
        
        number = self.menu.get_user_input("Digite um número decimal", int)
        if number is None:
            return
        
        print(f"\n🔢 Conversões do número {number}:")
        print(f"Binário (base 2): {bin(number)}")
        print(f"Octal (base 8): {oct(number)}")
        print(f"Hexadecimal (base 16): {hex(number).upper()}")
        
        self.menu.pause()
    
    def statistics_calculator(self):
        """Calculadora de estatísticas"""
        self.menu.clear_screen()
        self.menu.print_header("CALCULADORA DE ESTATÍSTICAS")
        
        self.menu.print_info("Digite números separados por vírgula")
        numbers_input = input("Números: ").strip()
        
        try:
            numbers = [float(x.strip()) for x in numbers_input.split(',')]
            
            if not numbers:
                self.menu.print_error("Nenhum número fornecido!")
                return
            
            # Calcula estatísticas
            n = len(numbers)
            total = sum(numbers)
            mean = total / n
            sorted_nums = sorted(numbers)
            
            if n % 2 == 0:
                median = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
            else:
                median = sorted_nums[n//2]
            
            variance = sum((x - mean)**2 for x in numbers) / n
            std_dev = math.sqrt(variance)
            
            print(f"\n📊 Estatísticas dos {n} números:")
            print(f"📈 Soma: {total}")
            print(f"📊 Média: {mean:.2f}")
            print(f"📋 Mediana: {median:.2f}")
            print(f"📉 Menor valor: {min(numbers)}")
            print(f"📈 Maior valor: {max(numbers)}")
            print(f"📊 Variância: {variance:.2f}")
            print(f"📊 Desvio padrão: {std_dev:.2f}")
            
        except ValueError:
            self.menu.print_error("Formato inválido! Use números separados por vírgula.")
        
        self.menu.pause()
