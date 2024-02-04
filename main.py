from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import WEBSITE

def hello_selenium_edge():
    driver = webdriver.Edge()

    driver.get("http://selenium.dev")

    driver.quit()


def hello_selenium_firefox():
    print('Hello Selenium Firefox!')

    driver = webdriver.Firefox()

    driver.get("http://selenium.dev")

    driver.quit()
    print('Bye Selenium Firefox!')


def init_driver_firefox():
    print('Initializing Firefox driver...')
    driver = webdriver.Firefox()
    driver.get(WEBSITE)
    return driver


def quit_driver(driver):
    print('Quitting Firefox driver...')
    driver.quit()


def get_info(driver):
    print('Getting info from Firefox driver...')

    print(driver.current_url)
    title = driver.title
    print(title)

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    text = message.text
    print(text)


if __name__ == '__main__':

    #hello_selenium_firefox()
    #hello_selenium_edge()
    driver = init_driver_firefox()
    get_info(driver)
    quit_driver(driver)

