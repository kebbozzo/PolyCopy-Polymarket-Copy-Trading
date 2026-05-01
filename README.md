# PolyCopy-Copy-Trading
A bot for automatically copying trades on Polymarket


---

## 📋 Description
A Python bot that monitors specified wallets on Polymarket and automatically copies their trading activity. It detects changes in positions (open, close, increase, decrease) and executes the same trades using your own account.

---

## ✨ Key Features
- 📊 **Simultaneous monitoring** of multiple wallet addresses
- ⚡ **Real-time detection** of position changes
- 🔄 **Automatic trade copying** with customizable percentage
- 🛡️ **Configurable rate limiting** to respect API constraints
- 📝 **Log mode** - disable live trading and only log what the bot would do

---

## 🚀 Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create a `.env` File with Your Credentials
```bash
POLYMARKET_PRIVATE_KEY=your_private_key
POLYMARKET_PROXY_ADDRESS=your_proxy_address
```

### 3. Configure `config.json`
```json
{
    "wallets_to_track": ["0x..."],
    "copy_percentage": 1.0,
    "rate_limit": 25,
    "trading_enabled": true
}
```

---

## ⚙️ Configuration Parameters

| Parameter | Description |
|-----------|------------|
| `wallets_to_track` | List of wallet addresses to follow |
| `copy_percentage` | Percentage to copy relative to original size (e.g., 1.0 = 100%, 0.2 = 20%, 2.0 = 200%) |
| `rate_limit` | Maximum number of API requests allowed per 10-second window (default: 25) |
| `trading_enabled` | If false, the bot only logs what it would do without executing trades |

---

## ▶️ Running the Bot
```bash
python src/main.py
```

---

## 📁 Project Structure
```
PolyCopy-Copy-Trading/
├── src/
│   ├── main.py
│   ├── positions.py
│   ├── trading.py
│   └── utils/
├── config.json
├── requirements.txt
└── README.md
```

---

## 📌 Important Notes
⚠️ **Make sure you have the `src.positions` and `src.trading` modules in your project structure.**

⚠️ **This bot interacts with real trading accounts. Use responsibly and test in log mode first.**

---

## 📝 License
This project is provided as-is. Use at your own risk.

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or open issues.
 