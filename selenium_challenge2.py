from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name=driver.find_element(By.NAME, "fName")
f_name.send_keys("james")

l_name=driver.find_element(By.NAME, "lName")
l_name.send_keys("taylor")

email=driver.find_element(By.NAME, "email")
email.send_keys("example@gmail.com")

enter=driver.find_element(By.CSS_SELECTOR, "form button")
enter.send_keys(Keys.ENTER)

# driver.quit()