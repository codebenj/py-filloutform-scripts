import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List

# Test data
test_data = {
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

def navigate_to_form(driver: webdriver.Chrome) -> None:
    driver.get("http://127.0.0.1:5500/")

def fill_text_field(driver: webdriver.Chrome, field_label: str, value: str) -> None:
    # Find the text field by its associated label
    print(field_label)
    label = driver.find_element(By.XPATH, f"//label[contains(text(), '{field_label}')]")

    # Try to find an input or textarea element following the label
    try:
        input_field = label.find_element(By.XPATH, "./following-sibling::input")
    except:
        input_field = label.find_element(By.XPATH, "./following-sibling::textarea")

    input_field.send_keys(value)

def detect_recaptcha(driver: webdriver.Chrome) -> bool:
    # Check if a recaptcha iframe or element is present
    recaptcha_elements = driver.find_elements(By.XPATH, "//iframe[contains(@src, 'recaptcha')] | //div[contains(@class, 'g-recaptcha')]")
    return len(recaptcha_elements) > 0

def submit_form_by_button_click(driver: webdriver.Chrome) -> None:
    # Find the submit button - Adjust the selector as needed
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    # Click the submit button
    submit_button.click()

# Main script
driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5500/')

# Fill in the form fields based on label text and test data
fill_text_field(driver, "Name", r"{test_data['firstName']} {test_data['lastName']}")
fill_text_field(driver, "Email", test_data["email"])
fill_text_field(driver, "Phone", test_data["phone"])
fill_text_field(driver, "City", test_data["city"])
fill_text_field(driver, "State", test_data["state"])
fill_text_field(driver, "Zip Code", test_data["postalCode"])
fill_text_field(driver, "Business", test_data["businessName"])
fill_text_field(driver, "Message", test_data["message"])

# Detect recaptcha
if detect_recaptcha(driver):
    print("Recaptcha detected.")
else:
    print("No recaptcha detected.")

# Submit the form
# submit_form_by_button_click(driver)

# Keep the browser open for a specified amount of time
time.sleep(30) 