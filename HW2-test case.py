from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.target.com/")
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl' and text()='Sign in']").click()

sleep(6)

actual_text = driver.find_element(By.XPATH, "//h1[contains(@class, 'AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa')]").text
assert 'Sign into your Target account' in actual_text, f'ERROR!!! Text Sign into your Target account not in {actual_text}'

print('Test case passed')

driver.quit()
