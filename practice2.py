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
        origin, destination = Flightdeals.readfile()

        driver.find_element(By.ID, "ctl00_mainContent_ddl_originStation1_CTXT").click()
        time.sleep(1)  # wait for dropdown
        origin_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[@class='left1']//a[@value='{origin}']")  # scope to origin div
        ))
        origin_element.click()
        #driver.execute_script("arguments[0].click();", origin_element)

        # Select destination
        driver.find_element(By.ID, "ctl00_mainContent_ddl_destinationStation1_CTXT").click()
        time.sleep(1)  # wait for dropdown
        destination_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[@class='right1']//a[@value='{destination}']")  # scope to destination div
        ))
        destination_element.click()
        #driver.execute_script("arguments[0].click();", destination_element)

    @staticmethod
    def readfile():
        with open("Citiesfor flight.txt", "r") as f:
         line = f.readline().strip()
         origin_element, destination_element = line.split(",")
         return origin_element, destination_element




obj = Flightdeals()
obj.deals()
