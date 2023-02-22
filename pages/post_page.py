import time
from .base_page import BasePage
from .locators import PostPageLocators
from .locators import BasePageLocators


class PostPage(BasePage):
    def create_text_post(self, generate_unique_string):
        self.driver.implicitly_wait(5)
        self.is_element_to_be_clickable(*PostPageLocators.TEXT_RADIOBUTTON)
        time.sleep(3)
        self.driver.find_element(*PostPageLocators.TEXT_RADIOBUTTON).click()
        self.driver.find_element(*PostPageLocators.CATEGORY_SELECTOR).click()
        self.driver.find_element(*PostPageLocators.PROGRAMMING_CATEGORY).click()
        self.driver.find_element(*PostPageLocators.TITLE_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*PostPageLocators.TEXT_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*PostPageLocators.CREATE_POST_BUTTON).click()

    def create_url_post(self, generate_unique_string, generate_url):
        self.driver.implicitly_wait(5)
        self.is_element_to_be_clickable(*PostPageLocators.URL_RADIOBUTTON)
        time.sleep(3)
        self.driver.find_element(*PostPageLocators.URL_RADIOBUTTON).click()
        self.driver.find_element(*PostPageLocators.CATEGORY_SELECTOR).click()
        self.driver.find_element(*PostPageLocators.PROGRAMMING_CATEGORY).click()
        self.driver.find_element(*PostPageLocators.TITLE_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*PostPageLocators.URL_FIELD).send_keys(generate_url)
        self.driver.find_element(*PostPageLocators.CREATE_POST_BUTTON).click()

    def should_be_post_created(self):
        assert self.is_element_present(*PostPageLocators.TITLE_POST), "Post not created!"

    def delete_post(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*BasePageLocators.USERNAME_LINK).click()
        self.driver.find_element(*PostPageLocators.TITLE_POST_TEXT).click()
        self.driver.find_element(*PostPageLocators.DELETE_BUTTON).click()

    def should_be_post_deleted(self):
        assert self.is_element_present(*PostPageLocators.EMPTY_POST_LIST_LABEL), "Post not deleted!"

    def create_comment(self, generate_unique_string):
        self.is_element_present(*PostPageLocators.COMMENT_COUNTER)
        self.driver.find_elements(*PostPageLocators.COMMENT_COUNTER)[0].click()
        self.is_element_present(*PostPageLocators.COMMENT_TEXT_FIELD)
        self.driver.find_element(*PostPageLocators.COMMENT_TEXT_FIELD).send_keys(generate_unique_string)
        self.is_element_present(*PostPageLocators.SUBMIT_BUTTON)
        self.driver.find_element(*PostPageLocators.SUBMIT_BUTTON).click()

    def should_be_comment_created(self):
        assert self.is_element_present(*PostPageLocators.DELETE_BUTTON), "Comment not created!"

    def delete_comment(self):
        time.sleep(3)
        self.driver.find_element(*PostPageLocators.DELETE_BUTTON).click()

    def should_be_comment_deleted(self):
        assert self.is_element_disappeared(*PostPageLocators.DELETE_BUTTON), "Comment not deleted!"
