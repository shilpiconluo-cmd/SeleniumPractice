from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
class openurl():
    def pageopen(self):       #Every method inside a class takes self as the first argument — it refers to the current object of the class.

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        return driver   # return so that we can use it another class

