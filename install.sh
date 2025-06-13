#!/bin/bash

# Оформление
echo ""
echo -e "\033[1;36m╔══════════════════════════════════════════╗"
echo -e "║          Установка Telegram Bot          ║"
echo -e "╚══════════════════════════════════════════╝\033[0m"
echo ""

# Обновление пакетов
echo -e "\033[1;33m[1/4] 🔄 Обновление пакетов...\033[0m"
pkg update -y
pkg upgrade -y
echo ""

# Установка зависимостей
echo -e "\033[1;33m[2/4] 📦 Установка Python и Git...\033[0m"
pkg install python git -y
echo ""

# Установка Python библиотек
echo -e "\033[1;33m[3/4] ⚙️ Установка библиотек Python...\033[0m"
pip install --upgrade pyrogram tgcrypto
echo ""

# Запуск бота
echo -e "\033[1;33m[4/4] 🚀 Запуск бота...\033[0m"
echo -e "\033[1;32m✔ Установка завершена успешно!\033[0m"
echo ""
python main.py
