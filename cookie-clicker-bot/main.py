from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def open_stores():
    all_stores = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    all_stores_list = [store.text.split("\n")[0] for store in all_stores]
    grayed_stores = driver.find_elements(By.CLASS_NAME, value="grayed")
    grayed_stores_list = [store.text.split("\n")[0] for store in grayed_stores]
    open_stores_list = list(set(all_stores_list).difference(grayed_stores_list))
    return open_stores_list


def purchase_most_expensive():
    open_stores_list = open_stores()
    open_stores_money = [store.split("-")[1] for store in open_stores_list]
    open_stores_name = [store.split("-")[0] for store in open_stores_list]
    my_money = int(driver.find_element(By.ID, value="money").text)
    print(open_stores_money)
    for store_money in open_stores_money[::-1]:
        if my_money >= int(store_money):
            store_index = open_stores_money.index(store_money)
            store_name = open_stores_name[store_index].strip()
            purchase_store = driver.find_element(By.ID, value=f"buy{store_name}")
            purchase_store.click()


flag = True
finish_timeout = time.time()
while flag:
    control_time = 5
    control_timeout_start = time.time()

    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()

    if time.time() == control_timeout_start + control_time:
        purchase_most_expensive()
    if time.time() >= finish_timeout + 30:
        flag = False

print(driver.find_element(By.ID, value="money").text)
driver.quit()
