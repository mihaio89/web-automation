from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


WEBSITE = "https://www.amazon.com"
SEARCH_BOX = "twotabsearchtextbox"
SUBMIT_BUTTON = "nav-search-submit-button"
WAIT_TIME_SECONDS = 3

SEARCH_FOR = "headphones"

def quit_driver(driver, source):
    print(f'Quitting Firefox driver... called from {source}')
    driver.quit()


def get_driver_firefox():
    try:
        print('Initializing Firefox driver...')
        driver = webdriver.Firefox()
        driver.get(WEBSITE)
        return driver
    except WebDriverException as e:
        print(f"Error initializing Firefox driver: {e}")
        # You can add additional error handling or log the error here
        return 


def get_info(driver):
    current_url = driver.current_url
    print(f"Getting info from ... {current_url}")
    print(f"Searching for ... {SEARCH_FOR}")

    WebDriverWait(driver,WAIT_TIME_SECONDS).until(EC.visibility_of_element_located((By.ID, SEARCH_BOX)))

    #WebDriverWait(driver,WAIT_TIME_SECONDS).until(EC.visibility_of_element_located((By.XPATH,'//span[@id="twotabsearchtextbox"]')))
    search = driver.find_element(by=By.ID, value=SEARCH_BOX)
    #submit = driver.find_element(by=By.ID, value=SUBMIT_BUTTON)

    search.send_keys(SEARCH_FOR + Keys.RETURN)
    #submit.click()

    driver.implicitly_wait(WAIT_TIME_SECONDS)

    # Find the span element containing the text "Results"
    results_span = driver.find_element('xpath', '//span[text()="Results"]')

    # Use assert to check if the span element is present on the page
    assert results_span, "Text 'Results' not found on the page."


    # Now using find_elements we can search for divs that has specific class value
    # and inside that class, it has span value.
    descriptions = driver.find_elements(By.XPATH,"//div[contains(@class,'s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16')]//span[@class='a-size-medium a-color-base a-text-normal']")
    prices_whole = driver.find_elements(By.XPATH,"//div[contains(@class,'s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16')]//span[@class='a-price-whole']")
    prices_fraction = driver.find_elements(By.XPATH,"//div[contains(@class,'s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16')]//span[@class='a-price-fraction']")

    for i in range(1, 5):
        print(f"{i}st product in results list:")
        print("Description:", descriptions[i - 1].text)  # Adjust index for 0-based list
        print("Price:", prices_whole[i - 1].text + "." + prices_fraction[i - 1].text)
        print()

    time.sleep(5)
    return 
    # Locate the first search result and click on it
    first_result = driver.find_element(By.CSS_SELECTOR, "div.s-main-slot h2 span")


    # Print the product description
    print("First product in results list:")
    print("Description:", first_result.text)

    price = first_result.find_element(By.CSS_SELECTOR,"span.a-price.a-text-price.a-size-medium span.a-offscreen").get_attribute("innerText")

    # Locate the price element within the first result
    #price_whole = first_result.find_element(By.XPATH, ".//span[contains(@class,'a-price-whole')]")
    #price_fraction = first_result.find_element('xpath', "(//span[contains(@class,'a-price-fraction')])")
    #price = price_whole.text + "." + price_fraction.text
    #print("Price:", price)

    # Locate the price element within the first result
    #price_element = first_result.find_element(By.CSS_SELECTOR, "span.a-price-whole")

    # Print the price
    #print("Price:", price_element.text)
    time.sleep(5)
    first_result.click()


    #message = driver.find_element(by=By.ID, value="message")
    #text = message.text
    #print(text)


if __name__ == '__main__':

    driver = get_driver_firefox()
    
    if driver:
        try:
            get_info(driver)
        except Exception as e:
            print(f"Error getting info: {e}")
            # You can add additional error handling or log the error here
        finally:
            quit_driver(driver, "main")
    else:
        quit_driver(driver, "main")
        print("Failed to initialize Firefox driver.")



"""
def get_driver_firefox_service():
    from selenium.webdriver.firefox.service import Service as FirefoxService
    # Specify the path to the GeckoDriver executable
    firefox_driver_path = '/path/to/geckodriver.exe'

    # Create a FirefoxService instance with the executable path
    firefox_service = FirefoxService(executable_path=firefox_driver_path)

    # Create a WebDriver instance using the FirefoxService
    driver = webdriver.Firefox(service=firefox_service)
"""