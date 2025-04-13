from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Setup
driver = webdriver.Chrome()  # or provide the path to your chromedriver
driver.get("https://banweb.canton.edu/StudentRegistrationSsb/ssb/registration/registration")
wait = WebDriverWait(driver, 20)

# Click "Browse Classes"
browse_classes_link = wait.until(EC.element_to_be_clickable((By.ID, "classSearchLink")))
browse_classes_link.click()


#Select Term
term_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "s2id_txt_term")))
term_dropdown.click()
search_input = wait.until(EC.presence_of_element_located((By.ID, "s2id_autogen1_search")))
search_input.send_keys("Fall 2025")
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='202509' and text()='Fall 2025']")))
search_input.send_keys(Keys.ENTER)
continue_button = wait.until(EC.element_to_be_clickable((By.ID, "term-go")))
continue_button.click()

# Wait for search button and click it
search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]")))
search_btn.click()

# Click "Continue"
continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(),'Continue')]")))
continue_btn.click()
driver.sleep(4)
driver.get("https://banweb.canton.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202509&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=500&sortColumn=subjectDescription&sortDirection=asc")

# Optional: Wait and close after viewing results
time.sleep(5)
driver.quit()
