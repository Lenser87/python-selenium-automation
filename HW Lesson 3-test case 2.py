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

driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

sleep(6)

driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(6)

actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text

sleep(6)

assert 'Sign into your Target account' in actual_text, f'ERROR!!! Text Sign into your Target account not in {actual_text}'
print('Test case passed')

driver.quit()
