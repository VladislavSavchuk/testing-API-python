"""Методы для проверки ответов запросов"""

# импортируем json для преобразования ответа
import json

# импортируем класс Response из стандартной библиотеки requests
from requests import Response

# Добавляем декоратор @staticmethod. Делаем методы статическими (без self). Созданный метод не привязывается
# к классу Checking, и может вызываться в любом другом классе или тесте


class Checking:
    """Метод для проверки статус-кода ответа"""
    @staticmethod
    # Создаем переменную response, указываем ответ Response (для этого импортируем библиотеку requests)
    # и указываем параметр, который хотим проверить - status_code
    def check_status_code(response: Response, status_code):
        print(f'Status-code: {response.status_code}')
        # проверяем на ассерт
        assert status_code == response.status_code
        print(f'TEST PASSED! Status-code: {response.status_code}')


    """Методы для проверки ключей обязательных полей в ответе запроса"""

    """Метод для проверки обязательных ключей в ответе"""
    @staticmethod
    # метод будет включать: ответ, ожидаемый ключ
    def check_json_token(response: Response, expected_token):
        # loads преобразует ответ response в формат json и присваиваем переменной token
        token = json.loads(response.text)
        # проверяем на ассерт
        assert list(token) == expected_token
        print('TEST PASSED! All required keys are present in the response')

    """Метод для проверки ключей внутри ключа 'booking' """
    @staticmethod
    # метод будет включать: ответ и ожидаемый ключ
    def check_json_token_booking(response: Response, expected_token):
        token = json.loads(response.text)

        # Находим список ключей внутри ключа "booking" и присваиваем переменной booking_keys
        booking_keys = list(token['booking'].keys())
        print(f"List of keys inside a key 'booking': {booking_keys}")

        # проверяем на ассерт
        assert booking_keys == expected_token
        print("TEST PASSED! All fields inside the 'booking' key are present in the response")


    """Методы для проверки значений ключей обязательных полей в ответе запроса"""

    """Метод для проверки id книги"""
    @staticmethod
    # метод будет включать: ответ и название поля
    def check_info_booking_id(response: Response, field_name):
        # Проверяем, является ли значение ключа 'bookingid' целым числом
        # Получаем ответ в json-формате и присваиваем переменной values
        values = response.json()

        # Получаем название необходимого поля из values и присваиваем переменной check_id
        check_id = values.get(field_name)
        print(f'ID: {check_id}')

        # Проверка типа данных переменной check_id. Функция isinstance() возвращает True, если объект (check_id)
        # является экземпляром указанного класса (в данном случае int), и False в противном случае.
        if isinstance(check_id, int):
            print(f"TEST PASSED! The 'bookingid' field is correctly! Value: {check_id} is integer")
        else:
            print(f"TEST FAILED! The value '{check_id}' is not an integer")

    """Метод для проверки значений ключей"""
    @staticmethod
    # метод будет включать: ответ, название поля и ожидаемое значение
    def check_json_value(response: Response, field_name, expected_value):
        # Получаем ответ в json-формате и присваиваем переменной values
        values = response.json()

        # Получаем название необходимого поля из values и присваиваем переменной check_info
        check_info = values.get(field_name)

        # проверяем на ассерт
        assert check_info == expected_value
        print(f"TEST PASSED! The '{field_name}' field is correctly! Value: {check_info}")

    """Метод для проверки значений внутри ключа 'booking' """
    @staticmethod
    # метод будет включать: ответ, название поля и ожидаемое значение
    def check_json_value_in_booking(response: Response, field_name, expected_value):
        # Получаем ответ в json-формате и присваиваем переменной values
        values = response.json()

        # проверка на присутствие ключа 'booking' в ответе
        if 'booking' not in values:
            raise KeyError("The 'booking' key is missing from the response")

        # Получаем словарь значений из ключа 'booking'
        booking_info = values['booking']

        # Проверяем, присутствует ли поле с заданным именем в словаре booking_info
        assert field_name in booking_info, f"TEST FAILED! '{field_name}' field not found in the response"

        # Получаем значение необходимого поля
        actual_value = booking_info[field_name]

        # Проверяем соответствие ожидаемому значению
        assert actual_value == expected_value, (f"The value of field '{field_name}' is invalid."
                                                f"Expected '{expected_value}', received '{actual_value}'")
        print(f"TEST PASSED! '{field_name}' field is correctly! Value: {actual_value}")

    """Метод для проверки значений в ответе запроса по заданному слову"""
    @staticmethod
    # метод будет включать: ответ и ключевое слово
    def check_search_word_in_value(response: Response, search_word):
        # Получаем ответ в text-формате и присваиваем переменной check_info
        check_info = response.text

        # Проверяем ответ
        if search_word in check_info:
            print(f'TEST PASSED! Word {search_word} present in the response')
        else:
            print(f"Word '{search_word}' not found")
