from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://books.toscrape.com")

wait = WebDriverWait(driver, 5 )


books = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "article.product_pod")

    )
    
)

print(len(books))