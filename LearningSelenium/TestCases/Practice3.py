from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os    # to delete files


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
class openurl():
    def pageopen(self):       #Every method inside a class takes self as the first argument — it refers to the current object of the class.

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        return driver   # return so that we can use it another class


class testcase():
    def __init__(self): # constructor — it automatically runs when you create an object of this class.
        self.browser = openurl().pageopen() # stores the returned driver (browser) inside self.browser.
    def tc1(self):
        print(self.browser.title)
        driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")
        text1 =  driver.find_element(By.XPATH,"//h4[text()='Cucumber - 1 Kg']").text
        text2=  wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[text()='Raspberry - 1/4 Kg']"))).text
        text3 = wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[text()='Strawberry - 1/4 Kg']"))).text
        text =  [text1, text2, text3]   # list of all texts
        file_name = "fruits.txt"   #genereta file
        with open("fruits.txt","w") as file:
            for item in text:
                file.write(item +"\n")
        C= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='products']//div[1]//div[3]//button[1]")))
        C.click()
        A= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='products']//div[2]//div[3]//button[1]")))
        A.click()
        B= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='products']//div[3]//div[3]//button[1]")))
        B.click()
        cart= wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='cart-icon']")))
        cart.click()
        button= wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='PROCEED TO CHECKOUT']")))
        button.click()

        text4 = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='Cucumber - 1 Kg']"))).text
        text5 = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='Raspberry - 1/4 Kg']"))).text
        text6 = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='Strawberry - 1/4 Kg']"))).text

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




TC= testcase()  #This automatically runs the __init__() method, so the browser opens.
TC.tc1()