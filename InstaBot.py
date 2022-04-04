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

        username_input.send_keys("")
        password_input.send_keys("")

        login_button = self.browser.find_element(by="xpath", value="//button[@type='submit']")
        login_button.click()

        sleep(5)

        save_details_button = self.browser.find_element(by="xpath", value="//button[text()='Not now']")
        save_details_button.click()

        sleep(5)

        save_details_button = self.browser.find_element(by="xpath", value="/html/body/div[6]/div/div/div/div[3]/button[2]")
        save_details_button.click()

        sleep(5)

    def open_messages(self):

        messages_button = self.browser.find_element(by="xpath", value="/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
        messages_button.click()

        sleep(5)

        dbdChat_button = self.browser.find_element(by="xpath", value="/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a")
        dbdChat_button.click()

        sleep(5)

    def close_browser(self):

        self.browser.close()

if __name__ == "__main__":
    testBot = InstaBot()
    testBot.login()
    testBot.open_messages()
