from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Use your own google sheet link and 591 link with preferred location
FORM_LINK = "google_sheet_link"
RENT_LINK = "https://rent.591.com.tw/?region=15&kind=3&rentprice=,10000"

chrome_driver_path = "C:/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.maximize_window()
driver.get(url=RENT_LINK)

time.sleep(5)
price_list = [price.text for price in driver.find_elements(By.CSS_SELECTOR, ".item-price-text span")]
address_list = [address.text for address in driver.find_elements(By.CSS_SELECTOR, ".item-area span")]
link_list = [link.get_attribute("href") for link in driver.find_elements(By.CSS_SELECTOR, ".vue-list-rent-item a")]

print(price_list)
print(address_list)
print(link_list)

driver.get(url=FORM_LINK)
time.sleep(3)

for n in range(len(price_list)):
    address_entry = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_entry = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_entry = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_entry.send_keys(price_list[n])
    price_entry.send_keys(address_list[n])
    link_entry.send_keys(link_list[n])
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(2)
    next = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next.click()
    time.sleep(2)