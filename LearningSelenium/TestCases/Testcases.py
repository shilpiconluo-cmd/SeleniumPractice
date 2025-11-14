from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from LearningSelenium.Browser.Browsercall import openurl
from LearningSelenium.Browser.XPath import searchbox, text1, text2, text3,C,A,B
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

import os    # to delete files

class testcase():
    def __init__(self): # constructor — it automatically runs when you create an object of this class.
        self.browser = openurl().pageopen() # stores the returned driver (browser) inside self.browser.
    def tc1(self):
        print(self.browser.title)
        self.browser.find_element(*searchbox).send_keys("ber")
        T1= self.browser.find_element(*text1).text
        T2= WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(text2)).text
        T3= WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(text3)).text

        text =  [T1, T2, T3]   # list of all texts
        file_name = "fruits.txt"   #genereta file
        with open("fruits.txt","w") as file:
            for item in text:
                file.write(item +"\n")
        time.sleep(4)

        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(C)).click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(A)).click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(B)).click()
        cart =  WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cart-icon']")))
        cart.click()
        button =  WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='PROCEED TO CHECKOUT']")))
        button.click()


        text4 = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Cucumber - 1 Kg']"))).text
        text5 = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Raspberry - 1/4 Kg']"))).text
        text6 = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Strawberry - 1/4 Kg']"))).text


        content = (text4, text5, text6)
        file_name = "shopping.txt"
        with open("shopping.txt","w") as writer:
            for Slist in content:
                writer.write(Slist+"\n")

        with open("fruits.txt","r") as file1:
            Comp1= file1.read().splitlines()
        with open("shopping.txt","r") as file2:
            Comp2= file2.read().splitlines()
        if Comp1==Comp2:
            print("Mission successful")
            os.remove("fruits.txt")
            os.remove("shopping.txt")
            print("Deleted all files")
        else:
            print("Different")

        promo= WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@class= 'promoCode']")))
        promo.send_keys("rahulshettyacademy")
        self.browser.find_element(By.XPATH,"//*[text()= 'Apply']").click()
        msg = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH,"//*[text()= 'Code applied ..!']")))
        successmsg = msg.text
        if successmsg == "Code applied ..!":
            print("Shilpi is doing good work")
        else:
            print("code did not work")




TC= testcase()  #This automatically runs the __init__() method, so the browser opens.
TC.tc1()