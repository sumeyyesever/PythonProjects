import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self, i_username, i_password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username = self.driver.find_element(By.NAME, value="username")
        username.send_keys(i_username)
        time.sleep(1)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(i_password)
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, value='//button[@type="submit"]')
        login_button.click()
        time.sleep(20)
        remember_not = self.driver.find_element(By.CLASS_NAME, value="_ac8f")
        remember_not.click()
        time.sleep(10)
        notification = self.driver.find_element(By.CLASS_NAME, value="_a9_1")
        notification.click()
        time.sleep(10)

    def find_followers(self, account):
        self.driver.get(f"https://www.instagram.com/{account}/")
        time.sleep(15)
        followers = self.driver.find_element(By.XPATH, value=f'//a[@href="/{account}/followers/"]')
        followers.click()
        time.sleep(10)

    def follow(self):
        follow_them_all = self.driver.find_elements(By.CSS_SELECTOR, value=".x1dm5mii button")
        print(follow_them_all)
        time.sleep(15)
        for follow in follow_them_all:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", follow)
                follow.click()
                time.sleep(5)
            except selenium.common.exceptions.ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CLASS_NAME, value="_a9_1")
                cancel_button.click()
                time.sleep(5)
                follow.click()
                time.sleep(5)
        self.driver.quit()

