# 🇺🇸 English 

# PolyCopy-Polymarket Copy-Trading

A bot for automatically copying trades on Polymarket

---

## 📋 Description

A Python bot that monitors specified wallets on Polymarket and automatically copies their trading activity. It detects changes in positions (open, close, increase, decrease) and executes the same trades using your own account.

---

## ✨ Key Features

* 📊 **Simultaneous monitoring** of multiple wallet addresses
* ⚡ **Real-time detection** of position changes
* 🔄 **Automatic trade copying** with customizable percentage
* 🛡️ **Configurable rate limiting** to respect API constraints
* 📝 **Log mode** - disable live trading and only log what the bot would do

---

## 🚀 Setup

Open a terminal inside the PolyCopy-Copy-Trading folder:

### 1. Install Dependencies

```bash
pip install -r requirements.txt

```

If you signed up with email/Magic Link on Polymarket, visit reveal.magic.link/polymarket to export your private key .

For standard wallets (MetaMask), use your wallet's private key .

The proxy address is the wallet address that holds your funds on Polymarket (your funder address) .

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
| --- | --- |
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

# 🇨🇳 中文 (Chinese Simplified)

# PolyCopy-Polymarket 跟单交易机器人

一个用于自动复制 Polymarket 交易的机器人

---

## 📋 项目描述

这是一个 Python 机器人，用于监控 Polymarket 上的指定钱包并自动复制其交易活动。它可以检测仓位变化（开仓、平仓、加仓、减仓），并使用您自己的账户执行相同的交易。

---

## ✨ 核心功能

* 📊 **多钱包同步监控**
* ⚡ **实时检测** 仓位变化
* 🔄 **自动跟单**，支持自定义跟单比例
* 🛡️ **可配置速率限制**，遵守 API 限制
* 📝 **日志模式** - 禁用实盘交易，仅记录机器人的预期操作

---

## 🚀 安装设置

在 PolyCopy-Copy-Trading 文件夹内打开终端：

### 1. 安装依赖

```bash
pip install -r requirements.txt

```

如果您在 Polymarket 上使用电子邮件/Magic Link 注册，请访问 reveal.magic.link/polymarket 导出您的私钥。

对于标准钱包（如 MetaMask），请直接使用您的钱包私钥。

代理地址（Proxy Address）是在 Polymarket 上持有您资金的钱包地址（您的资金地址）。

### 2. 创建包含凭据的 `.env` 文件

```bash
POLYMARKET_PRIVATE_KEY=您的私钥
POLYMARKET_PROXY_ADDRESS=您的代理地址

```

### 3. 配置 `config.json`

```json
{
    "wallets_to_track": ["0x..."],
    "copy_percentage": 1.0,
    "rate_limit": 25,
    "trading_enabled": true
}

```

---

## ⚙️ 配置参数

| 参数 | 描述 |
| --- | --- |
| `wallets_to_track` | 要追踪的钱包地址列表 |
| `copy_percentage` | 相对于原始交易规模的跟单比例（例如：1.0 = 100%, 0.2 = 20%, 2.0 = 200%） |
| `rate_limit` | 每 10 秒允许的最大 API 请求数（默认：25） |
| `trading_enabled` | 如果为 false，机器人仅记录日志而不执行交易 |

---

## ▶️ 运行机器人

```bash
python src/main.py

```

---

## 📁 项目结构

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

## 📌 重要提示

⚠️ **请确保您的项目结构中包含 `src.positions` 和 `src.trading` 模块。**

⚠️ **此机器人涉及真实交易账户。请负责任地使用，并先在日志模式下进行测试。**

---

## 📝 许可证

本项目按“原样”提供。使用风险自担。

---

# 🇪🇸 Español

# PolyCopy-Polymarket Copy-Trading

Un bot para copiar automáticamente operaciones en Polymarket

---

## 📋 Descripción

Un bot de Python que monitorea billeteras específicas en Polymarket y copia automáticamente su actividad de trading. Detecta cambios en las posiciones (abrir, cerrar, aumentar, disminuir) y ejecuta las mismas operaciones utilizando tu propia cuenta.

---

## ✨ Características Principales

* 📊 **Monitoreo simultáneo** de múltiples direcciones de billetera
* ⚡ **Detección en tiempo real** de cambios de posición
* 🔄 **Copia automática de trades** con porcentaje personalizable
* 🛡️ **Límite de tasa configurable** para respetar las restricciones de la API
* 📝 **Modo de registro** - desactiva el trading real y solo registra lo que haría el bot

---

## 🚀 Configuración

Abre una terminal dentro de la carpeta PolyCopy-Copy-Trading:

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt

```

Si te registraste con email/Magic Link en Polymarket, visita reveal.magic.link/polymarket para exportar tu clave privada .

Para billeteras estándar (MetaMask), usa la clave privada de tu billetera .

La dirección proxy es la dirección de la billetera que contiene tus fondos en Polymarket (tu dirección de fondeo) .

### 2. Crea un Archivo `.env` con tus Credenciales

```bash
POLYMARKET_PRIVATE_KEY=tu_clave_privada
POLYMARKET_PROXY_ADDRESS=tu_direccion_proxy

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

---

## ⚙️ Parámetros de Configuración

| Parametro | Descripción |
| --- | --- |
| `wallets_to_track` | Lista de direcciones de billetera a seguir |
| `copy_percentage` | Porcentaje a copiar en relación al tamaño original (ej., 1.0 = 100%, 0.2 = 20%, 2.0 = 200%) |
| `rate_limit` | Número máximo de solicitudes API permitidas por ventana de 10 segundos (por defecto: 25) |
| `trading_enabled` | Si es falso, el bot solo registra las acciones sin ejecutar operaciones |

---

## ▶️ Ejecución del Bot

```bash
python src/main.py

```

---

## 📁 Estruttura del Proyecto

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

## 📌 Notas Importantes

⚠️ **Asegúrate de tener los módulos `src.positions` y `src.trading` en la estructura de tu proyecto.**

⚠️ **Este bot interactúa con cuentas de trading reales. Úsalo con responsabilidad y pruébalo primero en modo de registro.**

---

## 📝 Licencia

Este proyecto se proporciona tal cual. Úsalo bajo tu propio riesgo.

---

# 🇧🇷 Português

# PolyCopy-Polymarket Copy-Trading

Um bot para copiar automaticamente negociações no Polymarket

---

## 📋 Descrição

Um bot em Python que monitora carteiras específicas no Polymarket e copia automaticamente sua atividade de negociação. Ele detecta mudanças em posições (abrir, fechar, aumentar, diminuir) e executa as mesmas negociações usando sua própria conta.

---

## ✨ Principais Funcionalidades

* 📊 **Monitoramento simultâneo** de vários endereços de carteira
* ⚡ **Detecção em tempo real** de mudanças de posição
* 🔄 **Cópia automática de trades** com porcentagem personalizável
* 🛡️ **Limite de taxa configurável** para respeitar as restrições da API
* 📝 **Modo de log** - desativa o trading real e apenas registra o que o bot faria

---

## 🚀 Configuração

Abra um terminal dentro da pasta PolyCopy-Copy-Trading:

### 1. Instalar Dependências

```bash
pip install -r requirements.txt

```

Se você se inscreveu com e-mail/Magic Link no Polymarket, visite reveal.magic.link/polymarket para exportar sua chave privada .

Para carteiras padrão (MetaMask), use a chave privada da sua carteira .

O endereço proxy é o endereço da carteira que contém seus fundos no Polymarket (seu endereço de financiamento) .

### 2. Crie um Arquivo `.env` com suas Credenciais

```bash
POLYMARKET_PRIVATE_KEY=sua_chave_privada
POLYMARKET_PROXY_ADDRESS=seu_endereco_proxy

```

### 3. Configure o `config.json`

```json
{
    "wallets_to_track": ["0x..."],
    "copy_percentage": 1.0,
    "rate_limit": 25,
    "trading_enabled": true
}

```

---

## ⚙️ Parâmetros de Configuração

| Parâmetro | Descrição |
| --- | --- |
| `wallets_to_track` | Lista de endereços de carteira para seguir |
| `copy_percentage` | Porcentagem a copiar em relação ao tamanho original (ex: 1.0 = 100%, 0.2 = 20%, 2.0 = 200%) |
| `rate_limit` | Número máximo de solicitações de API permitidas por janela de 10 segundos (padrão: 25) |
| `trading_enabled` | Se falso, o bot apenas registra as ações sem executar negociações |

---

## ▶️ Executando o Bot

```bash
python src/main.py

```

---

## 📁 Estrutura do Projeto

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

## 📌 Notas Importantes

⚠️ **Certifique-se de ter os módulos `src.positions` e `src.trading` na estrutura do seu projeto.**

⚠️ **Este bot interage com contas de negociação reais. Use com responsabilidade e teste primeiro no modo de log.**

---

## 📝 Licença

Este projeto é fornecido como está. Use por sua conta e risco.

---

```

```
# 🇮🇹 Italiano

# PolyCopy-Polymarket Copy-Trading
Un bot per copiare automaticamente le operazioni su Polymarket


---

## 📋 Descrizione
Un bot Python che monitora wallet specifici su Polymarket e copia automaticamente la loro attività di trading. Rileva cambiamenti nelle posizioni (apertura, chiusura, aumento, diminuzione) ed esegue le stesse operazioni utilizzando il tuo account.

---

## ✨ Funzionalità Chiave
- 📊 **Monitoraggio simultaneo** di più indirizzi wallet
- ⚡ **Rilevamento in tempo reale** dei cambiamenti di posizione
- 🔄 **Copia automatica dei trade** con percentuale personalizzabile
- 🛡️ **Configurabile rate limiting** per rispettare i vincoli API
- 📝 **Log mode** - disabilita il trading live e registra solo ciò che il bot farebbe

---

## 🚀 Setup

Apri un terminale all'interno della cartella PolyCopy-Copy-Trading:

### 1. Installa le Dipendenze
```bash
pip install -r requirements.txt

```

Se ti sei iscritto con email/Magic Link su Polymarket, visita reveal.magic.link/polymarket per esportare la tua chiave privata .

Per i wallet standard (MetaMask), usa la chiave privata del tuo wallet .

L'indirizzo proxy è l'indirizzo del wallet che detiene i tuoi fondi su Polymarket (il tuo indirizzo funder) .

### 2. Crea un File `.env` con le tue Credenziali

```bash
POLYMARKET_PRIVATE_KEY=tua_chiave_privata
POLYMARKET_PROXY_ADDRESS=tuo_indirizzo_proxy

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

---

## ⚙️ Parametri di Configurazione

| Parametro | Descrizione |
| --- | --- |
| `wallets_to_track` | Elenco degli indirizzi wallet da seguire |
| `copy_percentage` | Percentuale da copiare rispetto alla dimensione originale (es., 1.0 = 100%, 0.2 = 20%, 2.0 = 200%) |
| `rate_limit` | Numero massimo di richieste API consentite per finestra di 10 secondi (default: 25) |
| `trading_enabled` | Se falso, il bot registra solo quello che farebbe senza eseguire trade |

---

## ▶️ Avvio del Bot

```bash
python src/main.py

```

---

## 📁 Struttura del Progetto

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

## 📌 Note Importanti

⚠️ **Assicurati di avere i moduli `src.positions` e `src.trading` nella struttura del tuo progetto.**

⚠️ **Questo bot interagisce con account di trading reali. Usa responsabilmente e testa prima in log mode.**

---

## 📝 Licenza

Questo progetto è fornito così com'è. Usa a tuo rischio.
 