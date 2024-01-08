import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

list_items = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

item_links = []
item_prices = []
item_addresses = []
for item in list_items:
    item_link = item.find("a")["href"]
    item_links.append(item_link)
    item_price = item.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
    item_prices.append(item_price.getText().split("+")[0].split("/")[0])
    item_address = item.find("address")
    item_addresses.append(item_address.getText().strip().replace("|", ""))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(list_items)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSexsnRpyviiIyJsgPpY-l_Ym3zRQXutBuxQVDoVHKfMNj4Q6A/viewform?usp=sf_link")
    first_answer = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first_answer.click()
    first_answer.send_keys(item_addresses[i])
    time.sleep(5)
    second_answer = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_answer.click()
    second_answer.send_keys(item_prices[i])
    time.sleep(5)
    third_answer = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_answer.click()
    third_answer.send_keys(item_links[i])
    time.sleep(5)
    send_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_button.click()
    time.sleep(10)