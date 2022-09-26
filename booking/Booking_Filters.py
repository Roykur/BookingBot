# This file includes a class with instance methods

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# A class that includes methods to manage the filter of the booking search engine
class BookingFilters:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # sets the stars filter
    # stars[] - list of ints that represent the amount of stars
    def choose_stars(self, min_stars=4):
        #stars = self.driver.find_element(By.CSS_SELECTOR, f'span{const.CLASS_NAMES_DICT[f"{num_of_stars}stars"]}')
        stars_table_element = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        stars_sub_elements = stars_table_element.find_elements(By.CSS_SELECTOR, '*')

        for star in range(min_stars, 6):
            for element in stars_sub_elements:
                if str(element.get_attribute('innerHTML')).strip() == f'{star} stars':
                    element.click()

    def sort_by_lowest_price_first(self):
        sort_by_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-selected-sorter="popularity"]')
        sort_by_element.click()

        lowest_price_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        lowest_price_element.click()


    def choose_reviews(self, min_review_score=8):
        reviews_table_element = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="review_score"]')
        reviews_sub_elements = reviews_table_element.find_elements(By.CSS_SELECTOR, '*')


        for element in reviews_sub_elements:
            if str(element.get_attribute('innerHTML')).strip()[-2:] == f'{min_review_score}+':
                self.driver.wait.until(EC.visibility_of(element))
                element.click()
                break


    def bed_prefrence(self, prefrence = 'Double bed'):
        bed_pref_table_element = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="tdb"]')
        bed_pref_sub_elements = bed_pref_table_element.find_elements(By.CSS_SELECTOR, '*')


        for element in bed_pref_sub_elements:
            if str(element.get_attribute('innerHTML')).strip() == prefrence:
                self.driver.wait.until(EC.visibility_of(element))
                element.click()
                break


    def distance_from_center(self, max_distance=3):
        distance_table_element = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="distance"]')
        distance_sub_elements = distance_table_element.find_elements(By.CSS_SELECTOR, '*')

        for element in distance_sub_elements:
            if str(element.get_attribute('innerHTML')).strip() == f'Less than {max_distance} km':
                #self.driver.wait.until(EC.visibility_of(element))
                element.click()
                break
