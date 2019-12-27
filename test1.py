# -*- coding: utf-8 -*-
from selenium import webdriver
import math
import time
import pytest
import unittest

class TesteReg(unittest.TestCase):
    def test_TestReg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
        input1.send_keys("Ivan")
        input1 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
        input1.send_keys("Petrov")
        input2 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
        input2.send_keys("Petrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_TestReg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
        input1.send_keys("Ivan")
        input1 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
        input1.send_keys("Petrov")
        input2 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
        input2.send_keys("Petrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

if __name__ == "__main__":
    pytest.main()