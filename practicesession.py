from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select


class Practice():
    def practiceweb(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        searchbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='search']")))
        searchbox.send_keys("Cauliflower")
        driver.find_element(By.XPATH,"//div[contains(@class,'stepper-input')]/a[@class='increment']").click()
        driver.find_element(By.XPATH,"//div[contains(@class,'product-action')]/button").click()
        searchbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='search']"))).clear()
        driver.refresh()
        driver.find_element(By.LINK_TEXT,"Top Deals").click()
        abc = driver.window_handles
        print(abc)
        current = driver.current_window_handle
        print(current)
        newwindow = abc[1]
        driver.switch_to.window((newwindow))
        driver.find_element(By.ID,"search-field").send_keys("rice")
        Header1 = driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").text
        Header2 = driver.find_element(By.XPATH, "//span[text()='Price']").text
        Header3 = driver.find_element(By.XPATH, "//span[text()='Discount price']").text
        print(Header1, Header2, Header3)
        drop1 = driver.find_element(By.ID,"page-menu")
        dd = Select(drop1)
        dd.select_by_value("10")
        driver.find_element(By.XPATH,"//button[contains(@class, 'react-date-picker__calendar-button')]").click()
        #time.sleep(4)
        date = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[.//abbr[contains(@aria-label, '14') and contains(@aria-label, 'November 2025')]]")))
        date.click()
        #first = driver.find_element(By.XPATH,"//li[contains(@class, 'disabled')]/a[@aria-label='First']").get_attribute("class")
       # previous = driver.find_element(By.XPATH,"//li[contains(@class, 'disabled')]/a[@aria-label='Previous']").is_enabled()
        if "disabled" in driver.find_element(By.XPATH, "//li[a[@aria-label='First']]").get_attribute("class"):
            print("It's disabled")
        if "disabled" in driver.find_element(By.XPATH, "//li[a[@aria-label='Previous']]").get_attribute("class"):
            print("It also  disabled")

        time.sleep(4)







obj = Practice()
obj.practiceweb()


