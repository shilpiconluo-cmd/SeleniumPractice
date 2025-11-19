from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class child():
    def childwind(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/")
        wind = driver.find_element(By.XPATH,"//*[text()= 'Multiple Windows']")
        wind.click()
        wind1 = driver.find_element(By.XPATH,"//*[text()= 'Click Here'] ")
        wind1.click()
        childwind= driver.window_handles[1]
        driver.switch_to.window(childwind)
        el = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h3[normalize-space()='New Window']")))
        print(el.text)

obj = child()
obj.childwind()
