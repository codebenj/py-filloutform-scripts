import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Test data
data = {
    "firstName": "John",
    "lastName": "Smith",
    "email": "jsmith@test.com",
    "phone": "1231231234",
    "message": "Hello, I filled your form!",
    "city": "Atlantis",
    "state": "Unknown",
    "postalCode": "42424",
    "businessName": "RU"
}

driver = webdriver.Chrome()

# Open the local URL
driver.get('http://127.0.0.1:5500/')

# Fill the form
driver.find_element(By.ID, "a").send_keys(data["firstName"] + " " + data["lastName"])  # Assuming 'a' is for full name
driver.find_element(By.ID, "b").send_keys(data["email"])
driver.find_element(By.ID, "c").send_keys(data["phone"])
driver.find_element(By.ID, "d").send_keys(data["city"])
driver.find_element(By.ID, "e").send_keys(data["state"])
driver.find_element(By.ID, "f").send_keys(data["postalCode"])
driver.find_element(By.ID, "g").send_keys(data["businessName"])
driver.find_element(By.ID, "h").send_keys(data["message"])  # Assuming 'h' is for the message

# Keep the browser open for a specified amount of time
time.sleep(30)  # Adjust the time as needed

driver.quit()  # Uncomment this line to close the browser automatically after a delay
