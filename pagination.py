from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pandas as Pd

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://books.toscrape.com")
all_books= []

wait = WebDriverWait(driver, 10)
cnt=0
while True:
    books = wait.until(

    
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "article.product_pod")
        )
    )
    for i in books:
       title = driver.find_element(By.CSS_SELECTOR, "img.thumbnail")
       price = driver.find_element(By.CSS_SELECTOR, ".price_color")
       data = {
           "Title": title.text,
           "Price": price.text
       }
    try:
        d = driver.find_element(By.CSS_SELECTOR,"li.next a")
        d.click()
    except:
        break
    cnt+=len(books)
    print(f"Scraped in this page: {len(books)}")

print(f"total books = {cnt}")
df = pd.DataFrame(data)
  
