import time
from pprint import pprint
from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

def is_contact_form(form: WebElement) -> bool:
    keywords = ['email', 'phone']
    form_html = form.get_attribute('outerHTML').lower()
    return any(keyword in form_html for keyword in keywords)

def find_contact_form(driver: webdriver.Chrome) -> WebElement:
    forms = driver.find_elements(By.TAG_NAME, 'form')
    for form in forms:
        if is_contact_form(form):
            return form
    print("No contact form found on the page.")
    return None

def fill_input_field(field: WebElement) -> None:
    field_type = field.get_attribute('type')
    if field.is_displayed(): 
        if field_type == 'text':
            print("Filling out text field")
            field.send_keys('John Doe')
        elif field_type == 'email':
            print("Filling out email field")
            field.send_keys('john.doe@example.com')
        elif field_type == 'tel':
            print("Filling out telephone field")
            field.send_keys('+1234567890')
        elif field_type in ['radio', 'checkbox']:
            if not field.is_selected() and field.is_enabled():
                print(f"Selecting {field_type} field")
                field.click()

def fill_textarea_field(textarea: WebElement) -> None:
    if textarea.is_displayed():
        print("Filling out textarea")
        textarea.send_keys('Sample message')

def select_first_option(select: WebElement, form: WebElement) -> None:
    time.sleep(1)  # Delay before interacting with each field
    
    options = select.find_elements(By.XPATH, './/option')
    if options:
        for index, option in enumerate(options):
            if option.is_enabled():
                div_option = form.find_elements(By.XPATH, "//*[@role='option']")[index-1]
                option.click()
                Select(select).select_by_value(option.get_property("value"))
                if div_option:
                    print(f"Selecting option: {div_option.text}")
                    div_option.click()
                break

def detect_captcha(form: webdriver.Chrome) -> bool:
    captcha_indicators = ["recaptcha", "captcha"]
    form_page_source = form.get_attribute('outerHTML').lower()
    return any(indicator in form_page_source for indicator in captcha_indicators)

def fill_contact_form(driver: webdriver.Chrome) -> None:
    form = find_contact_form(driver)
    if form:
        input_fields = form.find_elements(By.XPATH, ".//input")
        for field in input_fields:
            fill_input_field(field)

        selects = form.find_elements(By.TAG_NAME, 'select')
        for select in selects:
            select.click()
            select_first_option(select, form)

        textareas = form.find_elements(By.TAG_NAME, 'textarea')
        for textarea in textareas:
            fill_textarea_field(textarea)

        if detect_captcha(form):
            print("Captcha detected.")


def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    websites = ["https://www.alpstra.com/contact",
                "https://www.fresnoplumbinginc.com/contact-us/",
                "https://transformationalpresence.org/contact-us/"]

    for website in websites:
        print("====================================================")
        print(f"Accessing: {website}")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(website)
        fill_contact_form(driver)
        print("====================================================")
    
    # Keep the browser open for a specified amount of time
    time.sleep(30)

    driver.quit() 

if __name__ == "__main__":
    main()
