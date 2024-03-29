
# Stock News Notifier

This Python script fetches stock data using the Alpha Vantage API and news articles using the News API. It then sends the articles via SMS using the Twilio API.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Required Python libraries: `requests`, `twilio`, `python-dotenv`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/dheerajark/stock-news-alert.git
   ```

2. Create a `.env` file in the root directory with the following environment variables:
   ```dotenv
   ACCOUNT_SID=your_twilio_account_sid
   AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PH_NO=your_twilio_phone_number
   YOUR_NUMBER=your_phone_number
   STOCK_END_POINT_APIKEY_ALPHAVANTAGE=your_alpha_vantage_api_key
   NEWS_APIKEY=your_news_api_key
   ```

## Usage

Run the script:
   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
