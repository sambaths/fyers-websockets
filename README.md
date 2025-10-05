# 📊 Fyers DOM Analyzer

> **Professional-grade Depth of Market analysis platform for multiple instruments, powered by Fyers TBT Data Feed**

A real-time 50-level DOM analyzer with secure Fyers OAuth integration, advanced order flow analytics, and a multi-tab interface to track several instruments concurrently.

![Fyers DOM Analyzer](https://img.shields.io/badge/Fyers-DOM%20Analyzer-blue?style=for-the-badge&logo=trading&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-WebSocket-red?style=for-the-badge&logo=flask&logoColor=white)
![TBT Feed](https://img.shields.io/badge/TBT-Feed-orange?style=for-the-badge&logo=data&logoColor=white)
![License](https://img.shields.io/badge/License-AGPL%20v3-blue?style=for-the-badge)

## ✨ Key Features

###  multi-instrument-config-ui
- **Multi-Instrument Tracking**: Monitor multiple instruments simultaneously, each in its own dedicated tab.
- **YAML Configuration**: Easily configure instruments in a clean, human-readable YAML file.
- **Dynamic UI**: The user interface dynamically creates tabs for each enabled instrument.
- **Seamless Data Routing**: Real-time data is efficiently routed to the correct instrument tab.
- **Backward Compatibility**: Fallback to `.env` configuration if `instruments.yaml` is not found.
- **Migration Script**: A simple script to migrate from the old `.env` configuration to the new YAML format.

### 🔐 **Secure Authentication**
- **Direct Fyers OAuth 2.0** integration with official API
- **Encrypted database storage** for auth tokens and API credentials
- **Automatic session management** with secure token handling

### 📈 **Advanced Market Analysis**
- **50-level DOM visualization** with real-time TBT updates
- **Order flow analytics** with bid-ask ratio analysis
- **Market sentiment indicators** and price level metrics
- **OrderBook Imbalance Analysis** at 10, 20, and 50 depth levels
- **Lot Size Display Toggle** for switching between shares and lots view

## 🚀 Quick Start

### 1. **Clone & Setup**
```bash
git clone https://github.com/sambaths/fyers-websockets.git
cd fyers-websockets
pip install -r requirements.txt
```

### 2. **Configure Environment**
Copy `.env.example` to `.env` and add your Fyers API credentials from [myapi.fyers.in](https://myapi.fyers.in/):

```env
# Fyers API Configuration (Get from https://myapi.fyers.in/)
BROKER_API_KEY=your_fyers_app_id
BROKER_API_SECRET=your_fyers_secret_key
REDIRECT_URL=http://127.0.0.1:5000/fyers/callback

# WebSocket Configuration
WEBSOCKET_URL=wss://rtsocket-api.fyers.in/versova

# Database and Security
DATABASE_URL=sqlite:///fyers_depth.db
SECRET_KEY=your_flask_secret_key_change_in_production
API_KEY_PEPPER=your_secure_pepper_key_change_in_production
```

### 3. **Configure Instruments**
Create a `config/instruments.yaml` file by copying the example:
```bash
mkdir -p config
cp config/instruments.yaml.example config/instruments.yaml
```
Now, edit `config/instruments.yaml` to add the instruments you want to track. Here is an example:
```yaml
instruments:
  - symbol: "NSE:NIFTY25OCTFUT"
    display_name: "NIFTY OCT FUT"
    lot_size: 75
    enabled: true
  - symbol: "NSE:BANKNIFTY25OCTFUT"
    display_name: "BANKNIFTY OCT FUT"
    lot_size: 35
    enabled: true
  - symbol: "BSE:SENSEX25OCTFUT"
    display_name: "SENSEX OCT FUT"
    lot_size: 20
    enabled: false
```

#### Migrating from `.env`
If you were using a previous version of this application, you can automatically generate the `config/instruments.yaml` file from your `.env` file by running the migration script:
```bash
python scripts/migrate_env_to_config.py
```

### 4. **Launch Application**
```bash
python app.py
```

Visit `http://127.0.0.1:5000` and you will be redirected to the Fyers login page. After authentication, you will see the dashboard with a tab for each enabled instrument.

## 📡 API Endpoints

### **Authentication Routes**
```
GET  /                    → Dashboard redirect
GET  /auth/broker         → Fyers OAuth login page
GET  /fyers/callback      → OAuth callback handler
GET  /dashboard           → Main DOM dashboard
GET  /auth/logout         → Logout and token revocation
```

### **API Routes**
```
GET  /api/config          → Application configuration
GET  /api/instruments     → Get the list of enabled instruments
```

### **WebSocket Events**
```
connect                   → Client connection established
market_depth             → Real-time DOM data updates for all subscribed instruments
```

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0) - see the [LICENSE](LICENSE) file for details.