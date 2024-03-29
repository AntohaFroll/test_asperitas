import time
from .base_page import BasePage
from .locators import PostPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By


class PostPage(BasePage):
    url = "https://asperitas.vercel.app/createpost"

    def go_to_create_post_page(self):
        self.go_to(self.url)

    def create_text_post(self, generate_unique_string):
        self.is_element_to_be_clickable(*PostPageLocators.TEXT_RADIOBTN)
        time.sleep(3)
        self.driver.find_element(*PostPageLocators.TEXT_RADIOBTN).click()
        self.driver.find_element(*PostPageLocators.CATEGORY_SELECTOR).click()
        self.driver.find_element(*PostPageLocators.PROGRAMMING_CATEGORY).click()
        self.driver.find_element(*PostPageLocators.TITLE_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*PostPageLocators.TEXT_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*PostPageLocators.CREATE_POST_BTN).click()

    def create_url_post(self, generate_unique_string, generate_url):
        self.is_element_to_be_clickable(*PostPageLocators.URL_RADIOBTN)
        time.sleep(3)
        self.driver.find_element(*PostPageLocators.URL_RADIOBTN).click()
        self.driver.find_element(*PostPageLocators.CATEGORY_SELECTOR).click()
        self.driver.find_element(*PostPageLocators.PROGRAMMING_CATEGORY).click()
        self.driver.find_element(*PostPageLocators.TITLE_FIELD).send_keys(generate_unique_string)
        self.driver.find_element(*PostPageLocators.URL_FIELD).send_keys(generate_url)
        self.driver.find_element(*PostPageLocators.CREATE_POST_BTN).click()

    def should_be_post_created(self):
        assert self.is_element_present(*PostPageLocators.TITLE_POST), "Post not created!"

    def delete_post(self, post):
        self.driver.find_element(*BasePageLocators.USERNAME_LINK).click()
        self.is_element_present(By.XPATH, f"//a[text()='{post.title}']")
        self.driver.find_element(By.XPATH, f"//a[text()='{post.title}']").click()
        self.is_element_present(*PostPageLocators.DELETE_BTN)
        self.driver.find_element(*PostPageLocators.DELETE_BTN).click()

    def should_be_post_deleted(self):
        assert self.is_element_present(*PostPageLocators.EMPTY_POST_LIST_LABEL), "Post not deleted!"

    def create_comment(self, generate_unique_string):
        time.sleep(3)
        self.is_element_present(*PostPageLocators.COMMENT_COUNTER)
        self.driver.find_elements(*PostPageLocators.COMMENT_COUNTER)[0].click()
        self.is_element_present(*PostPageLocators.COMMENT_TEXT_FIELD)
        self.driver.find_element(*PostPageLocators.COMMENT_TEXT_FIELD).send_keys(generate_unique_string)
        self.is_element_present(*PostPageLocators.SUBMIT_BTN)
        self.driver.find_element(*PostPageLocators.SUBMIT_BTN).click()

    def should_be_comment_created(self):
        assert self.is_element_present(*PostPageLocators.DELETE_BTN), "Comment not created!"

    def delete_comment(self, post, comment):
        self.driver.find_element(*BasePageLocators.USERNAME_LINK).click()
        self.is_element_present(By.XPATH, f"//a[text()='{post.title}']")
        self.driver.find_element(By.XPATH, f"//a[text()='{post.title}']").click()
        self.is_element_present(By.XPATH, f"//a[@href='/u/{comment.username}']/following-sibling::button")
        self.driver.find_element(By.XPATH, f"//a[@href='/u/{comment.username}']/following-sibling::button").click()

    def should_be_comment_deleted(self, comment):
        assert self.is_element_present(By.XPATH, "//div[text()='no comments']"), "Comment not deleted!"
