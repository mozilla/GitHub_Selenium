# -*- coding: utf-8 -*-

"""Top-level package for GitHub Selenium."""

__author__ = """Hal Wine"""
__email__ = 'hwine@mozilla.com'
__version__ = '0.1.0'


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)

WebDriverException


class GitHub2FA(object):

    def __init__(self, implicit_wait=5):
        # force headless mode
        # TODO make option
        os.environ['MOZ_HEADLESS'] = "1"
        driver = webdriver.Firefox()
        driver.wait = WebDriverWait(driver, implicit_wait)
        self.driver = driver

    def get_element(self, name_or_id):
        element = None
        e = None
        for method in By.NAME, By.ID, By.CSS_SELECTOR:
            try:
                element = self.driver.find_element(method, name_or_id)
                break
            except NoSuchElementException:
                pass
            except Exception as e:
                print("got {} for {}".format(repr(e), name_or_id))
        return element

    def fill_field(self, name_or_id, text_to_send, submit=False):
        element = self.get_element(name_or_id)
        element.send_keys(text_to_send)
        if submit:
            element.submit()

    def click_button(self, name_or_id):
        element = self.get_element(name_or_id)
        element.click()

    def wait_for_page(self, title_text):
        try:
            self.driver.wait.until(EC.title_contains(title_text))
        except TimeoutException:
            raise ValueError("Didn't arrive on {} page"
                             .format(title_text.encode('UTF-8')))

    def login(self, login, password, destination_page_url,
              destination_page_title, token):
        self.driver.get(destination_page_url)
        self.wait_for_page("Sign in")
        self.fill_field('login', login)
        self.fill_field('password', password)
        self.click_button('commit')
        # put in token
        self.wait_for_page("Where software is built")
        self.fill_field('otp', token, submit=True)
        # we have to wait for the page to refresh, the last thing that
        # seems to be updated is the title
        self.wait_for_page(destination_page_title)

    def quit(self):
        self.driver.quit()
