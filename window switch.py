from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SwitchWindowdemo():
    def switchwindow(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://foodfe.app/")
        parent = driver.current_window_handle
        print(parent)
        allhandles = driver.window_handles
        print(allhandles)
        login = (WebDriverWait(driver,4).
                 until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Login']"))))

        login.click()
        time.sleep(4)





        RENHOLDSCOMPAGNIET AS






SW = SwitchWindowdemo()
SW.switchwindow()
