#!/usr/bin/env python3
# FEN-OSINT v8.0

import os
import sys
import requests
from rich.console import Console
from rich.panel import Panel

console = Console()
ACCESS_CODE = "FENDARK"  # Измените этот код!

def show_banner():
    console.print(Panel.fit("""
[bold red]
 ██████╗ ███████╗███╗   ██╗
██╔═══██╗██╔════╝████╗  ██║
██║   ██║███████╗██╔██╗ ██║
██║   ██║╚════██║██║╚██╗██║
╚██████╔╝███████║██║ ╚████║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝
[/bold red][bold blue]
 ██████╗ ███████╗███╗   ██╗██╗████████╗
██╔═══██╗██╔════╝████╗  ██║██║╚══██╔══╝
██║   ██║███████╗██╔██╗ ██║██║   ██║   
██║   ██║╚════██║██║╚██╗██║██║   ██║   
╚██████╔╝███████║██║ ╚████║██║   ██║   
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝   ╚═╝   
[/bold blue][bold green]
      Termux OSINT Tool v8.0
      Created by [bold yellow]FEN[/bold yellow]
[/bold green]"""))

def check_code():
    for attempt in range(3):
        code = input("[?] Введите код доступа: ")
        if code == ACCESS_CODE:
            return True
        print(f"[!] Неверный код! Попыток осталось: {2-attempt}")
    return False

def main_menu():
    while True:
        console.print("\n[bold cyan]ГЛАВНОЕ МЕНЮ[/bold cyan]")
        console.print("1. Поиск по IP\n2. Поиск по имени\n3. Выход")
        choice = input("> ")
        
        if choice == "1":
            ip = input("IP: ")
            data = requests.get(f"http://ip-api.com/json/{ip}").json()
            console.print(f"[green]Страна:[/green] {data.get('country', '?')}")
        elif choice == "2":
            user = input("Имя: ")
            console.print(f"[green]Проверяю GitHub...[/green]")
            if requests.get(f"https://github.com/{user}").status_code == 200:
                console.print(f"[green]Найден: github.com/{user}[/green]")
        elif choice == "3":
            sys.exit()
        else:
            console.print("[red]Неверный выбор![/red]")

if __name__ == "__main__":
    os.system("clear")
    show_banner()
    if check_code():
        while True:
            try:
                main_menu()
            except Exception as e:
                console.print(f"[red]Ошибка: {e}[/red]")
    else:
        console.print("[red]Доступ запрещен![/red]")
        sys.exit()
