from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")

#oepning link in new tab
link = driver.find_element(By.LINK_TEXT,"Glemt passordet?")
clt_enter = Keys.CONTROL + Keys.ENTER
link.send_keys(clt_enter)


#opening new website in new tab
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.switch_to.new_window('tab')
driver.get ("https://mail.google.com/mail/u/0/")

#opening new website in new window

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.switch_to.new_window('window')
driver.get ("https://mail.google.com/mail/u/0/")