#!/bin/bash
# FEN-OSINT Auto-Installer v5.0

echo -e "\e[1;36mFEN-OSINT Ultimate Installer\e[0m"
echo -e "\e[1;33mDeveloper: FEN\e[0m"

# Проверка Termux
if [ ! -d "/data/data/com.termux/files/usr" ]; then
    echo -e "\e[1;31mОшибка: Этот установщик работает только в Termux!\e[0m"
    exit 1
fi

# Обновление пакетов
echo -e "\e[1;32m[1/5] Обновление пакетов...\e[0m"
pkg update -y && pkg upgrade -y

# Установка зависимостей
echo -e "\e[1;32m[2/5] Установка зависимостей...\e[0m"
pkg install -y python git python-pip

# Установка Python-библиотек
echo -e "\e[1;32m[3/5] Установка Python-пакетов...\e[0m"
pip install requests bs4 rich phonenumbers

# Загрузка программы
echo -e "\e[1;32m[4/5] Загрузка FEN-OSINT...\e[0m"
if [ -d "FEN-OSINT" ]; then
    rm -rf FEN-OSINT
fi
git clone https://github.com/FENRTH/FEN-OSINT.git

# Настройка прав
echo -e "\e[1;32m[5/5] Настройка...\e[0m"
cd FEN-OSINT
chmod +x fenosint.py

echo -e "\e[1;32mУстановка завершена!\e[0m"
echo -e "Запуск: \e[1;36mcd FEN-OSINT && ./fenosint.py\e[0m"
echo -e "Пароль: \e[1;33mFENDARK\e[0m"
