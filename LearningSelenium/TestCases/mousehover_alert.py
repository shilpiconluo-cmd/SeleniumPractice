from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import os
import time

class mouseh():
    def mohv(self):
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        action1 = ActionChains(driver)
       # button1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"mousehover")))
        action1.move_to_element(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"mousehover")))).perform()
        top =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Top']")))
        action1.move_to_element(top).click().perform()
        driver.switch_to.new_window("tab")
        driver.get("https://the-internet.herokuapp.com/hovers")
        action1.move_to_element(driver.find_element(By.XPATH,"//div[@class='example']//div[1]//img[1]")).perform()
        text1 = driver.find_element(By.XPATH,"//h5[normalize-space()='name: user1']").text
        print(text1)
        driver.switch_to.new_window("tab")
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        action1.context_click(driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']")).perform()
        time.sleep(2)
        button = driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
        alert = driver.switch_to.alert
        assert "I am a JS Alert" == alert.text
        alert.accept()
        time.sleep(3)
        text2= driver.find_element(By.ID,"result").text
        assert text2 == "You successfully clicked an alert"
        driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
        driver.switch_to.alert
        alert.dismiss()
        text2 = driver.find_element(By.ID, "result").text
        print(text2)




obj = mouseh()
obj.mohv()