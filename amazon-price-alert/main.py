import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

amazon_url = "https://www.amazon.com.tr/Karaca-K%C3%B6p%C3%BCrt%C3%BCc%C3%BCl%C3%BC-Bas%C4%B1n%C3%A7l%C4%B1-Cappuccino-Americano/dp/B0C4YRMC9Y/ref=sr_1_16?crid=4EPN1VOUU5AI&keywords=kahve+makinesi&qid=1704303671&sprefix=kahve%2Caps%2C322&sr=8-16"
amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

my_email = "python.sumeyye@gmail.com"
my_password = os.environ["MY_PASSWORD"]

response = requests.get(amazon_url, headers=amazon_headers)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "lxml")

price_lines = soup.find_all(name="span", class_="a-price-whole")
price = float(price_lines[0].getText().split(",")[0])
product_name = soup.title.string.split(":")[0]

if price < 4.000:
    message = (f"Subject: Amazon Price Down Alert!\n\n"
               f"Price is under 4.000 TL for {product_name}\n Go to link: {amazon_url}").encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="python.sumeyye@yahoo.com", msg=message)
