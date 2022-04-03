from time import sleep
from selenium import webdriver

class InstaBot:
    def __init__(self):

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

        self.browser.get('https://instagram.com')

        sleep(2)

        cookie_button = self.browser.find_element(by="xpath", value="//*[text()='Only Allow Essential Cookies']")
        cookie_button.click()

        sleep(5)

    def login(self):

        username_input = self.browser.find_element(by="css selector", value="input[name='username']")
        password_input = self.browser.find_element(by="css selector", value="input[name='password']")

        username_input.send_keys("<Your username>")
        password_input.send_keys("<Your Password>")

        login_button = self.browser.find_element(by="xpath", value="//button[@type='submit']")
        login_button.click()

        sleep(5)

        save_details_button = self.browser.find_element(by="xpath", value="//button[text()='Not now']")
        save_details_button.click()

        sleep(10)

    def close_browser(self):

        self.browser.close()