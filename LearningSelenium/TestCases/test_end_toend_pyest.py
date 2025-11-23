from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options   # how borwser shpuld behave, for sele 4 n more
from selenium.webdriver import ActionChains
import os
import time
import pytest




class TestEnd:
    def test_shopping(self):
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.find_element(By.XPATH,"//*[text()= 'Shop'] ").click()
        products = driver.find_elements(By.XPATH,"//div[contains(@class, 'card') and contains(@class, 'h-100')]")
        for product in products:
            product_name = product.find_element(By.XPATH,"div/h4/a").text
            if product_name == "Nokia Edge":
                product.find_element(By.XPATH,"div/button").click()
        checout = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR," a[class*= 'btn-primary']")))
        checout.click()
        text2 = driver.find_element(By.XPATH,"//a[normalize-space()='Nokia Edge']").text
        assert text2 == "Nokia Edge"
        driver.find_element(By.XPATH,"//button[contains(@class, 'btn-success')]").click()
        driver.find_element(By.ID,"country").send_keys("Norway")
        driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
        driver.get_screenshot_as_file("shopping.png")
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        text3 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'alert-success')]"))).text
        assert "Success! Thank you!" in text3


