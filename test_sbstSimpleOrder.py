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
import requests
from selenium.webdriver import ActionChains
from requests.auth import HTTPBasicAuth
from selenium.webdriver import Remote
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.remote import webelement , command
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions


class TestSmoke():


    def test_mainPage(self):
        link = "https://sushibox:hello@ufa.sbstaging.ru/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.set_window_size(1280, 1000)
        driver.get(link)


        #check element are present
        title = driver.title
        assert title == "Дискаунтер «Сушибокс»: доставка суши в Уфе! Закажи суши здесь, а не где-то там ;)", f" current title is {title}"
        factoid = driver.find_element_by_class_name("Factoid__header")
        assert factoid.text == "Почему наши роллы такие дешевые?", "factoid has another text"
        basketBtnPrice = driver.find_element_by_css_selector(".BasketButton__price div")
        assert basketBtnPrice.text == "0", "basketBtnPrice should be 0"
        facebookLink = driver.find_element_by_css_selector(".AppFooter__social:nth-of-type(1)").get_attribute("href")
        assert "https://facebook.com/sushiboxru/" == facebookLink, "no facebook link"
        vkLink = driver.find_element_by_css_selector(".AppFooter__social:nth-of-type(2)").get_attribute("href")
        assert "https://vk.com/sushiboxru/" in vkLink
        instagramLink = driver.find_element_by_css_selector(".AppFooter__social:nth-of-type(3)").get_attribute("href")
        assert str("https://www.instagram.com/sushiboxru/") in instagramLink

        #check rolly
        driver.find_element_by_link_text("Роллы").click()
        time.sleep(1)
        assert "rolly" in driver.current_url, "there is no /rolly/ in URL"
        #assert driver.title == "Роллы в городе Уфа: заказ и доставка. Дискаунтер «СушиБокс» позволит заказать доставку роллов в г. Уфа по выгодным ценам!", f" current title is {title}"
        driver.find_element_by_link_text("Роллы").click()
        driver.find_element_by_class_name("Factoid__header")
        assert driver.current_url == link

        #check sety
        driver.find_element_by_link_text("Сеты").click()
        time.sleep(1)
        assert "sety" in driver.current_url, "there is no /sety/ in URL"
        #assert driver.title == "Сеты в городе Уфа: заказ и доставка. Дискаунтер «СушиБокс» позволит заказать доставку роллов в г. Уфа по выгодным ценам!", f" current title is {title}"
        driver.find_element_by_link_text("Сеты").click()
        driver.find_element_by_class_name("Factoid__header")
        assert driver.current_url == link

        #check dobawky
        driver.find_element_by_link_text("Добавки").click()
        time.sleep(1)
        assert "dobawky" in driver.current_url, "there is no /dobawky/ in URL"
        #assert driver.title == "Добавки в городе Уфа: заказ и доставка. Дискаунтер «СушиБокс» позволит заказать доставку роллов в г. Уфа по выгодным ценам!", f" current title is {title}"
        driver.find_element_by_link_text("Добавки").click()
        driver.find_element_by_class_name("Factoid__header")
        time.sleep(1)
        assert driver.current_url == link

        # add item to basket
        driver.find_element_by_css_selector(".CategoryProductList:nth-of-type(1) .Catalog__categoryItem:nth-of-type(3) .v-btn").click()
        time.sleep(1)
        basketBtnPrice = (driver.find_element_by_css_selector(".BasketButton__price").text).split()[0]
        itemPrice = ((driver.find_element_by_css_selector(".CategoryProductList:nth-of-type(1) .Catalog__categoryItem:nth-of-type(3) .CategoryProductCard__price")).text).split()[0]
        assert basketBtnPrice == itemPrice, print(f" basketBtnPrice should be {itemPrice}")
        driver.find_element_by_css_selector(".CategoryProductList:nth-of-type(1) .Catalog__categoryItem:nth-of-type(3) .v-btn.theme--light:nth-of-type(2)").click()
        time.sleep(1)
        newbasketBtnPrice = (driver.find_element_by_css_selector(".BasketButton__price div").text).split()[0]
        assert int(newbasketBtnPrice) == 2*int(itemPrice), f" basketBtnPrice should be {2*int(itemPrice)}"

        #check pop-up
        driver.find_element_by_css_selector(".CategoryProductList:nth-of-type(1) .Catalog__categoryItem:nth-of-type(3) .CategoryProductCard__image").click()
        time.sleep(1)
        assert driver.find_element_by_css_selector(".CategoryProductCard--modal .CategoryProductCardImage__tagImage").is_displayed(), f"tag not visible"
        assert driver.find_element_by_css_selector(".CategoryProductCard--modal .CategoryProductCardImage__quantity").is_displayed(), f"quantity not visible"
        driver.find_element_by_css_selector(".AppDialog__closeBtn").click()

    def test_Chat(self):
        link = "https://sushibox:hello@ufa.sbstaging.ru/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.set_window_size(1280, 1000)
        driver.get(link)

        driver.find_element_by_css_selector(".AppHeader__phone").click()
        time.sleep(1)
        assert "chat" in driver.current_url, "there is no /chat/ in URL"
        #driver.find_element_by_class_name("ChatButton").click

    def test_DeliveryPage(self):
        link = "https://sushibox:hello@ufa.sbstaging.ru/"
        driver = webdriver.Chrome()
        action = ActionChains(driver)
        driver.implicitly_wait(10)
        driver.set_window_size(1280, 1000)
        driver.get(link)

        driver.find_element_by_link_text("ДОСТАВКА И ОПЛАТА").click()
        time.sleep(2)
        assert "delivery" in driver.current_url, "there is no /delivery/ in URL"
        assert "Доставка и оплата" in driver.find_element_by_tag_name("h1").text, "there os no 'Доставка и оплата' in tag h1"
        assert driver.find_element_by_id("yandexMapsContainer").is_displayed(), "there is no map on delivery page"
        driver.find_element_by_css_selector("[title='Определить ваше местоположение']").click()
        yaPosition = driver.find_element_by_class_name("ymaps-2-1-74-image ")
        time.sleep(1)
        action.move_to_element(yaPosition).move_by_offset(20,20).click().perform()
        deliveryInfo = driver.find_element_by_class_name("ymaps-2-1-74-balloon__content")
        assert deliveryInfo.is_displayed(), "no delivery info"
        mapDeliveryText = driver.find_element_by_css_selector("[class='ymaps-2-1-74-balloon__content'] > ymaps:nth-of-type(1)").text
        assert "Доставка осуществляется только в рамках выделенного района." in mapDeliveryText, "no delivery text on map"
        time.sleep(5)

    def test_FlatPages(self):
        link = "https://sushibox:hello@ufa.sbstaging.ru/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.set_window_size(1280, 1000)
        driver.get(link)

        # check "About" page
        driver.find_element_by_css_selector(".AppHeader__links [href='\/about']").click()
        time.sleep(1)
        assert "about" in driver.current_url, "there is no /about/ in URL"
        assert "О нас" == driver.find_element_by_css_selector(".ContentPage__breadcrumbs span").text, 'There is no "О нас" in breadcrumbs'
        h1Text = driver.find_element_by_css_selector(".content__heading").text
        assert "Почему наши роллы\nтакие дешевые?" == h1Text, "Content text doesn't match"

        # check document pages
        driver.find_element_by_link_text("Правовые документы").click()
        time.sleep(1)
        assert "docs" in driver.current_url, "there is no /docs/ in URL"
        assert "Правовые документы" == driver.find_element_by_css_selector(".ContentPage__breadcrumbs span").text, 'There is no "Правовые документы" in breadcrumbs'
        driver.find_element_by_link_text("Информация для потребителей").click()
        time.sleep(1)
        assert "Информация для потребителей" == driver.find_element_by_css_selector(".ContentPage__breadcrumbs span").text, 'There is no "Информация для потребителей" in breadcrumbs'
        assert "docs/info" in driver.current_url, "there is no /docs/info/ in URL"
        assert "Информация для потребителей" == driver.find_element_by_tag_name("h1").text, "Content doesn't match"
        driver.find_element_by_css_selector(".ContentPage__breadcrumbs [href='\/docs']").click()
        driver.find_element_by_link_text("Политика конфиденциальности").click()
        time.sleep(1)
        assert "Политика конфиденциальности" == driver.find_element_by_css_selector(".ContentPage__breadcrumbs span").text, 'There is no "Политика конфиденциальности" in breadcrumbs'
        assert "docs/confidential" in driver.current_url, "there is no /docs/confidential/ in URL"
        assert "Политика конфиденциальности" == driver.find_element_by_tag_name("h1").text, "Content doesn't match"
        driver.find_element_by_css_selector(".ContentPage__breadcrumbs [href='\/docs']").click()
        driver.find_element_by_link_text("Пользовательское соглашение").click()
        time.sleep(1)
        assert "Пользовательское соглашение" == driver.find_element_by_css_selector(".ContentPage__breadcrumbs span").text, 'There is no "Пользовательское соглашение" in breadcrumbs'
        assert "docs/terms_of_use" in driver.current_url, "there is no /docs/terms_of_use/ in URL"
        assert "Пользовательское соглашение" == driver.find_element_by_tag_name("h1").text, "Content doesn't match"
        driver.find_element_by_css_selector(".ContentPage__breadcrumbs [href='\/docs']").click()
        driver.find_element_by_link_text("Правила продажи").click()
        time.sleep(1)
        assert "Правила продажи" == driver.find_element_by_css_selector(".ContentPage__breadcrumbs span").text, 'There is no "Правила продажи" in breadcrumbs'
        assert "docs/rules" in driver.current_url, "there is no /docs/rules/ in URL"
        assert "Правила продажи" == driver.find_element_by_tag_name("h1").text, "Content doesn't match"
        driver.find_element_by_css_selector(".ContentPage__breadcrumbs [href='\/docs']")

    def test_Basket(self):
        link = "https://sushibox:hello@ufa.sbstaging.ru/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.set_window_size(1280, 1000)
        driver.get(link)

        driver.find_element_by_css_selector(".CategoryProductList:nth-of-type(1) .Catalog__categoryItem:nth-of-type(6) .v-btn").click()
        driver.find_element_by_css_selector(".CategoryProductList:nth-of-type(1) .Catalog__categoryItem:nth-of-type(3) .v-btn").click()
        driver.find_element_by_css_selector(".CategoryProductList:nth-of-type(2) .Catalog__categoryItem:nth-of-type(2) .v-btn").click()
        driver.find_element_by_css_selector(".BasketButton").click()
        time.sleep(1)
        assert "basket" in driver.current_url, "there is no /basket/ in URL"
        basketBtnPrice = int((driver.find_element_by_css_selector(".BasketButton__price").text).split()[0])
        driver.find_element_by_css_selector(".basket__products-list .grid:nth-of-type(1) .count__increase").click()
        firstItemPrice = int((driver.find_element_by_css_selector(".basket__products-list .grid:nth-of-type(1) .ProductListItem__content .ProductListItem__info-price").text).split()[0])
        time.sleep(1)
        newBasketBtnPrice = int((driver.find_element_by_css_selector(".BasketButton__price").text).split()[0])
        totalForItem = int((driver.find_element_by_css_selector(".basket__products-list .grid:nth-of-type(1) .ProductListItem__price").text).split()[0])
        assert totalForItem == int(2*firstItemPrice), "total price for item is not correct"
        assert newBasketBtnPrice == int(basketBtnPrice + firstItemPrice), "total price is not correct"
        driver.find_element_by_css_selector(".basket__products-list .grid:nth-of-type(1) .count__decrease").click()
        time.sleep(1)
        newBasketBtnPrice = int((driver.find_element_by_css_selector(".BasketButton__price").text).split()[0])
        assert newBasketBtnPrice == basketBtnPrice, "total price is not correct"
        driver.find_element_by_css_selector(".basket__products-list .grid:nth-of-type(1) .count__decrease").click()
        quantity = len(driver.find_elements_by_xpath("//*[contains(@class,'ProductListItem grid')]"))
        assert quantity == 2, "incorrect quantity of items"
        driver.find_element_by_css_selector(".basket__products-list .grid:nth-of-type(2) .ProductListItem__close").click()
        driver.find_element_by_css_selector(".basket__clearAllText").click()
        time.sleep(1)
        assert driver.find_element_by_css_selector(".BasketEmpty__image").is_displayed(), "there is no cat with empty basket((("
        driver.find_element_by_css_selector(".AppButton--violet").click()
        time.sleep(1)
        assert driver.current_url == link, "main page doesn't opened"
        driver.find_element_by_css_selector(".CategoryProductList:nth-of-type(1) .Catalog__categoryItem:nth-of-type(3) .v-btn").click()
        driver.find_element_by_css_selector(".BasketButton").click()
        time.sleep(1)
        assert driver.find_element_by_css_selector(".basket__minDeliveryCost").is_displayed(), "there IS NOT min cost massage"
        driver.find_element_by_css_selector(".ProductListItem__count .count__increase").click()
        time.sleep(1)
        assert not driver.find_element_by_css_selector(".basket__minDeliveryCost").is_displayed(), "there IS min cost massage"
        basketBtnPrice = int((driver.find_element_by_css_selector(".BasketButton__price").text).split()[0])
        additives = [1, 2, 3, 4]
        additivesSummary = int(0)
        for i in additives:
            driver.find_element_by_css_selector(f".BasketAdditivesItem:nth-of-type({i}) .count__increase").click()
            additivePrice = (driver.find_element_by_css_selector(f".BasketAdditivesItem:nth-of-type({i}) .BasketAdditivesItem__price").text).split()[0]
            additivesSummary = additivesSummary + int(additivePrice)
        time.sleep(1)
        additivesTotal = (driver.find_element_by_css_selector(".BasketAdditives__header span").text).split()[0]
        newBasketBtnPrice = int((driver.find_element_by_css_selector(".BasketButton__price").text).split()[0])
        assert additivesSummary == int(additivesTotal)
        assert newBasketBtnPrice == int(int(basketBtnPrice) + int(additivesTotal))
        # client info
        driver.find_element_by_css_selector("[aria-label='Номер телефона \*']").click()
        driver.find_element_by_css_selector("[aria-label='Номер телефона \*']").send_keys("6666666666")
        driver.find_element_by_css_selector("[aria-label='Имя \*']").click()
        driver.find_element_by_css_selector("[aria-label='Имя \*']").send_keys('Василиса')
        driver.find_element_by_css_selector("[aria-label='Укажите улицу \*']").click()
        driver.find_element_by_css_selector("[aria-label='Укажите улицу \*']").send_keys("Комму")
        time.sleep(1)
        streets = range(1, 10)
        for i in streets:
            if "нистическая" in driver.find_element_by_css_selector(f"#app div:nth-of-type(3) [role='listitem']:nth-of-type({i}) .v-list__tile__title").text:
                rightStreet = i
                driver.find_element_by_css_selector(f"#app div:nth-of-type(3) [role='listitem']:nth-of-type({rightStreet}) .v-list__tile__title").click()
                break
        driver.find_element_by_css_selector("[aria-label='Дом \*']").click()
        driver.find_element_by_css_selector("[aria-label='Дом \*']").send_keys("1")
        driver.find_element_by_css_selector("[aria-label='Квартира\/Офис']").click()
        driver.find_element_by_css_selector("[aria-label='Квартира\/Офис']").send_keys("2")
        driver.find_element_by_css_selector("[aria-label='Подъезд']").click()
        driver.find_element_by_css_selector("[aria-label='Подъезд']").send_keys("3")
        driver.find_element_by_css_selector("[aria-label='Этаж']").click()
        driver.find_element_by_css_selector("[aria-label='Этаж']").send_keys("4")
        #dleivery and payment
        driver.find_element_by_css_selector(".checkout__deliveryAtTime > div:nth-of-type(1) .v-label").click()
        driver.find_element_by_css_selector("[role='combobox']:nth-of-type(2) .material-icons").click()
        driver.find_element_by_css_selector("#app div:nth-of-type(2) [role='listitem']:nth-of-type(2)").click()
        driver.find_element_by_css_selector("[role='combobox']:nth-of-type(3) .material-icons").click()
        driver.find_element_by_css_selector("#app > div:nth-of-type(1) [role='listitem']:nth-of-type(5)").click()
        driver.find_element_by_css_selector("[aria-label='Картой курьеру']").is_selected()
        driver.find_element_by_css_selector("[aria-label='Наличными']").is_selected()
        driver.find_element_by_css_selector("[aria-label='Наличными']").send_keys("2000")
        #comment and confirm
        driver.find_element_by_css_selector("textarea").click()
        driver.find_element_by_css_selector("textarea").send_keys("Автотестовый комментарий")
        driver.find_element_by_css_selector(".CheckoutConfirmButton__appButton").click()
        driver.find_element_by_css_selector("[aria-label='Код \*']").click()
        driver.find_element_by_css_selector("[aria-label='Код \*']").send_keys("0000")
        time.sleep(5)
        #check order page

    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    pytest.main()
