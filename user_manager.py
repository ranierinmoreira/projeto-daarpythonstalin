#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de gerenciamento de usuários para o Console Retrô
"""

import json
import os
from datetime import datetime

class UserManager:
    """Classe responsável pelo gerenciamento de usuários e dados"""
    
    def __init__(self):
        self.users_file = "users.json"
        self.users_data = self.load_users()
    
    def load_users(self):
        """Carrega dados dos usuários do arquivo JSON"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}
    
    def save_users(self):
        """Salva dados dos usuários no arquivo JSON"""
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(self.users_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar usuários: {e}")
            return False
    
    def create_user(self, username, password):
        """Cria um novo usuário"""
        if username in self.users_data:
            return False
        
        self.users_data[username] = {
            "password": password,
            "created_at": datetime.now().isoformat(),
            "last_access": datetime.now().isoformat(),
            "games_played": 0,
            "total_score": 0,
            "level": 1,
            "experience": 0,
            "achievements": []
        }
        
        return self.save_users()
    
    def login(self, username, password):
        """Faz login do usuário"""
        if username in self.users_data:
            if self.users_data[username]["password"] == password:
                # Atualiza último acesso
                self.users_data[username]["last_access"] = datetime.now().isoformat()
                self.save_users()
                return True
        return False
    
    def get_user_stats(self, username):
        """Retorna estatísticas do usuário"""
        if username == "Visitante":
            return {
                "games_played": 0,
                "total_score": 0,
                "last_access": "Agora",
                "level": 1,
                "experience": 0
            }
        
        if username in self.users_data:
            user_data = self.users_data[username]
            return {
                "games_played": user_data.get("games_played", 0),
                "total_score": user_data.get("total_score", 0),
                "last_access": user_data.get("last_access", "Nunca"),
                "level": user_data.get("level", 1),
                "experience": user_data.get("experience", 0)
            }
        
        return {}
    
    def update_user_score(self, username, score):
        """Atualiza pontuação do usuário"""
        if username == "Visitante":
            return
        
        if username in self.users_data:
            self.users_data[username]["total_score"] += score
            self.users_data[username]["games_played"] += 1
            
            # Sistema de experiência simples
            exp_gained = score // 10
            self.users_data[username]["experience"] += exp_gained
            
            # Sistema de níveis
            level = self.users_data[username]["level"]
            exp_needed = level * 100
            if self.users_data[username]["experience"] >= exp_needed:
                self.users_data[username]["level"] += 1
                print(f"\n🎉 Parabéns! Você subiu para o nível {self.users_data[username]['level']}!")
            
            self.save_users()
    
    def get_rankings(self):
        """Retorna ranking dos usuários por pontuação"""
        rankings = []
        for username, data in self.users_data.items():
            rankings.append((username, data.get("total_score", 0)))
        
        return sorted(rankings, key=lambda x: x[1], reverse=True)
    
    def add_achievement(self, username, achievement):
        """Adiciona conquista ao usuário"""
        if username == "Visitante":
            return
        
        if username in self.users_data:
            if achievement not in self.users_data[username]["achievements"]:
                self.users_data[username]["achievements"].append(achievement)
                print(f"\n🏆 Nova conquista desbloqueada: {achievement}!")
                self.save_users()
