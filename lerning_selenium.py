from selenium import webdriver
from selenium.webdriver.common.by import By

# making the browser to remain open
# configuring driver options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating a chrome driver to drive through website
driver=webdriver.Chrome(chrome_options)

# website to drive through
driver.get("https://www.daraz.pk")

# price=driver.find_element(By.XPATH, value='//*[@id="module_product_price_1"]/div/div/span')


# to close the tab as program end
# driver.close()

# to close the entire browser as progrm end
driver.quit()