from selenium import webdriver


driver = webdriver.Chrome()

class openurl():
    def pageopen(self):       #Every method inside a class takes self as the first argument — it refers to the current object of the class.

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        return driver   # return so that we can use it another class

