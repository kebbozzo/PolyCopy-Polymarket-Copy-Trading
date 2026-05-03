import os
import time
import subprocess
from datetime import datetime

# --- CONFIGURAZIONE ---
FILENAME = "README.md"
INTERVAL = 120 
USERNAME = "kebbozzo"
REPO_NAME = "PolyCopy-Polymarket-Copy-Trading"

# Forza la directory di lavoro sulla cartella dello script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_token():
    """Estrae il token dal file .env pulendo ogni spazio"""
    if os.path.exists(".env"):
        try:
            with open(".env", "r", encoding="utf-8") as f:
                for line in f:
                    if "GITHUB_TOKEN=" in line:
                        return line.split("=", 1)[1].strip()
        except Exception as e:
            print(f"Errore lettura .env: {e}")
    return None

def toggle_invisible_space():
    """Modifica il README in modo invisibile"""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write(f"# {REPO_NAME}\n")
    with open(FILENAME, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content[:-1] if content.endswith(" ") else content + " "
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(new_content)

def run_sync():
    token = get_token()
    if not token:
        print("ERRORE: Token non trovato nel file .env")
        return

    # FORMATO RICHIESTO: https://username:token@github.com/username/reponame.git
    # Questa stringa è l'unica che garantisce l'accesso senza prompt di password
    auth_url = f"https://{USERNAME}:{token}@github.com/{USERNAME}/{REPO_NAME}.git"
    
    try:
        # 1. Aggiorna l'URL remoto con le credenziali integrate
        subprocess.run(["git", "remote", "set-url", "origin", auth_url], check=True, capture_output=True)
        
        # 2. Stage del file modificato
        subprocess.run(["git", "add", FILENAME], check=True, capture_output=True)
        
        # 3. Commit con orario
        commit_msg = f"Update: {datetime.now().strftime('%H:%M')}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, capture_output=True)
        
        # 4. Push forzando l'assenza di prompt interattivi
        env = os.environ.copy()
        env["GIT_TERMINAL_PROMPT"] = "0"
        
        subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True, env=env)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Sincronizzazione riuscita!")
        
    except subprocess.CalledProcessError as e:
        err_msg = e.stderr.decode(errors='ignore') if e.stderr else "Errore generico"
        if "nothing to commit" in err_msg:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Nessuna modifica rilevata.")
        else:
            print(f"Errore Git: {err_msg.strip()}")

if __name__ == "__main__":
    print(f"--- AUTO-UPDATER AVVIATO ---")
    print(f"Repo: {USERNAME}/{REPO_NAME}")
    
    # Rimuove helper di sistema per evitare conflitti con vecchie password di Windows
    subprocess.run(["git", "config", "--local", "credential.helper", ""], capture_output=True)

    try:
        while True:
            toggle_invisible_space()
            run_sync()
            
            # Timer visivo nel terminale
            for i in range(INTERVAL, 0, -1):
                print(f"Prossimo aggiornamento tra {i}s...   ", end="\r")
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nScript arrestato correttamente.")