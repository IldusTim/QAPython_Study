# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import math
from selenium.webdriver.support.ui import Select
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestSimpleOorder():
    #def setUp(self)
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(5)
        #self.verificationErrors = []
        #self.accept_next_alert = True
    def test_login(self):
        link = "https://ufa.sbstaging.ru/"
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        driver = webdriver.Chrome(chrome_options=opt)
        driver.implicitly_wait(5)
        driver.get(link)
        prompt = driver.switch_to.alert
        prompt.send_keys("sushibox")
        prompt.send_keys(keys)
        prompt.accept()

    def test_sbstOrder(self):
        driver.find_element_by_css_selector(".BasketButton").click()
        driver.find_element_by_css_selector(".AppButton--violet .v-btn__content").click()
        # driver.find_element_by_link_text("Сеты").click()
        # driver.find_element_by_link_text("Сеты").click()
        # driver.find_element_by_link_text("Роллы").click()
        # driver.find_element_by_link_text("Роллы").click()
        # driver.find_element_by_link_text("Добавки").click()
        # driver.find_element_by_link_text("Добавки").click()
        # driver.find_element_by_link_text("Сеты").click()
        # driver.find_element_by_css_selector("#app > div.application--wrap > main > div > div > div.page__wrapper > div.page__content > div.mainLayout > div.main.Category.Catalog > div > div > div > div:nth-child(3) > div > div.flex.CategoryProductCard__content > div.layout.justify-space-between.mb-3 > div.CategoryProductCard__basket-controls > button").click()
        # driver.find_element_by_css_selector(".BasketButton").click()
        # driver.find_element_by_css_selector("#app > div.application--wrap > main > div > div > div.page__wrapper > div.page__content > div.mainLayout.basketPage > div > div > div > div.basket__products-list > div > div.ProductListItem__count > div > button:nth-child(3)").click()
        # driver.find_element_by_css_selector("#app > div.application--wrap > main > div > div > div.page__wrapper > div.page__content > div.mainLayout.basketPage > div > div > div > div.BasketAdditives > div.BasketAdditives__content.grid > div.observer-wrapper > div > div:nth-child(1) > div.BasketAdditivesItem__count > div > button:nth-child(3)").click()
        # driver.find_element_by_css_selector("#app > div.application--wrap > main > div > div > div.page__wrapper > div.page__content > div.mainLayout.basketPage > div > div > div > div.BasketAdditives > div.BasketAdditives__content.grid > div.observer-wrapper > div > div:nth-child(2) > div.BasketAdditivesItem__count > div > button:nth-child(3)").click()
        # driver.find_element_by_css_selector("#app > div.application--wrap > main > div > div > div.page__wrapper > div.page__content > div.mainLayout.basketPage > div > div > div > div.BasketAdditives > div.BasketAdditives__content.grid > div.observer-wrapper > div > div:nth-child(3) > div.BasketAdditivesItem__count > div > button:nth-child(3)").click()
        # driver.find_element_by_css_selector("#app > div.application--wrap > main > div > div > div.page__wrapper > div.page__content > div.mainLayout.basketPage > div > div > div > div.BasketAdditives > div.BasketAdditives__content.grid > div.observer-wrapper > div > div:nth-child(4) > div.BasketAdditivesItem__count > div > button:nth-child(3)").click()
        # driver.find_element_by_name("phone").click()
        # driver.find_element_by_name("phone").clear()
        # driver.find_element_by_name("phone").send_keys("9174706960")
        # driver.find_element_by_name("name").click()
        # driver.find_element_by_name("name").clear()
        # driver.find_element_by_name("name").send_keys("Ильдус")
        # driver.find_element_by_name("street").clear()
        # driver.find_element_by_name("street").send_keys("Свердлова")
        # driver.find_element_by_css_selector("#app > div.v-menu__content.theme--light.menuable__content__active.v-autocomplete__content > div > div > div > a > div > div > span").click()
        # driver.find_element_by_name("house").click()
        # driver.find_element_by_name("house").send_keys("10")
        # driver.find_element_by_css_selector("[aria-label='Квартира\/Офис']").click()
        # driver.find_element_by_css_selector("[aria-label='Квартира\/Офис']").send_keys("1")
        # driver.find_element_by_css_selector("[aria-label='Подъезд']").click()
        # driver.find_element_by_css_selector("[aria-label='Подъезд']").send_keys("2")
        # driver.find_element_by_css_selector("[aria-label='Этаж']").click()
        # driver.find_element_by_css_selector("[aria-label='Этаж']").send_keys("3")
        # driver.find_element_by_css_selector(".checkoutAtTime__checkbox .v-label").click()
        # driver.find_element_by_css_selector("[class='v-input--selection-controls__ripple orange--text text--darken-2']").click()
        # driver.find_element_by_css_selector("textarea").click()
        # driver.find_element_by_css_selector("textarea").send_keys("Автотестовый комментарий")
        # driver.find_element_by_css_selector(".CheckoutConfirmButton__appButton .v-btn__content").click()
        # driver.find_element_by_name("code").click()
        # driver.find_element_by_name("code").send_keys("0000")

        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Стоимость доставки 100­₽'])[1]/following::label[5]").click()
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Стоимость доставки 100­₽'])[1]/following::textarea[1]").click()
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Стоимость доставки 100­₽'])[1]/following::textarea[1]").clear()
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Стоимость доставки 100­₽'])[1]/following::textarea[1]").send_keys(u"Тестовый комментарий!")
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Стоимость доставки 100­₽'])[1]/following::div[65]").click()
        # driver.find_element_by_name("code").click()
        # driver.find_element_by_name("code").clear()
        # driver.find_element_by_name("code").send_keys("0000")
        # driver.find_element_by_css_selector("svg.AppHeader__orders").click()
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Мои заказы'])[3]/following::div[3]").click()
    
    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    pytest.main()
