from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import time, sleep

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID, "cookie")
buy_grandma=driver.find_element(By.ID, "buyGrandma")

duration=time()+120
interval=time()+2



item_ids=[]
all_prices=[]


store=driver.find_elements(By.CSS_SELECTOR, "#store div")

store_items=driver.find_elements(By.CSS_SELECTOR, "#store b")

for i in range(len(store)):
    item_ids.append(store[i].get_attribute("id"))

for i in range(len(store_items)):
    price_text=store_items[i].text
    if price_text is not "":
        price=int(price_text.split("- ")[1].replace(",", ""))
    all_prices.append(price)

all_upgrades=[{'id': item_ids[i], 'price':all_prices[i]} for i in range(len(store)-1)]



while time()< duration:
    cookie.click()
    cookies_per_second=driver.find_element(By.ID, "cps")
    if time()>interval:
        cookie_count=int(driver.find_element(By.ID, "money").text.replace(",", ""))

        affordable_upgrades=[upgrade for upgrade in all_upgrades if upgrade['price']<=cookie_count]
        
        print(affordable_upgrades)

        upgrade_to_do=driver.find_element(By.ID, affordable_upgrades[-1]['id'])
        upgrade_to_do.click()

        interval=time()+2

print(cookies_per_second.text)

driver.quit()

