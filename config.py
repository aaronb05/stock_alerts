from dotenv import load_dotenv
import os
import requests
from newsapi import NewsApiClient
from twilio.rest import Client

load_dotenv()
NEWS_KEY = os.getenv("NEWS_KEY")
STOCK_KEY = os.getenv("STOCK_KEY")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")


def get_news(company):
    company = company
    news = NewsApiClient(api_key=NEWS_KEY)
    everything = news.get_everything(q=company, language="en", sort_by="relevancy")
    return everything


def get_latest_stock_info(stock):
    endpoint = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "interval": "5min",
        "apikey": STOCK_KEY
    }
    response = requests.get(url=endpoint, params=parameters)
    response.raise_for_status()
    stock_info = response.json()["Time Series (Daily)"]
    stock_data = [value for (key, value) in stock_info.items()]
    yesterday_closing = stock_data[0]["4. close"]
    previous_closing = stock_data[1]["4. close"]
    return yesterday_closing, previous_closing

    # stock_data = stock_info["Time Series (Daily)"]
    # compare_values = []
    # for record in stock_data:
    #     record_date = date.fromisoformat(record)
    #     days = datetime.date
    #     if record_date > current_date - timedelta(days=3):
    #         daily_data = stock_info["Time Series (Daily)"][record]
    #         closing_price = float(daily_data['4. close'])
    #         compare_values.append(closing_price)
    # return compare_values


def send_sms(body):
    client = Client(os.environ.get("TWILIO_ID"), os.environ.get("TWILIO_TOKEN"))
    message = client.messages.create(
        body=body,
        from_="+1 830 532 8450",
        to="+1 336 688 4616"
    )
    print(message.sid)

