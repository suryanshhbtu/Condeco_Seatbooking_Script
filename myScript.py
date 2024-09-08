import configparser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Load Configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Storing Credentials
email = config.get('credentials', 'email')
password = config.get('credentials', 'password')
login_url = config.get('urls', 'login_url')

# Seating Plan
floor = config.get('seating', 'floor')
seatNo = config.get('seating', 'seatNo')

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Loading Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(login_url)
# Logging In
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)

login_button = driver.find_element(By.ID, "ping-signin-button")
login_button.click()
time.sleep(1)

# Navigating To Personal Booking
iframe = driver.find_element(By.XPATH, "//iframe[@id='leftNavigation']")
driver.switch_to.frame(iframe)

# Selecting Desk Booking
personalSpaceButton = driver.find_element(By.ID, "DeskBookingHeader")
personalSpaceButton.click()
time.sleep(2)

try:
    alert = driver.switch_to.alert
    alert.accept()
    print("Alert accepted successfully.")
    
except NoAlertPresentException:
    print("No alert was present on the page.")

time.sleep(1)

driver.find_element(By.ID, "li_findADesk").click()
driver.switch_to.default_content()
time.sleep(2)

# Changing iFrame
iframe = driver.find_element(By.XPATH, "//iframe[@id='mainDisplayFrame']")
driver.switch_to.frame(iframe)
time.sleep(2)

# Selecting Department
dropdown = Select(driver.find_element(By.ID, "listGroup"))
dropdown.select_by_index(9)
time.sleep(2)

# Selecting Floor
dropdown = Select(driver.find_element(By.ID, "listFloor"))
dropdown.select_by_index(0 if int(floor) == 4 else 1)
time.sleep(2)

# Selecting Date -> 2 week later
driver.find_element(By.CSS_SELECTOR, "label[for='incAM_7']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incAM_8']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incAM_9']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incAM_10']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incAM_11']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incPM_7']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incPM_8']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incPM_9']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incPM_10']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='incPM_11']").click()

time.sleep(3)

# Tap Search
driver.find_element(By.ID, "btnSearch").click()
time.sleep(8)

# Switching Frame
driver.switch_to.default_content()
driver.switch_to.frame("mainDisplayFrame")
driver.find_element(By.ID, "tabBookingList").click()
time.sleep(2)

# My Personal Seat pre
button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Book workspace '+seatNo+'"]')
button.click()

button = driver.find_element(By.ID, 'btnAlertOkay')
button.click()

time.sleep(5)

driver.quit()
