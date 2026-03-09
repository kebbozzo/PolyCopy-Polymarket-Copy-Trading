import os
import time
import subprocess
from datetime import datetime

# Si assicura di lavorare nella cartella corretta
os.chdir(os.path.dirname(os.path.abspath(__file__)))

FILENAME = "README.md"
INTERVAL = 120 

def toggle_invisible_space():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write("# PolyCopy-Polymarket-Copy-Trading\n")

    with open(FILENAME, "r", encoding="utf-8") as f:
        content = f.read()

    # Se finisce con uno spazio lo toglie, altrimenti lo aggiunge.
    # Questo cambia il file per Git ma non cambia nulla visivamente su GitHub.
    if content.endswith(" "):
        new_content = content[:-1]
    else:
        new_content = content + " "

    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(new_content)

def run_git_safe():
    try:
        # 1. Aggiunge il file
        subprocess.run(["git", "add", FILENAME], check=True, capture_output=True)
        
        # 2. Commit con messaggio generico (niente scritte "bot" o "refresh")
        # Usiamo un messaggio fisso così sembra un normale update di documentazione
        commit_msg = "Update documentation"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, capture_output=True)
        
        # 3. Push verso il server
        subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Sincronizzazione completata.")
        
    except subprocess.CalledProcessError as e:
        # Se Git dice che non c'è nulla da cambiare, lo script continua silenzioso
        pass

if __name__ == "__main__":
    print("--- Avvio aggiornamento discreto della repository ---")
    try:
        while True:
            toggle_invisible_space()
            run_git_safe()
            
            # Countdown discreto
            for i in range(INTERVAL, 0, -1):
                print(f"In attesa... {i}s  ", end="\r")
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nScript terminato.")