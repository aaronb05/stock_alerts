
import config

STOCK = "GHL"
COMPANY_NAME = "Greenhill Inc"


def get_news():
    news = config.get_news(company=COMPANY_NAME)
    top_articles = []
    for article in news["articles"][0:3]:
        print(article)
        title = article['title']
        desc = article['description']
        article_tuple = (title, desc)
        top_articles.append(article_tuple)
    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.

    message = f"{COMPANY_NAME}({STOCK}): {percent_result}\n" \
              f"Headline:{top_articles[0][0]}\n" \
              f"Brief: {top_articles[0][1]}\n\n" \
              f"Headline:{top_articles[1][0]}\n" \
              f"Breif: {top_articles[1][1]}\n\n" \
              f"Headline:{top_articles[2][0]}\n" \
              f"Brief: {top_articles[2][1]}"
    config.send_sms(message)


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
closing_values = config.get_latest_stock_info(STOCK)
day_1 = float(closing_values[1])
day_2 = float(closing_values[0])
percent_result = ((day_2 - day_1) / day_1) * 100
if day_2 <= (day_1 * 0.95) or day_2 >= (day_1 * 1.05):
    get_news()
else:
    print(f"Yesterday closed at {day_1}, the previous day closed at {day_2}. Difference falls between set ranges, "
          f"no news to gather")

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.








