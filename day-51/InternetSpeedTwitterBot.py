from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/result/15721773122")
        time.sleep(10)
        go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(90)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        time.sleep(10)
        print(f"Download Mbps: {self.down}")
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Upload Mbps: {self.up}")
        time.sleep(10)

    def tweet_to_provider(self, t_email, t_password, promised_down, promised_up):
        time.sleep(15)
        self.driver.get("https://twitter.com/")
        time.sleep(10)
        sign_in = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()
        time.sleep(10)
        # enter email
        email = self.driver.find_element(By.NAME, value="text")
        email.click()
        email.send_keys(t_email)
        email.send_keys(Keys.TAB+Keys.ENTER)
        time.sleep(10)
        # enter password
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(t_password)
        password.send_keys(Keys.TAB+Keys.TAB+Keys.TAB+Keys.ENTER)
        time.sleep(15)
        # find tweet area write the tweet and send it
        tweet_area = self.driver.find_element(By.CLASS_NAME, value='public-DraftEditor-content')
        time.sleep(2)
        tweet_area.click()
        tweet_area.send_keys(f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when i pay for {promised_down}down/{promised_up}up????")
        tweet_button = self.driver.find_element(By.XPATH, value='//div[@data-testid="tweetButtonInline"]')
        tweet_button.click()
        time.sleep(10)
        self.driver.quit()
