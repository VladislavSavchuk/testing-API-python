"""Создание http-методов"""

# импортируем библиотеку requests для работы с API запросами
import requests

# импортируем библиотеку allure для генерации отчетов в allure
import allure

# импортируем класс logger из файла loggers.py папки utils
from utils.logger import Logger

"""Список http-методов"""


class Http_methods:
    """Передаем заголовки, куки и параметры авторизации вместе с запросами и ответами"""
    # все заголовки будут передаваться в json-формате
    headers = {'Content-Type': 'application/json'}
    # Оставляем пустым т.к. не передаем никакой информации для запоминания системой
    cookie = ""
    # параметры для авторизации
    username = "admin"
    password = "password123"

    # Делаем все методы статическими.
    # Декоратор @staticmethod превращает метод, определенный внутри класса, в обычную функцию, которая не имеет доступа
    # к экземпляру класса self, поэтому ее можно вызывать без создания экземпляра класса (методы не привязываются
    # к классу Http_methods, и могут вызываться в любом другом классе или тесте).

    @staticmethod
    # Передаем url к которой мы будем обращаться
    def get(url):
        # Определение шага allure с описанием "GET"
        with allure.step("GET"):
            # Вызов метода add_request класса Logger для добавления информации о запросе в лог
            Logger.add_request(url, method='GET')
            # Выполнение HTTP-запроса методом GET по указанному URL с передачей заголовков и куки
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            # Вызов метода add_response класса Logger для добавления информации в ответе на запрос в лог
            Logger.add_response(result)
            # Возврат результата запроса
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            # в переменную result передаем параметры url, body, headers, cookies
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body, username, password):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            # в переменную result передаем параметры url, body, headers, cookies и auth
            result = requests.put(url, json=body, headers=Http_methods.headers,
                                  cookies=Http_methods.cookie, auth=(username, password))
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body, username, password):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            # в переменную result передаем параметры url, body, headers, cookies и auth
            result = requests.delete(url, json=body, headers=Http_methods.headers,
                                     cookies=Http_methods.cookie, auth=(username, password))
            Logger.add_response(result)
            return result
