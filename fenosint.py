#!/usr/bin/env python3
# FEN-OSINT Ultimate v4.0
# Developer: FEN
# GitHub: https://github.com/FENRTH/FEN-OSINT

import os
import sys
import json
import requests
import platform
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
CONFIG_DIR = os.path.expanduser("~/.fenosint")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
PASSWORD = "FENDARK"
VERSION = "4.0"

class FENOSINT:
    def __init__(self):
        self.config = self.load_config()
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'FEN-OSINT/4.0'})

    def load_config(self):
        default_config = {
            "api_keys": {"numlookup": None},
            "settings": {"timeout": 15}
        }
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, "r") as f:
                    return json.load(f)
        except:
            pass
        return default_config

    def check_password(self):
        for _ in range(3):
            if getpass("[?] Password: ") == PASSWORD:
                return True
            print("[!] Invalid password!")
        return False

    def ip_lookup(self, ip):
        try:
            response = self.session.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            table = Table(title="IP Info")
            table.add_column("Field", style="cyan")
            table.add_column("Value", style="green")
            for k, v in data.items():
                table.add_row(k, str(v))
            console.print(table)
        except Exception as e:
            print(f"[!] Error: {e}")

    def username_search(self, username):
        sites = {
            "GitHub": f"https://github.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "VK": f"https://vk.com/{username}"
        }
        results = []
        for site, url in sites.items():
            try:
                if requests.head(url).status_code == 200:
                    results.append(f"[+] {site}: {url}")
            except:
                results.append(f"[!] {site} error")
        console.print(Panel("\n".join(results)))

    def show_menu(self):
        while True:
            console.print("\n[bold]FEN-OSINT MENU[/bold]")
            console.print("1. IP Lookup\n2. Username Search\n3. Exit")
            choice = input("Select: ")
            
            if choice == "1":
                self.ip_lookup(input("IP: "))
            elif choice == "2":
                self.username_search(input("Username: "))
            elif choice == "3":
                sys.exit()
            else:
                print("Invalid choice!")

def main():
    os.system('clear')
    print(Panel.fit(f"FEN-OSINT v{VERSION}"))
    
    tool = FENOSINT()
    if not tool.check_password():
        print("[!] Access denied!")
        return
    
    tool.show_menu()

if __name__ == "__main__":
    main()
