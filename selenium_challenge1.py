from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver=webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")

dates= driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events= driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for element in dates:
    print(element.text)
for element in events:
    print(element.text)

events_dict={f"{i}":{'date':dates[i].text, 'event':events[i].text} for i in range(len(events))}
print(events_dict)

driver.quit()