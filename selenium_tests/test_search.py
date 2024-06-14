from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the application
driver.get("http://localhost:8000")  # Replace with your app's URL

# Log in to the application (if authentication is required)
# email_input = driver.find_element(By.NAME, "email")
# email_input.send_keys("test@example.com")
# password_input = driver.find_element(By.NAME, "password")
# password_input.send_keys("password123")
# login_button = driver.find_element(By.ID, "loginButton")
# login_button.click()

# Navigate to the file upload page
driver.get("http://localhost:8000/upload")  # Replace with your upload URL

# Upload a file
file_input = driver.find_element(By.ID, "fileInput")
file_input.send_keys("/path/to/test_file.txt")  # Replace with the path to your test file

# Submit the form
upload_button = driver.find_element(By.ID, "uploadButton")
upload_button.click()

# Wait for the upload to complete (adjust the sleep time as needed)
time.sleep(5)

# Verify the upload was successful
success_message = driver.find_element(By.ID, "successMessage")
assert "Upload successful" in success_message.text

# Close the browser
driver.quit()
