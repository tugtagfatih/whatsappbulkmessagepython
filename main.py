from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import urllib.parse

chrome_driver_path = "C:/Users/User/Desktop/pythonchrometoplumesaj/chromedriver-win64/chromedriver.exe"
use_profile = True  # For save the browser profile
profile_folder = "C:/Users/User/Desktop/pythonchrometoplumesaj/whatsapp_profile" 

options = webdriver.ChromeOptions()
if use_profile:
    if not os.path.exists(profile_folder):
        os.makedirs(profile_folder)
    options.add_argument(f"user-data-dir={profile_folder}")

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

print("WhatsApp Web is loading...")
driver.get("https://web.whatsapp.com/")

time.sleep(5)
try:
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
    )
    print("Successfully logged in!")
except Exception as e:
    print("Login failed! Error:", e)
    driver.quit()
    exit()
with open("numbers.txt", "r", encoding="utf-8") as f:
    numbers = [line.strip() for line in f if line.strip()]
with open("text.txt", "r", encoding="utf-8") as f:
    message = f.read().strip()
    message = urllib.parse.quote(message)
for number in numbers:
    print(f"Message is being sent: {number}")
    url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    driver.get(url)

    try:
        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='wds-ic-send-filled']"))
        )

        send_button.click()

        print(f"Message sent: {number}")
    except Exception as e:
        print(f"Message could not be sent: {number}")

    time.sleep(5)

print("All messages have been sent successfully.")
