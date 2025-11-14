
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

searchbox = (By.CLASS_NAME, "search-keyword")
text1 = (By.XPATH, "//h4[text()='Cucumber - 1 Kg']")
text2 = (By.XPATH, "//h4[text()='Raspberry - 1/4 Kg']")
text3 = (By.XPATH, "//h4[text()='Strawberry - 1/4 Kg']")

C= (By.XPATH, "//div[@class='products']//div[1]//div[3]//button[1]")
A= (By.XPATH, "//div[@class='products']//div[2]//div[3]//button[1]")
B= (By.XPATH, "//div[@class='products']//div[3]//div[3]//button[1]")
cart= (By.XPATH, "//a[@class='cart-icon']")
button= (By.XPATH, "//*[text()='PROCEED TO CHECKOUT']")


