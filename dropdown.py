from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium. webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC

class Dropdown():
    def demo_dropdown(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.salesforce.com/form/signup/c/")
        driver.find_element(By.NAME,"UserFirstName").send_keys("Shilpi")
        driver.find_element(By.NAME,"UserLastName").send_keys("ghildiyal")
        driver.find_element(By.NAME, "UserTitle").send_keys("QA Analyst")
        driver.find_element(By.NAME, "UserEmail").send_keys("shilpi.ghildiyal@gmail.com")
        time.sleep(3)
        emp = driver.find_element(By.NAME,"CompanyEmployees")
        dd = Select(emp)
        dd.select_by_value("10")
        wait = WebDriverWait(driver, 4)
        driver.find_element(By.NAME,"UserPhone").send_keys("+919540250719")
        country = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.NAME,"CompanyCountry")))
        cc = Select(country)
        #dd.select_by_value("US")
        #dd.select_by_visible_text('United States')
      #  wait = WebDriverWait(driver,5)
        driver.find_element(By.XPATH,"//div[@class='field valid']//div[@class='checkbox-ui']").click()


drop = Dropdown()
drop.demo_dropdown()





