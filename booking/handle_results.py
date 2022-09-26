#  This file has methods and classes that handle the resluts of the search
import time

from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Results:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def handle_results(self, max_price=200):
        results = []
        results_table = self.driver.find_element(By.CSS_SELECTOR, 'div[class="d4924c9e74"]')
        results_sub_elements = results_table.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        print(len(results_sub_elements))  # to delete
        for element in results_sub_elements:
            price_of_element = element.find_element(By.CSS_SELECTOR,
                                                    'div[data-testid="price-and-discounted-price"] > span[class="fcab3ed991 bd73d13072"]'
                                                    )
            price = ''
            for c in price_of_element.get_attribute('innerHTML'):
                if c.isdigit():
                    price += c
            if price and int(price) <= max_price:
                name = self.get_hotel_name(element)
                url = self.get_url(element)
                results.append(f'{name}\n{price}€\n<a href="{url}">link</a>')
        return results

    def get_hotel_name(self, element: WebElement):
        name_element = element.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]')
        return name_element.get_attribute('innerHTML')

    def get_url(self, element: WebElement):
        URL_element = element.find_element(By.CSS_SELECTOR, 'div[data-testid="availability-cta"]>a')
        return URL_element.get_attribute('href')
