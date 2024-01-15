import requests
import datetime as dt
from twilio.rest import Client
import dotenv
import os

dotenv.load_dotenv()

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
twilio_phone_number = os.environ.get("TWILIO_PH_NO")
my_number = os.environ.get("YOUR_NUMBER")           # Recipient number


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = " https://newsapi.org/v2/everything"

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("STOCK_END_POINT_APIKEY_ALPHAVANTAGE")
}

parameter2 = {
    "q": COMPANY_NAME,
    "language": "en",
    "from": "",
    "to": "",
    "shortBy": "popularity",
    "apiKey": os.environ.get("NEWS_APIKEY")
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=STOCK_ENDPOINT, params=parameter)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
print(data_list)
yesterday = data_list[0]
yesterday_closing_price = float(yesterday["4. close"])
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday["4. close"])
difference = (yesterday_closing_price - day_before_yesterday_closing_price)
positive_difference = abs(difference)
inc_dec_percent = (difference/day_before_yesterday_closing_price) * 100
if inc_dec_percent >= 5 or inc_dec_percent <= -3:
    print("Get NEWs")
    print(inc_dec_percent)
    print(positive_difference)

#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

    response = requests.get(url=NEWS_ENDPOINT, params=parameter2)
    response.raise_for_status()
    data_2 = response.json()
    first_three_data = data_2["articles"][:3]
for article in first_three_data:
    headline = article["title"]
    content = article["description"]
    print(content)
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

    title = STOCK
    formatted_articles = [f"{STOCK}: {inc_dec_percent}%\n\nHeadline: {articles['title']}\n\nBrief: {articles['description']}"for articles in first_three_data]
    print(formatted_articles)
    client = Client(account_sid, auth_token)
    for articles in formatted_articles:
        message = client.messages.create(
            body=formatted_articles,
            from_=twilio_phone_number,
            to=my_number,
        )

        print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

