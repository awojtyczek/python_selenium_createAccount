import random
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from tests.selenium_demo.create_account_page import CreateAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_register_new_user(self):
        my_account_page = CreateAccountPage(self.driver)
        email = self.create_random_email()
        self.register_new_user(my_account_page, email)
        assert self.driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    def test_register_new_user_failed(self):
        my_account_page = CreateAccountPage(self.driver)
        email = self.create_random_email()
        self.register_new_user(my_account_page, email)
        my_account_page.logout()
        self.register_new_user(my_account_page, email)
        error_element_html = "/html/body/div[1]/div/div[2]/div/div/article/div/section/div/div/div[1]/ul/li/strong"
        error_element = self.driver.find_element(By.XPATH, error_element_html)
        assert "ERROR" in error_element.text.upper()

    def test_log_in(self):
        my_account_page = CreateAccountPage(self.driver)
        email = self.create_random_email()
        self.register_new_user(my_account_page, email)
        my_account_page.logout()
        my_account_page.set_current_email_and_password(email, "automatyzacja123")
        assert self.driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    def test_log_in_failed(self):
        my_account_page = CreateAccountPage(self.driver)
        email = self.create_random_email()
        self.register_new_user(my_account_page, email)
        my_account_page.logout()
        my_account_page.set_current_email_and_password(email + "abc", "automatyzacja123")
        error_element_div = "/html/body/div[1]/div/div[2]/div/div/article/div/section/div/div/div[1]"
        error_element = self.driver.find_element(By.XPATH, error_element_div)
        assert "ERROR" in error_element.text

    def test_update_billing_address(self):
        my_account_page = CreateAccountPage(self.driver)
        email = self.create_random_email()
        self.register_new_user(my_account_page, email)

        my_account_page.edit_address()
        my_account_page.change_first_name("Marian")
        my_account_page.change_last_name("Kowal")
        my_account_page.change_company("Auto")
        my_account_page.change_country("Poland")
        my_account_page.change_address("Klonowa", "4")
        my_account_page.change_postcode("00-020")
        my_account_page.change_city("Krakow")
        my_account_page.change_phone("123456432")
        sleep(2)
        my_account_page.submit()
        xpath_komunikatu = "/html/body/div[1]/div/div[2]/div/div/article/div/section/div/div/div/div[2]/div"
        assert "Address changed successfully" in self.driver.find_element(By.XPATH, xpath_komunikatu).text

    def create_random_email(self):
        return str(random.randint(0, 100000)) + "seleniumtesty@example.pl"

    def register_new_user(self, my_account_page, email):
        my_account_page.open_url()
        my_account_page.set_email(email)
        my_account_page.set_password("automatyzacja123")
        my_account_page.click_register_button()
