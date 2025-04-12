#!/usr/bin/env python3
# FEN-OSINT Ultimate v5.0

import os
import sys
from modules.ip_lookup import ip_search
from modules.username_search import username_search
from modules.phone_lookup import phone_search

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("""
\033[1;36m
███████╗███████╗███╗   ██╗
██╔════╝██╔════╝████╗  ██║
█████╗  █████╗  ██╔██╗ ██║
██╔══╝  ██╔══╝  ██║╚██╗██║
███████╗███████╗██║ ╚████║
╚══════╝╚══════╝╚═╝  ╚═══╝
\033[1;35m
  OSINT Tool v5.0 | By FEN
\033[0m""")

def check_pass():
    password = input("\033[1;33mВведите пароль: \033[0m")
    return password == "FENDARK"

def main():
    clear()
    banner()
    
    if not check_pass():
        print("\033[1;31mНеверный пароль!\033[0m")
        sys.exit()
    
    while True:
        print("\n\033[1;34mГлавное меню:\033[0m")
        print("1. Поиск по IP")
        print("2. Поиск по имени пользователя")
        print("3. Поиск по номеру телефона")
        print("4. Выход")
        
        choice = input("\n\033[1;35mВыберите вариант: \033[0m")
        
        if choice == "1":
            ip = input("Введите IP-адрес: ")
            ip_search(ip)
        elif choice == "2":
            username = input("Введите имя пользователя: ")
            username_search(username)
        elif choice == "3":
            phone = input("Введите номер телефона: ")
            phone_search(phone)
        elif choice == "4":
            print("\033[1;32mВыход...\033[0m")
            sys.exit()
        else:
            print("\033[1;31mНеверный выбор!\033[0m")
        
        input("\nНажмите Enter чтобы продолжить...")
        clear()
        banner()

if __name__ == "__main__":
    main()
