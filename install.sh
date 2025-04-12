#!/bin/bash
# FEN-OSINT Auto-Installer

echo "[*] Installing FEN-OSINT..."
pkg update -y
pkg install -y python git
pip install requests bs4 rich

if [ -d "FEN-OSINT" ]; then
    rm -rf FEN-OSINT
fi

git clone https://github.com/FENRTH/FEN-OSINT.git
cd FEN-OSINT
chmod +x fenosint.py

echo "[+] Installation complete!"
echo "Run: cd FEN-OSINT && ./fenosint.py"
echo "Password: FENDARK"
