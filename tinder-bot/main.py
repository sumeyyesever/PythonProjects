from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import os

MY_PASSWORD = os.environ["MY_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
time.sleep(2)

# decline cookies
decline_cookies = driver.find_element(By.XPATH, value='//*[@id="u-1919424827"]/div/div[2]/div/div/div[1]/div[2]/button')
decline_cookies.click()
time.sleep(10)

# log in
login_button = driver.find_element(By.XPATH, value='//*[@id="u-1919424827"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(10)

login_facebook = driver.find_element(By.XPATH, value='//*[@id="u647161393"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login_facebook.click()
time.sleep(5)

# switch to facebook login page
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# log in credentials
email = driver.find_element(By.ID, value="email")
email.send_keys("python.sumeyye@gmail.com")
password = driver.find_element(By.ID, value="pass")
password.send_keys(MY_PASSWORD)
submit = driver.find_element(By.NAME, value="login")
submit.click()
time.sleep(10)

# switch to tinder page
driver.switch_to.window(base_window)

# allow locations and decline notifications
allow_loc = driver.find_element(By.XPATH, value='//*[@id="u647161393"]/main/div/div/div/div[3]/button[1]')
allow_loc.click()
time.sleep(10)

notifications = driver.find_element(By.XPATH, value='//*[@id="u647161393"]/main/div/div/div/div[3]/button[2]')
notifications.click()
time.sleep(10)

# like people
for _ in range(15):
    body = driver.find_element(By.TAG_NAME, value="body")
    body.send_keys(Keys.ARROW_RIGHT)
    time.sleep(15)

driver.quit()



