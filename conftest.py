import pytest
from selenium import webdriver
import requests
import uuid
from entities.user import User

reg_url = "https://asperitas.vercel.app/api/register"
post_url = "https://asperitas.vercel.app/api/posts"


@pytest.fixture
def driver():
    print("\nstart browser for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser")
    driver.quit()


@pytest.fixture
def new_user():
    print("\ncreating user")
    username = uuid.uuid4().__str__().split("-")[-1]
    password = uuid.uuid4().__str__().split("-")[-1]
    data = {"username": username, "password": password}
    create_user_response = requests.post(reg_url, json=data)
    assert create_user_response.json()["token"] != "", "User not create"
    return User(username, password)


@pytest.fixture
def new_post():
    unique_string = uuid.uuid4().__str__().split("-")[-1]
    data = {"category": "music", "type": "text", "title": unique_string, "text": unique_string}
    create_post_response = requests.post(post_url, json=data)
    assert create_post_response.json() != "", "Post not create"


@pytest.fixture
def generate_unique_string():
    unique_string = uuid.uuid4().__str__().split("-")[-1]
    return unique_string


@pytest.fixture
def generate_url():
    unique_url = f"http://{uuid.uuid4().__str__().split('-')[-1]}.com"
    return unique_url


@pytest.fixture
def generate_password():
    password = uuid.uuid1().__str__().split("-")[-1]
    return password


# @pytest.fixture
# def user_authorized():
#     print("\ncreating and authorization user")
#
#     username = uuid.uuid4().__str__().split("-")[-1]
#     password = uuid.uuid4().__str__().split("-")[-1]
#
#     reg_url = "https://asperitas.vercel.app/api/register"
#     auth_url = "https://asperitas.vercel.app/api/login"
#     data = {"username": username, "password": password}
#
#     create_user_response = requests.post(reg_url, json=data)
#
#     assert create_user_response.json()["token"] != "", "User not created!"
#
#     authorization_user_response = requests.post(auth_url, json=data)
#
#     assert authorization_user_response.json()["token"] != "", "User not authorized!"
#
#     return UserAuthorized(username, password)
