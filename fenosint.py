from rich.console import Console
from rich.panel import Panel

def show_banner():
    console = Console()
    banner = """
[bold red]
 ██████╗ ███████╗███╗   ██╗
██╔═══██╗██╔════╝████╗  ██║
██║   ██║███████╗██╔██╗ ██║
██║   ██║╚════██║██║╚██╗██║
╚██████╔╝███████║██║ ╚████║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝
[bold blue]
 ██████╗ ███████╗███╗   ██╗██╗████████╗
██╔═══██╗██╔════╝████╗  ██║██║╚══██╔══╝
██║   ██║███████╗██╔██╗ ██║██║   ██║   
██║   ██║╚════██║██║╚██╗██║██║   ██║   
╚██████╔╝███████║██║ ╚████║██║   ██║   
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝   ╚═╝   
[/bold blue]
[bold green]
      Termux OSINT Tool v7.0
      Created by [bold yellow]FEN[/bold yellow]
[/bold green]
"""
    console.print(Panel.fit(banner, style="bold cyan"))
    show_banner()  # Показ баннера при запуске
#!/usr/bin/env python3
# FEN-OSINT UltraLite v6.0 - гарантированно работает в Termux

import os
import requests
from rich.console import Console

console = Console()
PASSWORD = "FENDARK"

def clear():
    os.system('clear')

def show_menu():
    clear()
    console.print("[bold green]FEN-OSINT UltraLite v6.0[/]")
    console.print("[yellow]1. Поиск по IP[/]\n[yellow]2. Поиск по имени[/]\n[yellow]3. Выход[/]")
    
    choice = input("Выберите: ")
    if choice == "1":
        ip = input("Введите IP: ")
        result = requests.get(f"http://ip-api.com/json/{ip}").json()
        console.print(f"[green]Страна:[/] {result.get('country', '?')}")
        console.print(f"[green]Город:[/] {result.get('city', '?')}")
    elif choice == "2":
        user = input("Введите имя: ")
        console.print(f"[green]Проверяю GitHub...[/]")
        if requests.get(f"https://github.com/{user}").status_code == 200:
            console.print(f"[green]Найден:[/] github.com/{user}")
    elif choice == "3":
        exit()

if __name__ == "__main__":
    if input("Пароль: ") == PASSWORD:
        while True:
            try:
                show_menu()
                input("\nEnter чтобы продолжить...")
            except:
                console.print("[red]Ошибка! Проверьте интернет.[/]")
    else:
        console.print("[red]Неверный пароль![/]")
