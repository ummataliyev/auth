# Authorization using Telegram Messenger

## Prerequisites

- Python 3.12
- Django 5.0.1
- PostgreSQL 15.4
- Ngrok (for local development and testing)

## Getting Started

### 1. Installation

```bash
# Clone the repository
git clone git@github.com:ummataliyev/auth.git

# Navigate to the project directory
cd auth

# Create a virtual environment (recommended)
python -m venv venv  # On Windows: python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt


### Database Setup
# Connect your database with project (PostgreSQL is recommended)
python3 manage.py migrate


### Set Environment Variables
# Check out .env.dist for required environment variables
# Django SECRET_KEY


### Ngrok Setup
# Download ngrok if not exist
https://ngrok.com/download

# Run ngrok to expose your local Django development server
ngrok http 8000


### Set Webhook
# Replace <YOUR_NGROK_URL> and <YOUR_TELEGRAM_BOT_TOKEN> with actual values
curl -F "url=<YOUR_NGROK_URL>/api/v1/bot/webhook/" https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/setWebhook


### Run Djano Server
python3 manage.py runserver
# The Django development server will run at http://127.0.0.1:8000/
