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
        time.sleep(4)







obj = Practice()
obj.practiceweb()


