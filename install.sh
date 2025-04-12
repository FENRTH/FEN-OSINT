#!/bin/bash
# FEN-OSINT Auto-Installer v8.0

# Цвета
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m'

echo -e "${BLUE}"
cat << "EOF"
  _____ ______ _   _ _______ 
 |  ___|___  /| \ | |__   __|
 | |__    / / |  \| |  | |   
 |  __|  / /  | . ` |  | |   
 | |___./ /___| |\  |  | |   
 |_____/_____|_| \_|  |_|   
EOF
echo -e "${NC}"

# Проверка Termux
if [ ! -d "/data/data/com.termux/files/usr" ]; then
    echo -e "${RED}Ошибка: Этот скрипт работает только в Termux!${NC}"
    exit 1
fi

echo -e "${YELLOW}[1/3] Обновление пакетов...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${YELLOW}[2/3] Установка зависимостей...${NC}"
pkg install -y python git
pip install requests rich

echo -e "${YELLOW}[3/3] Загрузка программы...${NC}"
if [ -d "FEN-OSINT" ]; then
    rm -rf FEN-OSINT
fi
git clone https://github.com/FENRTH/FEN-OSINT.git

# Автозапуск
echo -e "${GREEN}"
cat << "EOF"
 ___ _   _  ___ ___ ___  ___ ___ 
/ __| | | |/ __/ _ \ _ \/ __/ __|
\__ \ |_| | (_|  __/   /\__ \__ \
|___/\__,_|\___\___|_|_\|___/___/
EOF
echo -e "${NC}"

cd FEN-OSINT
chmod +x fenosint.py

# Добавляем автозапуск в .bashrc
if ! grep -q "fenosint.py" ~/.bashrc; then
    echo "cd ~/FEN-OSINT && python fenosint.py" >> ~/.bashrc
fi

echo -e "${GREEN}Установка завершена! Перезапустите Termux.${NC}"
echo -e "Код доступа: ${YELLOW}FENDARK${NC}"
