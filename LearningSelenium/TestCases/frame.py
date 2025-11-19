from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

class Frame():
    def frame1(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/frames")
        driver.find_element(By.XPATH,"//*[text()= 'iFrame']").click()
        driver.switch_to.frame("mce_0_ifr")
        driver.find_element(By.CLASS_NAME,"mce-content-body ").clear()
        driver.find_element(By.ID,"tinymce").send_keys("I am learning automation.\nI like swiming")
        driver.switch_to.default_content()
        driver.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']").click()
        child = driver.window_handles[1]
        driver.switch_to.window(child)
        text = driver.title
        file_name = "title.txt"
        with open("title.txt","w") as file:
            file.write(text)
        with open(file_name,"r") as reader:
            print(reader.read())

        os.remove(file_name)




obj = Frame()
obj.frame1()

