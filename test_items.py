import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link) 
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button