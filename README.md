# PolyCopy-Copy-Trading

Un bot per copiare automaticamente operazioni su Polymarket

## 📋 Descrizione

Un bot Python che monitora wallet specificati su Polymarket e copia automaticamente le loro attività di trading. Rileva variazioni nelle posizioni (apertura, chiusura, incremento, decremento) ed esegue le stesse operazioni utilizzando il tuo account.

## ✨ Caratteristiche principali

- 📊 Monitoraggio simultaneo di più indirizzi wallet
- ⚡ Rilevamento in tempo reale di cambiamenti nelle posizioni
- 🔄 Copia automatica delle operazioni con percentuale personalizzabile
- 🛡️ Limite di richieste configurabile per rispettare le API
- 📝 Possibilità di disattivare il trading reale (modalità log)

## 🚀 Setup

### 1. Installa le dipendenze

```bash
pip install -r requirements.txt
```

### 2. Crea un file `.env` con le tue credenziali

```bash
POLYMARKET_PRIVATE_KEY=your_private_key
POLYMARKET_PROXY_ADDRESS=your_proxy_address
```

### 3. Configura `config.json`

```json
{
    "wallets_to_track": ["0x..."],
    "copy_percentage": 1.0,
    "rate_limit": 25,
    "trading_enabled": true
}
```

## ⚙️ Parametri di configurazione

| Parametro | Descrizione |
|-----------|-------------|
| `wallets_to_track` | Lista degli indirizzi wallet da seguire |
| `copy_percentage` | Percentuale di copia rispetto alla dimensione originale (es. 1.0 = 100%, 0.2 = 20%, 2.0 = 200%) |
| `rate_limit` | Numero massimo di richieste API consentite in una finestra di 10 secondi (default: 25) |
| `trading_enabled` | Se `false`, il bot si limita a registrare le operazioni senza eseguirle |

## ▶️ Esecuzione

```bash
python src/main.py
```

## 📌 Note importanti

> ⚠️ Assicurati di avere i moduli `src.positions` e `src.trading` nella struttura del progetto.