from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from LearningSelenium.Browser.Browsercall import openurl
from LearningSelenium.Browser.XPath import searchbox, text1, text2, text3,C,A,B
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os    # to delete files

list1 = []
list2 = []
class testcase():
    def __init__(self): # constructor — it automatically runs when you create an object of this class.
        self.browser = openurl().pageopen() # stores the returned driver (browser) inside self.browser.
    def tc1(self):
        print(self.browser.title)
        self.browser.find_element(*searchbox).send_keys("ber")
        time.sleep(2)
        buttons = self.browser.find_elements(By.XPATH, "//div[@class='product-action']/button")
        for button in buttons:
           list1.append(button.find_element(By.XPATH, "./ancestor::div[@class='product']//h4").text)
           button.click()

        print(list1)
        cart = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cart-icon']")))
        cart.click()
        button1 = WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='PROCEED TO CHECKOUT']")))
        button1.click()

        Products = self.browser.find_elements(By.XPATH,"//p[@class='product-name']")
        for product in Products:
            if product.text=="":
                break
            list2.append(product.text)





        print(list2)
        if list1== list2:
            print("same veggies are there")

        promo = WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class= 'promoCode']")))
        promo.send_keys("rahulshettyacademy")
        self.browser.find_element(By.XPATH, "//*[text()= 'Apply']").click()
        msg = WebDriverWait(self.browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()= 'Code applied ..!']")))
        successmsg = msg.text
        if successmsg == "Code applied ..!":
         print("Shilpi is doing good work")
        else:
         print("code did not work")

TC= testcase()  #This automatically runs the __init__() method, so the browser opens.
TC.tc1()