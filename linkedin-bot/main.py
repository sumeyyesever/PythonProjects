from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

MY_PASSWORD = os.environ["MY_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3788106621&distance=25&f_AL=true&geoId=102299470&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")

time.sleep(1)

# sign in
signin_button = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
signin_button.click()
time.sleep(1)

# enter credentials
username = driver.find_element(By.ID, value="username")
username.send_keys("python.sumeyye@gmail.com")
password = driver.find_element(By.ID, value="password")
password.send_keys(MY_PASSWORD)
submit_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
submit_button.click()
time.sleep(5)

# save jobs
jobs = driver.find_elements(By.CLASS_NAME, value="jobs-search-results__list-item")
for job in jobs:
    job.click()
    time.sleep(10)
    jobs_save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "jobs-save-button")))
    jobs_save_button.click()
    time.sleep(10)

driver.quit()
