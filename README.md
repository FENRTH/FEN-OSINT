#как запускать на Termux 
pkg update && pkg upgrade -y
pkg install python git -y
pip install requests bs4
git clone https://github.com/FENRTH/FEN-OSINT.git
cd FEN-OSINT
chmod +x fen_osint.py
python fen_osint.py 

