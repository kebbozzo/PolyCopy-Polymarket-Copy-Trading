# PolyCopy-Copy-Trading
A bot for automatically copying trades on Polymarket

📋 Description
A Python bot that monitors specified wallets on Polymarket and automatically copies their trading activity. It detects changes in positions (open, close, increase, decrease) and executes the same trades using your own account.

✨ Key Features
📊 Simultaneous monitoring of multiple wallet addresses

⚡ Real-time detection of position changes

🔄 Automatic trade copying with customizable percentage

🛡️ Configurable rate limiting to respect API constraints

📝 Ability to disable live trading (log mode)

🚀 Setup
1. Install dependencies
bash
pip install -r requirements.txt
2. Create a .env file with your credentials
bash
POLYMARKET_PRIVATE_KEY=your_private_key
POLYMARKET_PROXY_ADDRESS=your_proxy_address
3. Configure config.json
json
{
    "wallets_to_track": ["0x..."],
    "copy_percentage": 1.0,
    "rate_limit": 25,
    "trading_enabled": true
}
⚙️ Configuration Parameters
Parameter	Description
wallets_to_track	List of wallet addresses to follow
copy_percentage	Percentage to copy relative to original size (e.g., 1.0 = 100%, 0.2 = 20%, 2.0 = 200%)
rate_limit	Maximum number of API requests allowed per 10-second window (default: 25)
trading_enabled	If false, the bot only logs what it would do without executing trades
▶️ Running
bash
python src/main.py
📌 Important Notes
⚠️ Make sure you have the src.positions and src.trading modules in your project structure.
