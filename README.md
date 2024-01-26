# Authorization using Telegram Messanger Task

## Prerequisites

- Python 3.12
- Django 5.0.1
- PostgreSQL (15.4)
- Ngrok (for local development and testing)

## Getting Started

### 1. Installation

```bash
# Clone the repository
git clone git@github.com:ummataliyev/auth.git

# Navigate to the project directory
cd auth

# Create a virtual environment (optional but recommended)
python -m venv venv
# or
sudo apt install virtualenv
virtualenv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip3 install -r requirements.txt
```

### Database Setup

```bash
# Connect your database with project (look to .env.dist)
python3 manage.py migrate
```

### Set Environment Variables
```bash
# Check out .env.dist
```

### Ngrok Setup
```bash
# Donwload ngrok if not exsist
https://ngrok.com/download

# Run ngrok to expose your local Django development server
ngrok http 8000
```

### Set Webhook
```bash
curl -F "url=<YOUR_NGROK_URL>/api/v1/bot/webhook/" https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/setWebhook
```

### Run Djano Server
```bash
python3 manage.py runserver
```
