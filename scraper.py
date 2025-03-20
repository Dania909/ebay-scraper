import csv
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Setup Selenium ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = Service()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.ebay.com/globaldeals/tech"
driver.get(url)
time.sleep(3)

# Scroll down the page slowly to trigger lazy loading
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

products = driver.find_elements(By.CSS_SELECTOR, 'div.ebayui-dne-item-featured-card, div.dne-itemtile')

data = []

for product in products:
    try:
       
        try:
            title = product.find_element(By.CSS_SELECTOR, '.dne-itemtile-title').text.strip()
        except:
            title = 'N/A'

        try:
            price = product.find_element(By.CSS_SELECTOR, 'span[itemprop="price"]').text.strip()
        except:
            price = 'N/A'

        try:
            original_price = product.find_element(By.CSS_SELECTOR, 'span.itemtile-price-strikethrough').text.strip()
        except:
            original_price = 'N/A'

        try:
            shipping = product.find_element(By.CSS_SELECTOR, 'span.dne-itemtile-delivery').text.strip()
        except:
            shipping = 'N/A'

        item_url = product.find_element(By.TAG_NAME, 'a').get_attribute('href').strip()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data.append([timestamp, title, price, original_price, shipping, item_url])

    except Exception as e:
        print(f"Skipped a product due to unexpected error: {e}")


# Save the extracted data to CSV
csv_file = 'ebay_tech_deals.csv'
file_exists = os.path.isfile(csv_file)

with open(csv_file, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(['timestamp', 'title', 'price', 'original_price', 'shipping', 'item_url'])

    writer.writerows(data)

print(f"Extracted {len(data)} products successfully.")

driver.quit()
