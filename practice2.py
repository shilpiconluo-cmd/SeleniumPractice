from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Flightdeals():
    def deals(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.find_element(By.XPATH,"//a[text()='Flight Booking']").click()
        handles = driver.window_handles
        print(handles)
        current = driver.current_window_handle
        for i in handles:
            if i!= current:
                driver.switch_to.window(i)
        driver.find_element(By.XPATH,"//input[contains(@id,'autosuggest')]").send_keys("India")
        driver.find_element(By.XPATH,"//input[contains(@id,'ctl00_mainContent_rbtnl_Trip_1')]").click()
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.ID, "ctl00_mainContent_ddl_originStation1_CTXT").click()
        time.sleep(4)
        origin =  wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@value='JAI']")))
        origin.click()
        








obj = Flightdeals()
obj.deals()
