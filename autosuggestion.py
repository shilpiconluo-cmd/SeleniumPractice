from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Autosuggest():
    def autosuggestion(self):
      driver = webdriver.Chrome()
      driver.maximize_window()
      driver.get("https://www.yatra.com/")
      oneway = driver.find_element(By.XPATH,"//h4[normalize-space()='One Way']").is_enabled()
      print(oneway)
      WebDriverWait(driver, 10).until(
          EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Departure From']"))
      )
      driver.find_element(By.XPATH, "//p[normalize-space()='Departure From']").click()
      depat = driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']").send_keys("New")
      search_results = driver.find_elements(By.XPATH,"//span[normalize-space()='New Haven']")
      time.sleep(4)
      nyc_option = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='New Haven']"))
      )
      print("Found option:", nyc_option.text)
      nyc_option.click()
      time.sleep(4)  # Just to see the result before closing
      driver.find_element(By.XPATH,"//p[normalize-space()='Going To']").click()
      arrival = driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']").send_keys("Bang")
      time.sleep(4)
      nyc1_option = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.XPATH, "//span[normalize-space(text())='Bangalore']"))
      )
      print("Found option:", nyc1_option.text)
      nyc1_option.click()
      time.sleep(2)
      driver.find_element(By.XPATH,"//div[normalize-space()='Student']").click()
      driver.find_element(By.XPATH,"//span[normalize-space()='Travellers & Class']")
      WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".position-relative.css-13i4lru")))

      trav = (driver.find_element(By.CSS_SELECTOR,".position-relative.css-13i4lru"))
      trav.screenshot(".\\test.png")
      trav.click()
      driver.get_screenshot_as_file(".\\yatra.png")
      time.sleep(6)
      #adult = driver.find_element(By.XPATH,"(//ul[@class='css-19awrdm']//li)[3]").click()
      #WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='( 2-12 YRS )']")))
      adult_li = WebDriverWait(driver, 10).until(
          EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-label='Adult']//li"))
      )
      adult_li[2].click()  # Python index starts at 0
      time.sleep(0.5)

      # Wait for Child li elements
      child_li = WebDriverWait(driver, 10).until(
          EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-label='Child']//li"))
      )

      # Select Children = 1 (2nd li)
      child_li[1].click()
      time.sleep(0.5)

      # Wait for Infant li elements
      infant_li = WebDriverWait(driver, 10).until(
          EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-label='Infant']//li"))
      )

      # Select Infant = 0 (1st li)
      infant_li[0].click()
      time.sleep(0.5)
      #child_age = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='MuiStack-root css-1yhvumz']//li[1]")))
      #child_age.click()
     #WebDriverWait(driver, 10).until(
          #EC.visibility_of_element_located((By.XPATH, "//p[@aria-label='Infant']")))
      #infant = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[@class='css-5g008u'][normalize-space()='0']")))
      #time.sleep(2)
      #driver.get_screenshot_as_file(".\\yatra1.png")
      #driver.quit()


#//input[@id='input-with-icon-adornment']
auto = Autosuggest()
auto.autosuggestion ()

