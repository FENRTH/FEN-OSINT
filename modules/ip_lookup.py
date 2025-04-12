import requests
from rich.console import Console
from rich.table import Table

console = Console()

def ip_search(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        table = Table(title="Информация об IP")
        table.add_column("Параметр", style="cyan")
        table.add_column("Значение", style="green")
        
        fields = {
            'IP': 'query',
            'Страна': 'country',
            'Город': 'city',
            'Провайдер': 'isp',
            'Широта': 'lat',
            'Долгота': 'lon'
        }
        
        for desc, field in fields.items():
            table.add_row(desc, str(data.get(field, 'N/A')))
        
        console.print(table)
    except Exception as e:
        print(f"Ошибка: {e}")
