# -*- coding: utf-8 -*-

"""Top-level package for GitHub Selenium."""

__author__ = """Hal Wine"""
__email__ = 'hwine@mozilla.com'
__version__ = '0.2.0'


import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (  # noqa: F401,W0611
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)

logger = logging.getLogger(__name__)


class GitHub2FA(object):

    def __init__(self, implicit_wait=5, headless=True, **kwargs):
        # set headless mode
        if headless:
            os.environ['MOZ_HEADLESS'] = "1"
        driver = webdriver.Firefox(**kwargs)
        driver.wait = WebDriverWait(driver, implicit_wait)
        self.driver = driver

    def get_element(self, name_or_id):
        element = None
        for method in By.NAME, By.ID, By.CSS_SELECTOR:
            try:
                element = self.driver.find_element(method, name_or_id)
                break
            except NoSuchElementException:
                pass
            except Exception as e:
                logger.debug("got {} for {}".format(repr(e), name_or_id))
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
            logger.debug("Got to: {}".format(title_text))
        except TimeoutException:
            logger.debug("Did NOT get to: {}".format(title_text))
            raise ValueError("Didn't arrive on {} page"
                             .format(title_text.encode('UTF-8')))

    def login(self, login, password, destination_page_url,
              destination_page_title, token):
        self.driver.get("https://github.com/login")
        try:
            self.wait_for_page("Sign in")
            self.fill_field('login', login)
            self.fill_field('password', password)
            self.click_button('commit')
            # put in token
            self.wait_for_page("Where software is built")
            self.fill_field('otp', token, submit=True)
            # we have to wait for the page to refresh, the last thing that
            # seems to be updated is the title
            self.wait_for_page("Github")
        except ValueError as e:
            if "GitHub" not in self.driver.title:
                # didn't get to post login page
                logger.debug("Didn't get to {}".format(destination_page_url))
                logger.debug("latest title '{}'".format(self.driver.title))
                raise e
        self.driver.get(destination_page_url)
        self.wait_for_page(destination_page_title)

    def quit(self):
        self.driver.quit()
