from time import sleep
from selenium import webdriver

class InstaBot:
    def __init__():

        browser = webdriver.Firefox()
        browser.implicitly_wait(5)

        browser.get('https://instagram.com')

        sleep(2)

        cookie_button = browser.find_element(by="xpath", value="//*[text()='Only Allow Essential Cookies']")
        cookie_button.click()

        sleep(5)

        username_input = browser.find_element(by="css selector", value="input[name='username']")
        password_input = browser.find_element(by="css selector", value="input[name='password']")

        username_input.send_keys("<Your username>")
        password_input.send_keys("<Your Password>")

        login_button = browser.find_element(by="xpath", value="//button[@type='submit']")
        login_button.click()

        sleep(5)

        save_details_button = browser.find_element(by="xpath", value="//button[text()='Not now']")
        save_details_button.click()

        sleep(10)

        browser.close()