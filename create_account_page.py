from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://seleniumdemo.com/?page_id=7"
        self.current_email_id = "username"
        self.current_password_id = "password"
        self.email_id = "reg_email"
        self.password_id = "reg_password"
        self.button_register = "register"
        self.address_link = "Addresses"
        self.edit_link = "Edit"
        self.first_name_id = "billing_first_name"
        self.last_name_id = "billing_last_name"
        self.company_id = "billing_company"
        self.country_id = "billing_country"
        self.address_1_id = "billing_address_1"
        self.address_2_id = "billing_address_2"
        self.postcode_id = "billing_postcode"
        self.city_id = "billing_city"
        self.phone_id = "billing_phone"
        self.save_id = "save_address"
        self.xpath_komunikatu = "/html/body/div[1]/div/div[2]/div/div/article/div/section/div/div/div/div[2]/div"

    def open_url(self):
        self.driver.get(self.url)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def set_password(self, haslo):
        self.driver.find_element(By.ID, self.password_id).send_keys(haslo)

    def click_register_button(self):
        self.driver.find_element(By.NAME, self.button_register).send_keys(Keys.ENTER)

    def edit_address(self):
        self.driver.find_element(By.LINK_TEXT, self.address_link).click()
        self.driver.find_element(By.LINK_TEXT, self.edit_link).click()

    def change_first_name(self, imie):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(imie)

    def change_last_name(self, nazwisko):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(nazwisko)

    def change_company(self, firma):
        self.driver.find_element(By.ID, self.company_id).send_keys(firma)

    def change_country(self, kraj):
        element = self.driver.find_element(By.ID, self.country_id)
        select = Select(element)
        select.select_by_visible_text(kraj)

    def change_address(self, address1, address2):
        self.driver.find_element(By.ID, self.address_1_id).send_keys(address1)
        self.driver.find_element(By.ID, self.address_2_id).send_keys(address2)

    def change_postcode(self, kod_pocztowy):
        self.driver.find_element(By.ID, self.postcode_id).send_keys(kod_pocztowy)

    def change_city(self, miasto):
        self.driver.find_element(By.ID, self.city_id).send_keys(miasto)

    def change_phone(self, telefon):
        self.driver.find_element(By.ID, self.phone_id).send_keys(telefon)

    def submit(self):
        self.driver.find_element(By.NAME, self.save_id).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def set_current_email_and_password(self, email, password):
        self.driver.find_element(By.ID,self.current_email_id).send_keys(email)
        self.driver.find_element(By.ID, self.current_password_id).send_keys(password)
        self.driver.find_element(By.NAME, "login").click()