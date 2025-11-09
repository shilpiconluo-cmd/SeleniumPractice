from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class mousehover():
    def hovere(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.hindustantimes.com/")
        el1 = driver.find_element(By.XPATH,"//a[normalize-space()='+ 17 more']")
        Action = ActionChains(driver)
        Action.move_to_element(el1).perform()
        driver.find_element(By.XPATH,"//li[@class=' cohortMore']//a[normalize-space()='Cities']").click()
        time.sleep(4)


ms = mousehover()
ms.hovere()