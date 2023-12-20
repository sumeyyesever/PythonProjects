import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
# [new_value for (key, value) in dictionary.items()]

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
day_dict = stock_data["Time Series (Daily)"]
day_list = [value for (key, value) in day_dict.items()]
yesterday_close = float(day_list[0]["4. close"])
print(yesterday_close)

# TODO 2. - Get the day before yesterday's closing stock price

day_before_close = float(day_list[1]["4. close"])
print(day_before_close)


# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp

pos_dif = abs(yesterday_close - day_before_close)
print(pos_dif)
if yesterday_close > day_before_close:
    inc_dec = "Increase"
else:
    inc_dec = "Decrease"


# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

percentage_dif = (pos_dif / day_before_close) * 100
percentage_dif = round(percentage_dif, 2)
print(percentage_dif)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_dif > 5:
    print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "from": 2023-11-20,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY,
    "language": "en"
}
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
print(news_data)

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
#  Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

articles_list = news_data["articles"]
first_three_news = articles_list[:3]
print(first_three_news)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

last_news = [(news["title"], news["description"], news["url"]) for news in first_three_news]


# TODO 9. - Send each article as a separate message via Twilio.

my_email = "python.sumeyye@gmail.com"
my_password = ""

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    for news in last_news:
        message = (f"Subject:{COMPANY_NAME} News\n\n {STOCK_NAME}: {percentage_dif}% {inc_dec}\n\nTitle: {news[0]}\n "
                   f"Brief: {news[1]}\nLink: {news[2]}")
        message = message.encode("ascii", "ignore").decode("ascii")
        connection.sendmail(from_addr=my_email, to_addrs="python.sumeyye@yahoo.com", msg=message)
