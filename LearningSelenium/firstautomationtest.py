from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.edge.options import Options
#config = Options()
#config.add_argument("--start-maximized")

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://admin.foodfe.app/")
wait = WebDriverWait(driver, 10)
text= wait.until(EC.visibility_of_element_located((By.XPATH,"//div[normalize-space()='Registrer e-post adresse']")))
print(text.text)
email = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[2]//input[1]"))).send_keys("foodfe8@gmail.com")
button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[2]//button[1]")))
button.click()
time.sleep(5)