from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.edge.options import Options
#config = Options()
#config.add_argument("--start-maximized")

def safe_click(driver, button):
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    try:
        button.click()
    except:
        driver.execute_script("arguments[0].click();", button)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.foodfe.app/")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[normalize-space()='Login to Menu Planner']")
))

#button = driver.find_element(By.XPATH,"//button[normalize-space()='Login to Menu Planner']")
button.click()

wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='PlannerHeader_headerContainer__FTypm PlannerHeader_headerContainerBgColor__s+NlP']")))
time.sleep(3)
driver.back()

about =wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "About")))
print(about.text)
work = driver.find_element(By.LINK_TEXT,"How It Works")
work.click()
print(work.text)
button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Login']")))
safe_click(driver, button)
driver.set_page_load_timeout(30)
button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[2]//button[1]")))
driver.execute_script("arguments[0].scrollIntoView(true);", button)
button.click()




#WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, "(//input[@class='login-email'])[1]")))
#email_input = WebDriverWait(driver, 30).until(
    #EC.element_to_be_clickable((By.XPATH, "//span[2]//input[1]"))
#)
#email_input.send_keys("ashokgaur")#
