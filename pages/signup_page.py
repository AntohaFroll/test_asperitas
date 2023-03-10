from .base_page import BasePage
from .locators import SignupPageLocators
from .locators import BasePageLocators


class SignupPage(BasePage):
    url = "https://asperitas.vercel.app/signup"

    def go_to_signup_page(self):
        self.go_to(self.url)

    def enter_valid_date(self, generate_unique_string, generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BTN).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.CREATE_POST_LINK), \
            "Login failed (valid values)!"

    def click_to_signup_btn(self):
        self.driver.find_element(*SignupPageLocators.SIGNUP_BTN).click()

    def should_be_massage_required(self):
        assert self.is_element_present(*SignupPageLocators.MESSAGE_REQUIRED), \
            "Login failed (no value/values)!"

    def enter_invalid_username_and_empty_password_field(self):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys("$#%")
        self.driver.find_element(*SignupPageLocators.SIGNUP_BTN).click()

    def enter_valid_username_and_empty_password_field(self, generate_unique_string):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BTN).click()

    def should_be_message_contains_invalid_characters(self):
        assert self.is_element_present(*SignupPageLocators.MESSAGE_CONTAINS_INVALID_CHARACTERS), \
            "Signup failed (invalid user name)!"

    def enter_valid_username_and_short_password(self, generate_unique_string, generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password[0])
        self.driver.find_element(*SignupPageLocators.SIGNUP_BTN).click()

    def enter_valid_username_password_and_7_signs_confirm_password(self, generate_unique_string,
                                                                   generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password[0:7])
        self.driver.find_element(*SignupPageLocators.SIGNUP_BTN).click()

    def should_be_message_most_be_more_than_8_characters(self):
        assert self.is_element_present(*SignupPageLocators.MESSAGE_MUST_BE_MORE_THAN_8_CHARACTERS), \
            "Signup failed (short password)!"

    def enter_valid_username_password_and_empty_confirm_password_field(self, generate_unique_string,
                                                                       generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BTN).click()

    def enter_valid_username_password_and_invalid_confirm_password_field(self, generate_unique_string,
                                                                         generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BTN).click()

    def should_be_message_password_must_match(self):
        assert self.is_element_present(*SignupPageLocators.MESSAGE_PASSWORD_MUST_MATCH), \
            "Signup failed (password not match)!"
