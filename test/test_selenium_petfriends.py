import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_quantum_my_pets():
    #time.sleep(2)

    #забираем массив текста логин, питомцев, друзья и сообщения
    #all_text = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]')
    all_text = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
    all_text_str = all_text.text
    pets_index = all_text_str.find('Питомцев')
    friends_index = all_text_str.find('Друзей')
    number_pets = all_text_str[pets_index +10:friends_index].replace(' ', '')

    # забираем массив с именами всех питомцев
    #my_pets = pytest.driver.find_element_by_xpath('//tbody')
    my_pets = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//tbody')))
    my_pets_name = my_pets.text
    count_my_pets = 0
    for i in my_pets_name:
        if i == '×':
            count_my_pets += 1


    #проверяем соответсвие количества питомцев и количество крестиков
    assert count_my_pets == int(number_pets)


def test_have_half_photo_pets():

    images = pytest.driver.find_elements_by_css_selector('div th > img')
    images = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div th > img')))
    count = 0
    # проходим циклом по массиву фотографий, считаем количество фото i
    for i in range(len(images)):
        if 'base64' in images[i].get_attribute('src'):
            count += 1
     #ставим условие по количеству в зависимости от того, четное или нечетное число фотографий
    if (len(images) % 2) == 0:
        assert count >= (len(images) / 2), 'Фото присутствует менее чем у половины питомцев'


def test_age_clas_name():
    pytest.driver.implicitly_wait(5)
    #локаторы с именем возрастом и породой
    #all_text = pytest.driver.find_elements_by_css_selector('div td')
    all_text = pytest.driver.find_elements_by_xpath('//tr/td')
    name = all_text[::4]
    age = all_text[2::4]
    clas = all_text[1::4]

    assert '' not in name, "нет у кого то имени"
    assert '' not in age, "нет у кого то возраста"
    assert '' not in clas, "нет у кого то породы"

def test_diff_names():
    #all_text = pytest.driver.find_elements_by_xpath('//tr/td')
    all_text = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//tr/td')))
    name = all_text[::4]

    assert len(name) == len(set(list(name))), 'Есть одинаковые имена'


def test_diff_pets():
    #pytest.driver.implicitly_wait(5)
    #локаторы с именем возрастом и породой, заводим переменные с массивами данных
    #all_text = pytest.driver.find_elements_by_xpath('//tr/td')
    all_text = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//tr/td')))
    name = all_text[::4]
    age = all_text[2::4]
    clas = all_text[1::4]

    #если во всех трех параметрах нет одинаковых значений, значит одинаковых животных нет
    assert len(name) == len(set(list(name))) and len(age) == len(set(list(age))) and len(clas) == len(set(list(clas))), "Есть повторяющиеся питомцы"