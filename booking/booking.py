import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const
from booking.Booking_Filters import BookingFilters


#  class the represents a webdriver that handles the booking.com main page
class Booking(webdriver.Chrome):
    def __init__(self, path=const.DRIVER_PATH, option=const.OPTION):
        self.driver_path = path
        self.service = Service(executable_path=path)
        self.option = option  # setup option for Brave
        self.wait = WebDriverWait(self, const.WAIT_TIME)
        super(Booking, self).__init__(service=self.service, options=option)
        self.implicitly_wait(const.WAIT_TIME)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    # opens the landing page
    def landing_page(self):
        self.get(const.URL)

    # accepts cookies
    def accept_cookies(self):
        try:
            accept_button = self.find_element(By.ID, 'onetrust-accept-btn-handler')
            accept_button.click()
        except:
            pass

    # changes the currency
    # need to fix
    def change_currency(self, currency='USD'):
        currency_element = self.find_element(By.CSS_SELECTOR, '#b2indexPage > header > nav.bui-header__bar > div.bui-group.bui-button-group.bui-group--inline.bui-group--align-end.bui-group--vertical-align-middle > div:nth-child(1) > button')
        currency_element.click()
        # data-modal-header-async-url-param
        selected_currency_element = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="changed_currency=1&selected_currency={currency}"]')
        selected_currency_element.click()

    # changes the website language
    def change_language(self, language='en-us'):
        language_element = self.find_element(By.CSS_SELECTOR,
                                             "#b2indexPage > header > nav.bui-header__bar > div.bui-group.bui-button-group.bui-group--inline.bui-group--align-end.bui-group--vertical-align-middle > div:nth-child(2) > button")
        language_element.click()

        change_language_element = self.find_element(By.CSS_SELECTOR, f'div[lang={language}]')
        change_language_element.click()

    # chooses the destination
    def place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)

    #  chooses and sets the check in and check out dates
    def dates(self, check_in_date=None, check_out_date=None):
        dates_box_element = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        '//*[@id="frm"]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/span'))
                                            )
        self.wait.until(
            EC.element_to_be_clickable(dates_box_element)
        )

        time.sleep(2)  # explicit wait doesn't work - need to figure it out
        dates_box_element.click()

        # booking shows only current and next month
        check_in_month = int(check_in_date[5:7])
        for _ in range(int((check_in_month - int(time.localtime().tm_mon)) / 2)):
            self.next_calender_page()

        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def next_calender_page(self):
        next_button_element = self.find_element(By.CSS_SELECTOR, 'div[data-bui-ref="calendar-next"]')
        next_button_element.click()

    # need to finish
    def select_adults(self, num_of_adults):
        if num_of_adults > const.DEFAULT_AMOUNT_OF_ADULTS:

            adults_button_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
            time.sleep(2)  # explicit wait doesn't work - need to figure it out
            adults_button_element.click()

            plus_one_adult_button = self.find_element(By.CSS_SELECTOR, 'svg[xmlns="http://www.w3.org/2000/svg"]')
            for _ in range(num_of_adults - const.DEFAULT_AMOUNT_OF_ADULTS):
                plus_one_adult_button.click()

    #  clicks the submit button
    def submit(self):
        submit_button_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        submit_button_element.click()

    #  closes the "sign in" window
    def close_sign_in_window(self):
        try:
            x_button_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            x_button_element.click()
        except:
            pass

    #  calls all the filtering methods
    def apply_filters(self):
        booking_filters = BookingFilters(driver=self)
        booking_filters.sort_by_lowest_price_first()
        booking_filters.choose_reviews(min_review_score=8)
        booking_filters.choose_stars(min_stars=4)
        booking_filters.bed_prefrence()
        #  booking_filters.distance_from_center(max_distance=5)
